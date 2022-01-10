import argparse
import json
import os
import os.path
import pathlib
import re
import yaml
from yaml.representer import Representer

FIXUPS = (
  ("A P I", "API"),
  ("App Embedded", "App-Embedded"),
  ("C I", "CI"),
  ("C L I", "CLI"),
  ("C V E", "CVE"),
  ("Ecs", "ECS"),
  ("H T T P", "HTTP"),
  ("I Ds", "IDs"),
  ("Ia C", "IaC"),
  ("T A S", "TAS"),
  ("U R L", "URL"),
  ("V M", "VM"),
  ("V Ms", "VMs"),
  ("Wild Fire", "WildFire"),
  ("X S O A R", "XSOAR")
)

# Record that holds all command line params.
#  spec      - OpenAPI JSON
#  topic_map - Topic map YAML
#  local     - How to reference external markdown files (local = relative link on local file system, otherwise HTTPS to GitHub)
class Config:
  pass


def load_spec(f):
  """
  Read the OpenAPI JSON spec
  """
  with open(f, "r") as stream:
    try:
      data = json.load(stream)
    except ValueError as e:
      print('Error: invalid JSON: %s' % e)
      sys.exit(1)

  return data


def load_topic_map(f):
  """
  Read the topic map, which is in YAML format.
  If the file cannot be parsed, exit the program and return 1.
  If the file contains !include references to non-existent files, exit the program and return 1.
  """
  with open(f, "r") as stream:
    try:
      data = yaml.load(stream, Loader=yaml.FullLoader)
    except yaml.YAMLError as e:
      print(f'Error loading {f}: Invalid YAML. {e}')
      sys.exit(1)
    except OSError as e:
      print('Error loading {f}: {e}')
      sys.exit(1)

  return data


def enrich_spec(config):

  add_api_desc(config)
  add_endpoint_operation_id(config.spec)
  add_endpoint_summary(config)
  add_resource_desc(config)
  add_endpoint_desc(config)


def add_api_desc(config):
  """
  Link to the markdown file for API intro.
  """
  spec = config.spec

  spec['info']['description'] = {}
  if config.local:
    spec['info']['description']['$ref'] = "../descriptions/intro.md"
  else:
    spec['info']['description']['$ref'] = f"https://raw.githubusercontent.com/PaloAltoNetworks/prisma-cloud-docs/{config.branch}/api/descriptions/intro.md"


def add_resource_desc(config):
  """
  Link to markdown file for top-level resource description.
  """
  spec = config.spec
  topic_map = config.topic_map

  # "tags" are an array, not a dict.
  # https://realpython.com/python-enumerate/
  for i, tag in enumerate(spec['tags']):
    resource = tag_to_resource(tag)
    link = get_resource_desc_link(config, resource)
    if link:
      spec['tags'][i]['description'] = {}
      spec['tags'][i]['description']['$ref'] = link
    else:
      print(f'WARNING: No top-level desc for {resource}')  

def tag_to_resource(tag):
  """
  Convert tag to a key that can used to lookup the resource in the topic_map
  """
  return f"/{tag['name'].lower()}"


def get_resource_desc_link(config, resource):

  desc = lookup_resource_attr(config.topic_map, resource, 'description')
  if desc:
    link = desc.get_link(config)
    #print(f"FOUND desc for {resource}")
    #print(f"LINK = {link}")
  else:
    link = None

  return link


def add_endpoint_desc(config):
  """
  Link to markdown file that contains each endpoint's description.
  """
  spec = config.spec
  topic_map = config.topic_map

  for route in spec['paths']:
    for method in spec['paths'][route]:
      desc = lookup_endpoint_attr(topic_map, route, method, 'description')
      if desc:
        spec['paths'][route][method]['description'] = {}
        spec['paths'][route][method]['description']['$ref'] = desc.get_link(config)
        #print(f"FOUND desc for {method}{route}")
        #print(f"LINK = {desc.get_link(config)}")
      else:
        print(f'WARNING: No endpoint desc for {method.upper()} {route}')



def add_endpoint_summary(config):
  """
  Get the summary from the topic map and add it to the spec.
  """
  spec = config.spec
  topic_map = config.topic_map

  for route in spec["paths"]:
    for method in spec["paths"][route]:
      summary = lookup_summary(topic_map, route, method)
      if summary:
        # print(f'FOUND summary for {route} {method}')
        spec["paths"][route][method]["summary"] = summary
      else:
        # print(f"No summary in topic map for {route} {method}")
        summary = get_summary_from_desc(spec["paths"][route][method]['description'])
        spec["paths"][route][method]["summary"] = summary
        # print(f"Derived summary = {summary}")


def get_summary_from_desc(desc):

  words = desc.split()
  if len(words) >= 1:
    desc_str = re.split('(?=[A-Z])', words[0])
    desc_str = " ".join(desc_str)
    desc_str = fixup(desc_str)
  else:
    desc_str = "TODO"

  return desc_str


def fixup(desc):

  for substr in FIXUPS:
    if substr[0] in desc:
      desc = desc.replace(substr[0], substr[1])
      #print(f"desc2 = {desc2}")
      break

  return desc


def lookup_summary(topic_map, route, method):
  """
  In the OpenAPI spec file, route has the following format: /api/v1/resource/subresource.
  In the topic map, routes are shorter, and keyed as follows:
    /resource:
      /subresource:
  """
  # Debug
  print(f"Look up summary for {method} {route}")

  route_key1 = None
  route_key2 = None

  parts = route.split('/')

  if len(parts) >= 4:
    route_key1 = '/'
    route_key1 += parts[3]
    #print(f"route_key1 = {route_key1}")

  if len(parts) > 4:
    route_key2 = ''
    for part in parts[4:]:
      route_key2 += '/'
      route_key2 += part
    #print(f"route_key2 = {route_key2}")

  if route_key1 and not route_key2:
    if route_key1 in topic_map:
      if method in topic_map[route_key1]:
        if 'summary' in topic_map[route_key1][method]:
          return topic_map[route_key1][method]["summary"]

  if route_key1 and route_key2:
    if route_key1 in topic_map:
      if route_key2 in topic_map[route_key1]:
        if method in topic_map[route_key1][route_key2]:
          if 'summary' in topic_map[route_key1][route_key2][method]:
            return topic_map[route_key1][route_key2][method]["summary"]

  return None



def lookup_resource_attr(topic_map, resource, key):
  """
  In the OpenAPI spec file, route has the following format: /api/v1/resource/subresource.
  In the topic map, routes are shorter, and keyed as follows:
    /resource:
      displayName:
      description:
      /subresource:
  """
  if resource in topic_map:
    if key in topic_map[resource]:
      return topic_map[resource][key]
  
  return None
  

def lookup_endpoint_attr(topic_map, route, method, key):
  """
  In the OpenAPI spec file, route has the following format: /api/v1/resource/subresource.
  In the topic map, routes are shorter, and keyed as follows:
    /resource:
      /subresource:
  """
  route_key1, route_key2 = get_route_keys(route)

  if route_key1 and not route_key2:
    if route_key1 in topic_map:
      if method in topic_map[route_key1]:
        if key in topic_map[route_key1][method]:
          return topic_map[route_key1][method][key]

  if route_key1 and route_key2:
    if route_key1 in topic_map:
      if route_key2 in topic_map[route_key1]:
        if method in topic_map[route_key1][route_key2]:
          if key in topic_map[route_key1][route_key2][method]:
            return topic_map[route_key1][route_key2][method][key]

  return None


def get_route_keys(route):
  """
  Extract the keys required to lookup an endpoint in _topic_map.yml.

  In the OpenAPI spec file, route has the following format: /api/v1/resource/subresource/subresource.
  In the topic map, routes are shorter, and keyed as follows:
    /resource:
      /subresource:
      /subresource/subresource:
      /subresource/subresource/subresource:
  """
  key1 = None
  key2 = None

  parts = route.split('/')

  if len(parts) >= 4:
    key1 = '/'
    key1 += parts[3]

  if len(parts) > 4:
    key2 = ''
    for part in parts[4:]:
      key2 += '/'
      key2 += part

  return (key1, key2)


def add_endpoint_operation_id(spec):

  for route in spec["paths"]:
    for method in spec["paths"][route]:
      op_id = '-'
      parts = route.split('/')
      op_id = op_id.join(parts[3:])
      mapping = op_id.maketrans({'{': None, '}': None})
      op_id = op_id.translate(mapping)
      spec["paths"][route][method]["operationId"] = f"{method}-{op_id}"


def add_endpoint_operation_id2(spec):

  count = 0
  for route in spec["paths"]:
    for method in spec["paths"][route]:
      spec["paths"][route][method]["operationId"] = f"{count}"
      count += 1


def output_spec(spec):
  """
  Write the enriched spec to a file.
  """
  with open("openapi_enriched.json", "w") as outfile:
    json.dump(spec, outfile, indent=2)


def include_constructor(loader, node):
  value = loader.construct_scalar(node)
  return IncludeFile(value)


# When the YAML deserializer encounters the !include <path> tag, we encode it in this class.
# The path attribute is validated in __init__ to catch authoring errors in _topic_map.yml.
# When hand editing YAML it's easy to make mistakes, so we're being aggressive about catching and reporting
# issues.
#
# Nice discussion about the options for validating attributes in __init__.
# https://mail.python.org/pipermail/python-list/2009-December/562185.html
class IncludeFile(object):
  def __init__(self, path):
    print(path)
    self.path = path
    if not self.validate(path):
      raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), path)

  def __repr__(self):
    return f"IncludeFile({self.path})"

  def validate(self, path):
    return os.path.isfile(self.path)

  def get_link(self, config):
    if config.local:
      link = self.path
    else:
      p = pathlib.PurePosixPath(self.path)
      rel_p = p.relative_to('../')
      link = f"https://raw.githubusercontent.com/PaloAltoNetworks/prisma-cloud-docs/{config.branch}/api/{rel_p}"
    return link

  def append_role(self, role):
    self.modify_file()
    with open(self.path, "a") as stream:
      stream.write('\n')
      stream.write('\n')
      stream.write('### Role')
      stream.write('\n')
      stream.write('Minimum role required to access this endpoint: %s.' % role)

  def modify_file(self):
    """
    If this script modifies a git-versioned file, then it:
      * Creates a temporary working copy of the file where modifications can be made.
        Modified files are kept in repo/_build/tmp/.
      * Updates the path to point to the temp working copy.
      * The intermediate files under repo/_build/tmp/ are ignored with .gitignore.
    """
    # Get the path to the !include file relative to the root of this repo.
    # This Python script runs in repo/_build/.
    tmp_path = os.path.relpath(self.path, '..')
    tmp_path = os.path.join('tmp', tmp_path)
    # print('tmp path: %s' % tmp_path)

    # Does the dir exist already under tmp/?
    # If not, create it.
    dirname = os.path.dirname(tmp_path)
    if os.path.exists(dirname) == False:
      print('new dir name: %s' % dirname)
      os.makedirs(dirname)

    # Copy the file to tmp/
    shutil.copy2(self.path, dirname)

    # Update self.path
    self.path = tmp_path


def main():
  """
  Read the OpenAPI spec file and enrich it.
  Print the result to a file.
  """
  parser = argparse.ArgumentParser(description='Enrich basic OpenAPI spec for publication on pan.dev.')
  parser.add_argument('spec', type=str, help='Path to OpenAPI spec')
  parser.add_argument('topic_map', type=str, help='Path to _topic_map.yml')
  parser.add_argument('--branch', help='Specify the branch from which to retrieve API endpoint descriptions (default: master)')
  parser.add_argument('--local', action='store_true', help='Build for testing locally with redoc-cli')
  args = parser.parse_args()

  config = Config()

  # Specify how to process RAML's !include application-specific tag.
  # See: https://pyyaml.org/wiki/PyYAMLDocumentation
  # See: https://stackoverflow.com/questions/43058050/creating-custom-tag-in-pyyaml
  yaml.add_constructor(u'!include', include_constructor)

  # Read the OpenAPI spec file.
  config.spec = load_spec(args.spec)

  # Read _topic_map.yml
  config.topic_map = load_topic_map(args.topic_map)

  # Get the branch from which to retrieve API endpoint descriptions
  if args.branch:
    config.branch = args.branch
  else:
    config.branch = 'master'

  # Enrich OpenAPI spec for local testing or publication on pan.dev.
  if args.local:
    config.local = args.local
  else:
    config.local = False

  enrich_spec(config)

  output_spec(config.spec)


if __name__ == '__main__':
  main()

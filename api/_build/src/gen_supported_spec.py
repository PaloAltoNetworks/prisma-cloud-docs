import argparse
import collections
import copy
from dataclasses import dataclass
import json
import pathlib
import re


# Constants
COMMA = ","

METHODS = [
  'get', 'head', 'post', 'put', 'delete',
  'connect', 'options', 'trace', 'patch'
]


# Command line arguments
@dataclass()
class Config:
  spec: dict
  inclusions: list
  exclusions: list


# Endpoint read from supported.cfg
@dataclass(frozen=True)
class Endpoint:
  path: str
  method: str


def gen_spec(spec_file, config_file):

  # Read the OpenAPI spec file.
  spec = load_spec_file(spec_file)

  # Read the supported.cfg file.
  inclusions, exclusions = config_file and load_config_file(config_file)

  # Create a config object.
  config = Config(spec, inclusions, exclusions)

  # Generate a new spec file.
  s = update_spec(config)
  return s


# A defaultdict automatically creates any items you try to access that don't exist yet.
# A standard Python dict, in contrast, would throw a KeyError.
def hasher():
  return collections.defaultdict(hasher)


def load_spec_file(f):
  """
  Read the OpenAPI JSON spec file.
  """
  with open(f, "r") as stream:
    try:
      data = json.load(stream)
    except ValueError as e:
      print('Error: invalid JSON: %s' % e)
      sys.exit(1)

  return data


def load_config_file(f):
  """
  Reads the config file and processes the entries.

  Returns a list of inclusions and a list of exclusions. If there are no
  inclusions/exclusions, return empty lists (len == 0).
  """
  inclusions = list()
  exclusions = list()

  with open(f, "r") as stream:
    for line in stream:
      line = line.rstrip('\n')
      # Blank line
      if not line:
        continue
      # Comment
      elif line.startswith("#"):
        continue
      # Inclusion
      elif line.startswith("+"):
        ep = process_config_entry(line)
        if ep: inclusions.append(ep)
      # Exclusion
      elif line.startswith("-"):
        ep = process_config_entry(line)
        if ep: exclusions.append(ep)
      # Unknown
      else:
        print(f"Ignoring line from config file - invalid syntax: {line}")

  return inclusions, exclusions


def process_config_entry(line):

    ep = None

    # Strip out the + or - directive.
    l = line[1:]

    # We expect two values: path and method.
    e = l.split(COMMA, 2)
    if len(e) == 2:
      path, method = e
      path = path.strip()
      method = method.strip().lower()

      if method in METHODS:
        ep = Endpoint(path, method)

    if not ep:
       print(f"Ignoring line from config file - invalid syntax: {line}")    

    return ep


def update_spec(config):

  supported_spec = hasher()
  supported_spec['components'] = copy.deepcopy(config.spec['components'])
  supported_spec['info'] = copy.deepcopy(config.spec['info'])
  supported_spec['openapi'] = copy.deepcopy(config.spec['openapi'])
  supported_spec['tags'] = copy.deepcopy(config.spec['tags'])

  count = 0
  # Work on the paths object
  for path in config.spec['paths']:
    for method in config.spec['paths'][path]:
      ep = config.spec['paths'][path][method]
      if supported_by_tag(ep) or supported_by_cfg(config.inclusions, path, method):
        print(f"Supported endpoint {path}, {method}")
        count += 1
        supported_spec['paths'][path][method] = copy.deepcopy(ep)

  print(f"Count = {count}")

  return supported_spec


def supported_by_tag(ep):
  """
  Checks if the endpoint is tagged as `Supported API`.
  """
  if 'tags' in ep:
    tags = ep['tags']
    for tag in tags:
      if tag == 'Supported API':
        return True
  else:
    return False


def supported_by_cfg(inclusions, path, method):
  """
  Checks if the endpoint is listed in support.cfg.
  """
  # No supported.cfg file was specified on the command line.
  if inclusions is None:
    return False

  for ep in inclusions:
    # How to use a variable in a regex:
    # https://stackoverflow.com/questions/6930982
    full_path = re.compile(rf"/api/v[0-9.]+{re.escape(ep.path)}")
    # Use fullmatch() to exactly match the path. match() returns true if full_path
    # is a substring in path. For example, you get a false positive match for:
    # full_string = /api/v1/scans, post
    # path = /api/v1/scans/sonatype, post
    if full_path.fullmatch(path):
      if ep.method == method:
        return True

  return False


def output_spec(spec):
  """
  Write the spec to a file.
  """
  with open("openapi_supported.json", "w") as outfile:
    json.dump(spec, outfile, indent=2)


def main():
  """
  Read the OpenAPI spec file and split it into micro-specs.
  Save each micro-spec to a file in a subdirectory named micro-specs.
  """
  parser = argparse.ArgumentParser(description='Generates an OpenAPI spec with supported endpoints only')
  parser.add_argument('spec',
    help='Path to OpenAPI spec file')
  parser.add_argument('config', nargs='?', default=None,
    help='(Optional) Path to supported.cfg, which overrides which endpoints to include and exclude')
  args = parser.parse_args()

  s = gen_spec(args.spec, args.config)

  output_spec(s)


if __name__ == '__main__':
  main()

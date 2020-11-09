import argparse
import collections
import errno
import json
import os
import os.path
import re
import shutil
import sys
import yaml
from yaml.representer import Representer

COMMA         = ","
NEW_LINE      = "\n"
NEW_PARAGRAPH = "\n\n"

# ANSI escape sequences to output formatted (color, style) text
CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CSELECTED = '\33[7m'

CBLACK    = '\33[30m'
CRED      = '\33[31m'
CGREEN    = '\33[32m'
CYELLOW   = '\33[33m'
CBLUE     = '\33[34m'
CVIOLET   = '\33[35m'
CBEIGE    = '\33[36m'
CWHITE    = '\33[37m'
CGRAY     = '\33[90m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

# Global variables
suppress_partial = list()
suppress_exact = list()

# A defaultdict automatically creates any items you try to access that don't exist yet.
# A standard Python dict, in contrast, throws a KeyError.
# https://docs.python.org/2/library/collections.html
# https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
# https://stackoverflow.com/questions/19321776/need-to-omit-values-from-yaml-output-when-using-defaultdict
def hasher():
  return collections.defaultdict(hasher)

# When the YAML deserializer encounters the !include <path> tag, we encode it in this class.
# The path attribute is validated in __init__ to catch authoring errors in _topic_map.yml.
# When hand editing YAML it's easy to make mistakes, so we're being aggressive about catching and reporting
# issues.
#
# Nice discussion about the options for validating attributes in __init__.
# https://mail.python.org/pipermail/python-list/2009-December/562185.html
class IncludeFile(object):
  def __init__(self, path):
    self.path = path
    if not self.validate(path):
      raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), path)

  def __repr__(self):
    return "IncludeFile(%s)" % self.path

  def validate(self, path):
    return os.path.isfile(self.path) 

  def append_role(self, role):
    self.modify_file()
    with open(self.path, "a") as stream:
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


def include_constructor(loader, node):
  value = loader.construct_scalar(node)
  return IncludeFile(value)


def include_representer(dumper, data):
  return dumper.represent_scalar(u'!include', data.path)


def generate_raml(api_json, add_json):

  #api_raml = {}
  api_raml = hasher()

  for endpoint in api_json:
    generate_raml_endpoint(api_raml, endpoint)

  if add_json:
    for endpoint in add_json:
      check_endpoint_in_json(endpoint, api_json)
      generate_raml_endpoint(api_raml, endpoint)

  add_long_descriptions(api_raml)

  write_raml_file(api_raml)

  # Python f-Strings are supported in Python 3.6+ only.
  # It makes sense to upgrade the Jenkins build to support Python 3.7+,
  # but given the transition to PAN, it's not worth the effort until we
  # figure out the direction for docs.
  # print(f"{CGREEN}RAML file successfully generated.{CEND}")
  print("%sRAML file successfully generated.%s" % (CGREEN, CEND))

def check_endpoint_in_json(endpoint, api_json):
  """
  Print a warning message if dev's API JSON contains the endpoint being added via add_json.
  Rationale: dev strives to add all endpoints to the API JSON. If it it's in the API JSON, that definition
  should be considered authoritative. Endpoints in add_json are a temporary band-aid for stuff dev can't
  get in because of development cycle pressures.
  """
  route = endpoint['path'].lower()
  method = endpoint['action'].lower()

  for ep in api_json:
    route_compare = ep['path'].lower()
    method_compare = ep['action'].lower()
    if(route_compare == route):
      if(method_compare == method):
        print("WARNING: Endpoint " + method + " " + route + " exists in the main API JSON already.\n")


def is_suppress(method, route):
  """
  Check the endpoint against the list of endpoints in suppress.cfg.
  If it's in suppress.cfg, return True. Otherwise, return False.
  """
  global suppress_partial
  global suppress_exact

  for x in suppress_exact:
    if route == x[0]:
      if method == x[1]:
        return True

  # If this endpoint is in the suppress list, return. There is no work to do.
  # This simple one liner is a Python generator expression.
  # For more info, see:
  # https://www.python.org/dev/peps/pep-0289/
  # https://stackoverflow.com/questions/2783969/compare-string-with-all-values-in-array
  # https://stackoverflow.com/questions/16505456/how-exactly-does-the-python-any-function-work
  if any(x in route for x in suppress_partial):
    return True

  return False


def generate_raml_endpoint(api_raml, endpoint):

  # Without casting these vars to type str, they're type unicode.
  # When the YAML gets serialized, there is no representer for unicode, so method gets rendered as !!python/unicode post, and the
  # raml2html processor skips it because it doesn't know what to do with it.
  # Force everything to type str.
  route = str(endpoint['path'].lower())
  method = str(endpoint['action'].lower())

  # Debug
  # print('Working on %s %s' % (method.upper(), route))

  if is_suppress(method, route):
    #print(f"Suppress {method.upper()} {route}")
    print("Suppress %s %s" % (method.upper(), route))
    return

  resource = get_resource(route)
  subresource = get_subresource(route)

  if subresource != '':
    node = api_raml[resource][subresource][method]
  else:
    node = api_raml[resource][method]

  # Encode security (basic auth, access token)
  encode_security(node, route)

  # Encode long description
  if 'comments' in endpoint:
    encode_long_desc(node, endpoint)

  # Encode the request parameters 
  if 'in' in endpoint:
    encode_request(node, endpoint)

  # Encode the response
  if 'out' in endpoint:
    encode_response(node, endpoint)

  # Encode the query parameters{
  if 'queryParam' in endpoint:
    encode_query_params(node, endpoint)


def get_resource(route):
  """
  Return the first-level resource from an endpoint.
  For example, if route is '/api/v1/containers', then this function returns '/containers'.
  """
  segments = route.split('/')
  return '/' + segments[3]


def get_subresource(route):
  """
  Return everything past the first-level resource from an endpoint.
  For example, if the route is '/api/v1/audits/incidents/acknowledge/{id}', return '/acknowledge/{id}'.
  Nifty split trick from SO: https://stackoverflow.com/questions/12572362/get-a-string-after-a-specific-substring
  """
  resource = route.split('/')[3]
  split_str = '/api/v1/' + resource
  subresource = route.split(split_str,1)[1]
  return subresource


def encode_security(node, route):
  """
  If the endpoint requires auth to access it, add the relevent RAML.
  Most endpoints are secured with basic auth and JWT tokens.
  These security schemes are described in static RAML files in the repo.
  """
  exempt = ['/api/v1/authenticate', '/api/v1/authenticate-client', '/api/v1/signup', '/api/v1/_ping']

  if route not in exempt:
    node['securedBy'] = ['basicAuth', 'jwtAccessToken']


def encode_long_desc(node, endpoint):
  """
  Generate a long description for the endpoint.

  By default, use engineering's long description.
  This will most likely be overwritten by the CTO-maintained long
  description later in the API doc generation process (see
  the add_long_descriptions function).

  However, if there is no CTO content (which should be temporary),
  then this will at least provide some basic info. It's better than
  being blank.

  Also, add a node called role to the endpoint RAML.
  This is not 'valid' RAML, but it's safely ignored by the raml2html
  processor. We use it as temp storage so when add_long_descriptions()
  is called for the endpoint, the role information can be easily
  grabbed and added to the markdown file.
  """
  long_desc = str(endpoint['comments'])
  role = str(endpoint['minRole'])

  # Clean up long_desc string.
  # * Remove any line feeds escape sequences (\n) from the end of the line.
  # * Add a period to the end of the line if it doesn't exist.
  long_desc = long_desc.replace('\n', '')
  if not long_desc.endswith('.'):
    long_desc += '. '

  role_desc = 'Minimum role required to access this endpoint: %s.' % role
  long_desc += role_desc

  node['description'] = long_desc
  node['minRole'] = role


def encode_request(node, endpoint):
  """
  Generate RAML for the endpoint's request params.
  """
  properties = hasher()
  encode_properties(endpoint['in'], properties)
  node['body']['properties'] = properties


def encode_response(node, endpoint):
  """
  Generate RAML for the endpoint's response params.
  """
  properties = hasher()
  encode_properties(endpoint['out'], properties)
  node['responses'][200]['description'] = 'Success'
  node['responses'][200]['body']['properties'] = properties


def encode_query_params(node, endpoint):
  """
  Generate RAML for the endpoint's query parameters.
  """
  properties = hasher()
  encode_properties(endpoint['queryParam'], properties)
  node['queryParameters'] = properties


def encode_properties(endpoint_fragment, properties):
  """
  Extract and encode all properties.
  Recursive algorithm handles artibrary depth.
  """
  if 'fields' in endpoint_fragment:
    if endpoint_fragment['fields'] != None:
      for prop in endpoint_fragment['fields']:
        if 'name' in prop:
          prop_name = str(prop['name'])
        else:
          # If there is no property name, we've got an error in the API JSON.
          # File a bug with engineering, but continue processing.
          #print('Input JSON Error: No name for property. JSON:  %s' % endpoint_fragment)
          print('Input JSON Error: No name for property')
          continue

        # Set the property description
        prop_desc = get_prop_desc(prop)
        properties[prop_name]['description'] = prop_desc
        
        # Set the property type
        prop_type = get_prop_type(prop)
        set_prop_type(properties[prop_name], prop_type)

        properties[prop_name]['required'] = False

        if 'value' in prop:
          if prop['value'] != None:
            encode_properties(prop['value'], properties[prop_name]['properties'])


def get_prop_desc(prop):

  if 'comments' in prop:
    prop_desc = str(prop['comments'])
    prop_desc = prop_desc.replace('\n', '')
  else:
    prop_desc = ''

  if 'value' in prop:
    if 'values' in prop['value']:
      prop_desc += '. Range of acceptable values: '
      for val in prop['value']['values']:
        if val == "":
          continue
        else:
          prop_desc += '`' + val + '`, '
      # Strip the last comma
      prop_desc = prop_desc[:-2]

  return prop_desc


def get_prop_type(prop):
  """
  Get the property type. Twistlock JSON uses the following types:
    * bool
    * int
    * int64
    * float32
    * float64
    * shared.*
    * string
    * time.Time
  """
  if 'value' in prop:
    if 'type' in prop['value']:
      return prop['value']['type']


def set_prop_type(prop, prop_type):
  """
  Set the property type. The RAML 1.0 specification has the following scalar types:
    * string
    * number
    * integer
    * boolean
    * date
  """
  if prop_type == 'string':
    prop['type'] = 'string'
  elif prop_type == 'bool':
    prop['type'] = 'boolean'
  elif prop_type == 'time.Time':
    prop['type'] = 'datetime'
  elif prop_type == 'int':
    prop['type'] = 'integer'
    prop['format'] = 'int'
  elif prop_type == 'int64':
    prop['type'] = 'integer'
    prop['format'] = 'int64'
  elif prop_type == 'float32':
    prop['type'] = 'number'
    prop['format'] = 'float'
  elif prop_type == 'float64':
    prop['type'] = 'number'
    prop['format'] = 'double'
  else:
    prop['type'] = 'object'


def add_long_descriptions(api_raml):
  """
  Long descriptions are authored and maintained by the CTO team in markdown files that
  are checked into this repo. The _topic_map.yml file maps endpoints to long
  description files.

  Assume just two levels: resource and subresource.

  Example: The /users endpoint

    /users = {
      'displayName': 'Users',
      'description': IncludeFile(../descriptions/users/users.md),
      'get': IncludeFile(../descriptions/users/get.md),
      'put': IncludeFile(../descriptions/users/put.md),
      '/password': {
        'put': IncludeFile(../descriptions/users/password_put.md)
      },
      '/{id}': {
        'delete': IncludeFile(../descriptions/users/id_delete.md)
      }
    }
  """
  methods = ['get', 'post', 'delete', 'put', 'patch']

  # Open and read the topic map.
  # If the file cannot be parsed, exit the program and return 1.
  # If the file contains !include references to non-existent files, exit the program and return 1.
  with open("../_topic_map.yml", "r") as stream:
    try:
      data = yaml.load(stream)
    except yaml.YAMLError as e:
      print('XXX Error XXX _topic_map.yml: Invalid YAML %s' % e)
      sys.exit(1)
    except OSError as e:
      print('XXX Error XXX _topic_map.yml: %s' % e)
      sys.exit(1)

  # Handle level 1 nodes.
  for resource,elements in data.items():

    # CTO content exists for an endpoint that doesn't exist in this version of the API JSON.
    # Skip processing it.
    if resource not in api_raml:
      print('CTO CONTENT CLEANUP: Top level resource' + resource)
      print('  Defined in _topic.map.yml, but does not exist in the API JSON.')
      print('  This might have happened because the endpoint is in the suppress list.\n')
      continue

    for key in elements:

      if key == 'displayName':
        api_raml[resource]['displayName'] = elements['displayName']
       
      elif key == 'description':
        api_raml[resource]['description'] = elements['description']
      
      elif key in methods:
        if key in api_raml[resource]:
          api_raml[resource][key]['description'] = elements[key]
          elements[key].append_role(str(api_raml[resource][key]['minRole']))
        else:
          print('CTO CONTENT CLEANUP: Endpoint ' + key.upper() + ' ' + resource)
          print('  Defined in _topic.map.yml, but does not exist in the API JSON')
          print(' ')

      elif key.startswith('/'):
        subresource = key
        subelements = elements[key]

        # Handle level 2 nodes.
        for subkey in subelements:
          if subkey in methods:
            if subkey in api_raml[resource][subresource]:
              api_raml[resource][subresource][subkey]['description'] = subelements[subkey]
              subelements[subkey].append_role(str(api_raml[resource][subresource][subkey]['minRole']))
            else:
              print('CTO CONTENT CLEANUP: Endpoint ' + subkey.upper() + ' ' + resource + subresource)
              print('  Defined in _topic.map.yml, but does not exist in the API JSON')
              print(' ')

          else:
            # Handles the case when there is a typo (human error) in _topic_map.yml.
            # A typo would likely be an invalid key, which the raml2html processor will just ignore when generating the HTML.
            # For example, 'grt' which should be 'get'.
            print('XXX Warning XXX _topic_map.yaml: Unhandled node %s in %s %s' % (subkey, resource, subresource))

      else:
        # Handles the case when there is a typo (human error) in _topic_map.yml.
        # A typo would likely be an invalid key, which the raml2html processor will just ignore when generating the HTML.
        # For example, 'dispayName' which should be 'displayName'.
        print('XXX Warning XXX _topic_map.yaml: Unhandled node %s in %s' % (key, resource))


def write_raml_file(api_raml):
  """
  The final RAML file is constructed from two sources:
    * api.raml: The API header. A flat file at the root of the repo.
    * api_raml: Per-endpoint documentation. A YAML struct generated by this script from the API JSON manifest
  """
  with open("twistlock_api.raml", "w") as outfile:
    lines = []
    lines.append('#%RAML 1.0')
    lines.append(NEW_LINE)
    outfile.writelines(lines)

    header = get_raml_header()
    yaml.dump(header, outfile, default_flow_style=False)
    yaml.dump(api_raml, outfile, default_flow_style=False)


def get_raml_header():

  # Open and read the topic map.
  # If the file cannot be parsed, exit the program and return 1.
  # If the file contains !include references to non-existent files, exit the program and return 1.
  with open("../api.raml", "r") as stream:
    try:
      data = yaml.load(stream)
    except yaml.YAMLError as e:
      print('XXX Error XXX _topic_map.yml: Invalid YAML %s' % e)
      sys.exit(1)
    except OSError as e:
      print('XXX Error XXX _topic_map.yml: %s' % e)
      sys.exit(1)
  return data


def read_suppress_cfg(f):
  """
  Read the suppress.cfg file, and save each entry to the global variable suppress, which is of type list.
  """
  with open(f, "r") as stream:
    for line in stream:
      if line.startswith("#"):
        continue
      else:
        ep = line.rstrip('\n')
        process_suppress_entry(ep)


def process_suppress_entry(ep):

  global suppress_partial
  global suppress_exact

  if not ep:
    # Empty string
    # https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty
    return
  elif COMMA in ep:
    suppress_exact.append(ep.split(COMMA))
  else:
    suppress_partial.append(ep)


def read_api_json(f):

  with open(f, "r") as stream:
    try:
      json_obj = json.load(stream)
    except ValueError as e:
      print('XXX Error XXX Invalid JSON: %s' % e)
      sys.exit(1)

  return json_obj


def report_missing_endpoint_descs(api_json):
  """
  For each endpoint in the API JSON, check the topic map for an entry.
  If there isn't one, then report it so that we can open an issue.
  """
  missing = list()

  # Open and read the topic map.
  # If the file cannot be parsed, exit the program and return 1.
  # If the file contains !include references to non-existent files, exit the program and return 1.
  with open("../_topic_map.yml", "r") as stream:
    try:
      topic_map = yaml.load(stream)
    except yaml.YAMLError as e:
      print('XXX Error XXX _topic_map.yml: Invalid YAML %s' % e)
      sys.exit(1)
    except OSError as e:
      print('XXX Error XXX _topic_map.yml: %s' % e)
      sys.exit(1)

    for endpoint in api_json:
      if missing_from_topic_map(endpoint, topic_map):
        missing.append(endpoint)

    if missing:
      print_missing_report(missing)


def missing_from_topic_map(endpoint, topic_map):
  """
  If there's no entry in the _topic.map file for the given endpoint,
  then return True. Otherwise, return False.
  """
  route = str(endpoint['path'].lower())
  method = str(endpoint['action'].lower())

  # If the endpoint is listed in suppress.cfg, then we don't care if there
  # isn't an entry in _topic.map.
  if is_suppress(method, route):
    return False

  resource = get_resource(route)
  subresource = get_subresource(route)

  if subresource:
    return missing_from_topic_map_sub(topic_map, resource, subresource, method)
  else:
    return missing_from_topic_map_res(topic_map, resource, method)


def missing_from_topic_map_res(topic_map, resource, method):

  missing = True

  if resource in topic_map:
    if method in topic_map[resource]:
      missing = False

  return missing


def missing_from_topic_map_sub(topic_map, resource, subresource, method):

  missing = True

  if resource in topic_map:
    if subresource in topic_map[resource]:
      if method in topic_map[resource][subresource]:
        missing = False

  return missing


def print_missing_report(missing):
  
  #print(f"{CYELLOW}The following endpoints need long descriptions. Add them with _topic.map.{CEND}")
  print("%sThe following endpoints need long descriptions. Add them with _topic.map.%s" % (CYELLOW, CEND))

  for endpoint in missing:
    route = str(endpoint['path'].lower())
    method = str(endpoint['action'].lower())
    #print(f" {CGRAY}{method.upper()} {route}{CEND}")
    print(" %s%s %s%s" % (CGRAY, method.upper(), route, CEND))


def main():
  """
  Read the JSON API manifest and construct the API definition in RAML (~YAML) format.
  Output the RAML struct to a file.
  The resulting RAML file will be transformed into HTML with a separate tool outside of this program (raml2html).
  """
  parser = argparse.ArgumentParser(description='Generate the API docs from the JSON manifest file.')
  parser.add_argument('api_json', type=str, help='Path to API JSON file')
  parser.add_argument('-a', '--add', type=str, help='Path to supplemental API JSON file that contains additional endpoints')
  parser.add_argument('-s', '--suppress', type=str, help='Path to suppress.cfg, which lists the endpoints that shouldn\'t be documented')
  args = parser.parse_args()

  # Define RAML's !include application-specific tag.
  # See: https://pyyaml.org/wiki/PyYAMLDocumentation
  # See: https://stackoverflow.com/questions/43058050/creating-custom-tag-in-pyyaml
  yaml.add_representer(IncludeFile, include_representer)
  yaml.add_constructor(u'!include', include_constructor)

  # Add representer for the defaultdict type. Cleans the output when the RAML is serialized.
  # https://stackoverflow.com/questions/19321776/need-to-omit-values-from-yaml-output-when-using-defaultdict
  yaml.add_representer(collections.defaultdict, Representer.represent_dict)

  # Open and read the Twistlock API JSON manifest file.
  # If the file cannot be parsed, exit the program and return 1.
  api_json = read_api_json(args.api_json)

  # Open and read the optional supplemental API JSON manifest file.
  # This file contains any valid endpoints not captured in engineering's API JSON.
  # If the file cannot be parsed, exit the program and return 1.
  add_json = None
  if args.add:
    add_json = read_api_json(args.add)

  # Read suppress.cfg
  if args.suppress:
    read_suppress_cfg(args.suppress)

  # Generate the RAML source file
  generate_raml(api_json, add_json)

  # Report endpoints that need documentation
  report_missing_endpoint_descs(api_json)
  if add_json:
    report_missing_endpoint_descs(add_json)

  # Print final status
  #print(f"{CGREEN}OK{CEND}")
  print("%sOK%s" % (CGREEN, CEND))


if __name__ == '__main__':
  main()

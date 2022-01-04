import argparse
import collections
import copy
import json
import pathlib
import re


# Constants
COMMA = ","


# Record that holds all command line params.
#  spec      - OpenAPI JSON
class Config:
  pass


# A defaultdict automatically creates any items you try to access that don't exist yet.
# A standard Python dict, in contrast, throws a KeyError.
def hasher():
  return collections.defaultdict(hasher)


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


def gen_spec(config):

  found = list()

  supported_spec = hasher()
  supported_spec['components'] = copy.deepcopy(config.spec['components'])
  supported_spec['info'] = copy.deepcopy(config.spec['info'])
  supported_spec['openapi'] = copy.deepcopy(config.spec['openapi'])
  supported_spec['tags'] = copy.deepcopy(config.spec['tags'])

  count = 0
  # Work on the paths object
  for path in config.spec['paths']:
    for method in config.spec['paths'][path]:
      if supported(config, path, method):
        print(f"Supported endpoint {path}, {method}")
        count += 1
        supported_spec['paths'][path][method] = copy.deepcopy(config.spec['paths'][path][method])

  print(f"Count = {count}")
  output_spec(supported_spec)


def supported(config, path, method):
  """
  Checks if the endpoint passed to this function is listed in support.cfg
  """
  #print(f"Endpoint {path}, {method}")

  for endpoint in config.supported:
    full_path = re.compile(rf"/api/v[0-9.]+{re.escape(endpoint[0])}")
    # Use fullmatch() to exactly match the path. match() returns true if full_path
    # is a substring in path. For example, you get a false positive  match for:
    # full_string = /api/v1/scans, post
    # path = /api/v1/scans/sonatype, post
    if full_path.fullmatch(path):
      if endpoint[1] == method:
        return True

  return False  


def output_spec(spec):
  """
  Write the spec to a file.
  """
  with open("openapi_supported.json", "w") as outfile:
    json.dump(spec, outfile, indent=2)


def read_supported_cfg(f):
  """
  Read the supported.cfg file, and save each entry to the global variable suppress, which is of type list.
  """
  endpoints = list()

  with open(f, "r") as stream:
    for line in stream:
      line = line.rstrip('\n')
      if not line:
        # Empty string
        continue
      elif line.startswith("#"):
        # Comment
        continue
      else:
        ep = line.split(COMMA)
        endpoints.append(ep)

  return endpoints


def main():
  """
  Read the OpenAPI spec file and split it into micro-specs.
  Save each micro-spec to a file in a subdirectory named micro-specs.
  """
  parser = argparse.ArgumentParser(description='Generate an OpenAPI spec with supported endpoints only')
  parser.add_argument('spec', type=str, help='Path to OpenAPI spec')
  parser.add_argument('supported', type=str, help='Path to supported.cfg, which lists the endpoints should be documented')
  args = parser.parse_args()

  config = Config()

  # Read the OpenAPI spec file.
  config.spec = load_spec(args.spec)

  # Read the supported.cfg file
  config.supported = read_supported_cfg(args.supported)

  gen_spec(config)


if __name__ == '__main__':
  main()

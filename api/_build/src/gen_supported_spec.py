import argparse
import collections
import copy
from dataclasses import dataclass
import json
import pathlib
import re


# Constants
COMMA = ","


# Command line arguments
@dataclass()
class Config:
  spec: dict
  inclusions: list


# Endpoint entry read from supported.cfg
@dataclass(frozen=True)
class Endpoint:
  path: str
  method: str


def gen_spec(spec_file, config_file):

  # Read the OpenAPI spec file.
  spec = load_spec_file(spec_file)

  # Read the supported.cfg file
  inclusions = config_file and load_config_file(config_file)

  config = Config(spec=spec, inclusions=inclusions)
  supported_spec = update_spec(config)

  output_spec(supported_spec)


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
  Read the supported.cfg file and save each entry to a list.
  """
  endpoints = list()

  with open(f, "r") as stream:
    for line in stream:
      line = line.rstrip('\n')
      if not line:
        # Blank line
        continue
      elif line.startswith("#"):
        # Comment
        continue
      else:
        path, method = line.split(COMMA)
        ep = Endpoint(path=path, method=method)
        endpoints.append(ep)

  return endpoints


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
  parser.add_argument('spec', help='Path to OpenAPI spec file')
  parser.add_argument('config', nargs='?', default=None, help='(Optional) Path to supported.cfg, which lists non-versioned endpoints to include and versioned endpoints to  exclude')
  args = parser.parse_args()

  gen_spec(args.spec, args.config)


if __name__ == '__main__':
  main()

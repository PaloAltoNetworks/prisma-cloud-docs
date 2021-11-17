import argparse
import collections
import copy
import json
import pathlib


FIXUPS = (
  ("Coderepos", "Code-Repos"),
  ("Coderepos-Ci", "Code-Repos-CI"),
  ("Cves", "CVEs"),
  ("Iac", "IaC"),
  ("Rbac", "RBAC"),
  ("Tas-Droplets", "TAS-Droplets"),
  ("Vms", "VMs"),
  ("Xsoar-Alerts", "XSOAR-Alerts")
)


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


def split_spec(config):

  for tag in config.spec['tags']:
    #print(tag)
    micro_spec = hasher()
    micro_spec['components'] = copy.deepcopy(config.spec['components'])
    micro_spec['info'] = copy.deepcopy(config.spec['info'])
    micro_spec['openapi'] = copy.deepcopy(config.spec['openapi'])
    tag_desc = tag.pop('description', None)
    micro_spec['tags'] = [copy.deepcopy(tag)]
    #print(tag_desc)

    # Get tag name
    #tag_pub = fixup(tag['name'])

    # Work on info object
    micro_spec['info']['title'] = f"{tag['name']} Overview"
    if tag_desc:
      micro_spec['info']['description'] = tag_desc
    else:
      info_obj = micro_spec['info']
      info_obj.pop('description', None)

    # Gather all endpoints with this tag
    paths = get_all_paths(config.spec, tag['name'])
    if paths:
      micro_spec['paths'] = paths
      output_spec(micro_spec, tag['name'])


def fixup(s):

  for substr in FIXUPS:
    if substr[0] == s:
      return substr[1]

  return s


def get_all_paths(spec, tag):

  print(f"Tag name = {tag}")

  paths_collection = hasher()
  for path in spec['paths']:
    for method in spec['paths'][path]:
      if 'tags' in spec['paths'][path][method]:
        for path_tag in spec['paths'][path][method]['tags']:
          if tag == path_tag:
            paths_collection[path][method] = spec['paths'][path][method]

  return paths_collection


def output_spec(spec, f):
  """
  Write the spec to a file.
  """
  pathlib.Path("micro-specs/").mkdir(parents=True, exist_ok=True) 

  out = pathlib.PurePosixPath("micro-specs/", f"{f}.json")
  with open(out, "w") as outfile:
    json.dump(spec, outfile, indent=2)


def main():
  """
  Read the OpenAPI spec file and split it into micro-specs.
  Save each micro-spec to a file in a subdirectory named micro-specs.
  """
  parser = argparse.ArgumentParser(description='Split an OpenAPI spec into micro-specs')
  parser.add_argument('spec', type=str, help='Path to OpenAPI spec')
  args = parser.parse_args()

  config = Config()

  # Read the OpenAPI spec file.
  config.spec = load_spec(args.spec)

  split_spec(config)


if __name__ == '__main__':
  main()

import argparse
import json


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


def list_endpoints(spec):

  count = 0

  for path in spec['paths']:
    for method in spec['paths'][path]:
      print(f"{path}, {method}")
      count += 1

  print(f"\nCount: {count}")


def list_supported_endpoints(spec):

  count = 0

  for path in spec['paths']:
    for method in spec['paths'][path]:
      ep = spec['paths'][path][method]
      tags = ep.get('tags', [])
      if 'Supported API' in tags:
        print(f"{path}, {method}")
        count += 1
        
  print(f"\nCount: {count}")


def main():
  """
  Read the OpenAPI spec file list endpoints by versioned and non-versioned
  """
  parser = argparse.ArgumentParser(description='List endpoints')
  parser.add_argument('spec', type=str, help='Path to OpenAPI spec')
  parser.add_argument('--supported', action="store_true", help='List endpoints tagged as supported only')
  args = parser.parse_args()

  # Read the OpenAPI spec file.
  spec = load_spec(args.spec)

  if args.supported:
    list_supported_endpoints(spec)
  else:
    list_endpoints(spec)


if __name__ == '__main__':
  main()

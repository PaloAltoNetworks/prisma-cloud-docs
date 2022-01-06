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

  for path in spec['paths']:
    print(path)


def main():
  """
  Read the OpenAPI spec file list endpoints by versioned and non-versioned
  """
  parser = argparse.ArgumentParser(description='List endpoints')
  parser.add_argument('spec', type=str, help='Path to OpenAPI spec')
  args = parser.parse_args()

  # Read the OpenAPI spec file.
  spec = load_spec(args.spec)

  list_endpoints(spec)


if __name__ == '__main__':
  main()

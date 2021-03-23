# Prisma Cloud Compute API documentation

To prepare the API docs for publication on pan.dev:

* Install Python 3.8 (using something like pyenv)

Run the following commands from the `_build` directory:

1. `$ python enrich_spec.py <openapi_spec_file> <topic_map>`
2. `$ python gen_micro_specs.py <enriched_openapi_spec_file>`

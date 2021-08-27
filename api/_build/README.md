# Generate CWPP API docs

The CWPP API docs consist of an OpenAPI spec file, combined with additional per-endpoint content from this repo.

The scripts in this directory add the content from this repo to the spec, and then prepare the spec file for publication on prisma.pan.dev.

## Running the scripts

1. Set up a Python 3.8 environment on your machine using pyenv.

1. Create a virtualenv, and activate it.

1. Install the package deps.

   `$ pip install -r requirements.txt`

1. Generate a spec file that contains supported endpoints only.

   This step generates a file called `openapi_supported.json`.

   `$ python gen_supported_spec.py <PATH-TO-COMPUTE-SPEC-FILE> ./supported.cfg`

1. Add the content from the docs repo to the new spec file.

    This step generates a file called `openapi_enriched.json`.

   `$ python enrich_spec.py ./openapi_supported.json ../_topic_map.yml`

1. Prepare the spec for publication on prisma.pan.dev.

   This step generates a directory called `micro-specs`.

   `$ python gen_micro_specs.py openapi_enriched.json`

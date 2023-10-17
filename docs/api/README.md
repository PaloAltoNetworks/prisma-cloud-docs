# Prisma Cloud Compute (CWP) API Docs

The CWP API docs consist of an OpenAPI spec file, combined with additional per-endpoint content from this repo.

The scripts in the `_build/` directory add the content from this repo to the spec, and then prepare the spec file for publication on prisma.pan.dev.

## Generating the API docs

1. Set up a Python 3.9.6 environment on your machine using pyenv.

1. Create a virtualenv, and activate it.

1. Install the package deps.

   `$ pip install -r requirements.txt`

1. Go to the prisma-cloud-docs/api directory.

   `$ cd prisma-cloud-docs/api/_build`

1. Generate a spec file that contains supported endpoints only.

   This step generates a file called `openapi_supported.json`.

   `$ python src/gen_supported_spec.py <PATH-TO-COMPUTE-SPEC-FILE> ../supported.cfg`

1. Add the content from the docs repo to the new spec file.

   This step generates a file called `openapi_enriched.json`.

   `$ python src/enrich_spec.py openapi_supported.json ../_topic_map.yml`

   By default, branch is master. 
   Note that `enrich_spec.py` accepts an optional `--branch` argument, so you can point to specific revisions of the content.

   **Caution**: You must generate microspecs from the master branch unless advised explicitly. This avoids 404 error if the branch is deleted.

1. Prepare the spec for publication on prisma.pan.dev.

   This step generates a directory called `micro-specs`.

   `$ python src/gen_micro_specs.py openapi_enriched.json`

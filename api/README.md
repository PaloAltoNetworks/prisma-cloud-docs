# Prisma Cloud Compute API documentation

To build the api docs:

1. Install python3
2. Install raml2html

Run the following commands from the `_build` directory:

1. `$ python twapi_gen.py api_<version>.json -s suppress.cfg -a add_endpoints.json`
2. `$ raml2html twistlock_api.raml > twistlock_api.html`

For raml2html, the -v option (validate) is no longer passing.
This should be fixed.
For more info, see https://github.com/twistlock/api-docs/issues/76

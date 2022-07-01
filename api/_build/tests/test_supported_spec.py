"""
Test that the generated spec file contains supported endpoints only.

Endpoints are identified as supported when they are:

* Tagged as `Supported API` in the input spec file.
* Included or excluded via a config file. The config file overrides
  the tags in the input spec file.
"""
import json
import gen_supported_spec


def test_no_supported_endpoints(datadir):
    """No endpoint in the input OpenAPI spec is tagged as supported."""
    # GIVEN a spec file that has a single endpoint that's not tagged as supported
    spec_file = datadir / 'openapi_no_supported_endpoints.json'
    with open(spec_file) as f:
        input_spec = json.load(f)
    config = gen_supported_spec.Config(input_spec, None, None)

    # WHEN generating a spec file for the API docs
    output_spec = gen_supported_spec.get_spec(config)

    # THEN the resulting spec file shouldn't contain any endpoints.
    assert len(output_spec['paths']) == 0


def test_one_supported_endpoint_by_tag(datadir):
    """An endpoint in the input OpenAPI spec is tagged as supported."""
    # GIVEN a spec file that has a single endpoint that's not tagged as supported
    spec_file = datadir / 'openapi_one_supported_endpoint.json'
    with open(spec_file) as f:
        input_spec = json.load(f)
    config = gen_supported_spec.Config(input_spec, None, None)

    # WHEN generating a spec file for the API docs
    output_spec = gen_supported_spec.get_spec(config)

    # THEN the resulting spec file shouldn't contain any endpoints.
    assert len(output_spec['paths']) == 1


def test_include_unsupported_endpoint(datadir):
    """An endpoint in the input OpenAPI spec isn't tagged as supported, but it's included via config file."""
    # GIVEN a spec file that has a single endpoint that's not tagged as supported
    spec_file = datadir / 'openapi_no_supported_endpoints.json'
    with open(spec_file) as f:
        input_spec = json.load(f)

    ep = gen_supported_spec.Endpoint('/api/v1/agentless/scan', 'post')

    config = gen_supported_spec.Config(input_spec, [ep], None)

    # WHEN generating a spec file for the API docs
    output_spec = gen_supported_spec.get_spec(config)

    # THEN the resulting spec file shouldn't contain any endpoints.
    print(output_spec['paths'])
    assert len(output_spec['paths']) == 1


def test_include_unsupported_endpoint2(shared_datadir):
    """An endpoint in the input OpenAPI spec isn't tagged as supported, but it's included via config file."""
    # GIVEN a spec file that has a single endpoint that's not tagged as supported
    spec_file = shared_datadir / 'openapi_no_supported_endpoints.json'
    config_file = shared_datadir / 'supported.cfg'

    # WHEN generating a spec file for the API docs
    output_spec = gen_supported_spec.gen_spec(spec_file, config_file)

    # THEN the resulting spec file shouldn't contain any endpoints.
    #print(output_spec['paths'])
    assert len(output_spec['paths']) == 1


def test_exclude_supported_endpoint(datadir):
    """An endpoint in the input OpenAPI spec is tagged as supported, but it's excluded via config file."""
    # GIVEN a spec file that has a single endpoint that's not tagged as supported
    spec_file = datadir / 'openapi_one_supported_endpoint.json'
    with open(spec_file) as f:
        input_spec = json.load(f)

    ep = gen_supported_spec.Endpoint('gen_supported_spec', 'post')

    config = gen_supported_spec.Config(input_spec, None, [ep])

    # WHEN generating a spec file for the API docs
    output_spec = gen_supported_spec.get_spec(config)

    # THEN the resulting spec file shouldn't contain any endpoints.
    assert len(output_spec['paths']) == 0

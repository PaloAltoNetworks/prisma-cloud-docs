import pytest
import gen_supported_spec


# Config file contents
CFG_FILE_BLANK_LINE="\n"
CFG_FILE_COMMENT="# Comment"
CFG_FILE_INCLUSION="+/api/v1/registry/webhook/webhook,delete"
CFG_FILE_EXCLUSION="-/api/v*/cloud/discovery/progress,get"
CFG_FILE_INVALID_INCLUSION_UNKOWN_METHOD="+/api/v1/registry/webhook/webhook,abc"
CFG_FILE_INVALID_INCLUSION_MISSING_METHOD1="+/api/v1/registry/webhook/webhook"
CFG_FILE_INVALID_INCLUSION_MISSING_METHOD2="+/api/v1/registry/webhook/webhook,"
CFG_FILE_INVALID_INCLUSION_MISSING_PATH="+,abc"
CFG_FILE_INVALID_ENTRY="hello"
CFG_FILE_INCLUSION_SPACES="+ /api/v1/registry/webhook/webhook , get "


def test_no_cfg_file(shared_datadir):
    """Validate that you can run the script without specifying a config file

    The config file is optional.
    """
    # GIVEN the gen_supported_spec.py script is called without a config file
    spec_file = shared_datadir / 'openapi_one_supported_endpoint.json'

    # WHEN when you generate a spec file with supported endpoints
    s = gen_supported_spec.gen_spec(spec_file, None)

    # THEN you should you should get a valid spec dict
    assert len(s['paths']) == 1


def test_empty_cfg_file(tmp_path):
    """Test that an empty file is handled gracefully"""
    # GIVEN a config file with a blank line only
    cfg_file = tmp_path / "supported.cfg"
    cfg_file.touch()

    # WHEN you load and process the file
    inclusions, exclusions = gen_supported_spec.load_config_file(cfg_file)

    # THEN there are no inclusions or exclusions
    assert len(inclusions) == len(exclusions) == 0


@pytest.mark.parametrize("cfg_file_content",
    [
        CFG_FILE_BLANK_LINE, CFG_FILE_COMMENT, CFG_FILE_INVALID_INCLUSION_UNKOWN_METHOD,
        CFG_FILE_INVALID_INCLUSION_MISSING_METHOD1, CFG_FILE_INVALID_INCLUSION_MISSING_METHOD2,
        CFG_FILE_INVALID_INCLUSION_MISSING_PATH, CFG_FILE_INVALID_ENTRY
    ]
)
def test_non_directives(tmp_path, cfg_file_content):
    """Test that blank lines, comments, and invalid entries are ignored"""
    # GIVEN a config file with a blank line only
    cfg_file = tmp_path / "supported.cfg"
    cfg_file.write_text(cfg_file_content)

    # WHEN you load and process the file
    inclusions, exclusions = gen_supported_spec.load_config_file(cfg_file)

    # THEN there should be no inclusions or exclusions
    assert len(inclusions) == len(exclusions) == 0


@pytest.mark.parametrize("cfg_file_content",
    [CFG_FILE_INCLUSION, CFG_FILE_INCLUSION_SPACES]
)
def test_inclusion(tmp_path, cfg_file_content):
    """Test that inclusions are identified"""
    # GIVEN a config file with a blank line only
    cfg_file = tmp_path / "supported.cfg"
    cfg_file.write_text(cfg_file_content)

    # WHEN you load and process the file
    inclusions, exclusions = gen_supported_spec.load_config_file(cfg_file)

    # THEN there should be no inclusions or exclusions
    assert len(inclusions) == 1 and len(exclusions) == 0


def test_exclusion(tmp_path):
    """Test that exclusions are identified"""
    # GIVEN a config file with a blank line only
    cfg_file = tmp_path / "supported.cfg"
    cfg_file.write_text(CFG_FILE_EXCLUSION)

    # WHEN you load and process the file
    inclusions, exclusions = gen_supported_spec.load_config_file(cfg_file)

    # THEN there should be no inclusions or exclusions
    assert len(inclusions) == 0 and len(exclusions) == 1

import pytest
from python_enabler.tools.url_matcher import is_valid_git_url


def test_git_url_matcher():
    assert is_valid_git_url("https://github.com/inflamously/stable-cheese") == True 
    assert is_valid_git_url("git@github.com:inflamously/stable-cheese.git") == True
    with pytest.raises(Exception):
        assert is_valid_git_url("")

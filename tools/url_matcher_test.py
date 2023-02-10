from re import Match
from typing import Union
from cli.tools.url_matcher import git_url_matcher


def test_git_url_matcher():
    assert git_url_matcher("git@github.com:inflamously/stable-cheese.git") is not None
    assert git_url_matcher("") is None
    match: Union[Match[str], None] =  git_url_matcher("git@")
    assert match is not None
    assert match.group(1) == 'git'
    assert match.group(2) == '@'
    match = git_url_matcher("git@github.com:inflamously/stable-cheese.git")
    assert match is not None
    assert match.group(1) == 'git'
    assert match.group(2) == '@github.com:inflamously/stable-cheese.git'
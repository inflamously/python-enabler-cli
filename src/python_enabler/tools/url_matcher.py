from re import Match, match
from typing import Union
import validators

def get_git_url(value):
    return match(r"(.*)(@.*)", value)

@validators.validator
def is_git_url(value):
    return not get_git_url(value) == None


def is_valid_git_url(url):
    return is_git_url(url) or validators.url(url)


def git_url_extract(url: str) -> Union[str, None]:
    if url is None:
        return None
    
    url_match: Union[Match[str], None] = is_valid_git_url(url)
    if url_match is None:
        return None
    else:
        return url_match.group(2)

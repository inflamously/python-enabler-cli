from re import Match, match
from typing import Union


def git_url_matcher(url: str) -> Union[Match[str], None]:
    return match(r"(.*)(@.*)", url)


def git_url_extract(url: str) -> Union[str, None]:
    if url is None:
        return None
    
    url_match: Union[Match[str], None] = git_url_matcher(url)
    if url_match is None:
        return None
    else:
        return url_match.group(2)

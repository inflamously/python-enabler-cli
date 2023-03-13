import os
from re import Match
from typing import Union
from python_enabler.errors.exceptions.peprojectexception import PEProjectExceptionURLMismatch
from typer import Typer
from .pecommanddict import PECommandDict
from ..tools.url_matcher import is_valid_git_url


project: Typer = Typer()


@project.command()
def install(repo_url: str, project_path: str, personal_access_token: str) -> None:
    if not os.path.exists(project_path):
        os.makedirs(project_path, exist_ok=True)

    if is_valid_git_url(repo_url):
        ...
    else:
        raise PEProjectExceptionURLMismatch()
    

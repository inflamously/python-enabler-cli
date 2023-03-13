import os
from re import Match
from typing import Union
from typer import Typer
from .pecommanddict import PECommandDict
from ..tools.url_matcher import git_url_matcher


project: Typer = Typer()


@project.command()
def install(repo_url: str, project_path: str, personal_access_token: str) -> None:
    if not os.path.exists(project_path):
        os.makedirs(project_path, exist_ok=True)

    repository: Union[Match[str], None] = git_url_matcher(repo_url)

    if repository:
        PECommandDict().new_command(
            ["git", "clone", f"{personal_access_token}{repository}"],
            desc="Cloning git repository",
        ).execute()

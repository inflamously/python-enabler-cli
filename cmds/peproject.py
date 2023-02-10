import os
from re import Match
from typing import Union
from typer import Typer
from cli.tools.pecommand import PECommand, PECommandDict
from cli.tools.url_matcher import git_url_matcher


project: Typer = Typer()


@project.command()
def install(repo_url: str, project_path: str, personal_access_token: str):
    if not os.path.exists(project_path):
        os.makedirs(project_path, exist_ok=True)

    repository: Union[Match[str], None] = git_url_matcher(repo_url)

    if repository is None:
        return

    PECommandDict(
        PECommand(
            ["git", "clone", "{}{}".format(personal_access_token, repository)],
            desc="Cloning git repository",
        )
    ).execute()
    # Input: py .\main.py project install <git-repo> <path>
    # Allow Scripting (Automation)
    # Checkout git repository at given path
    # If path does not exist create

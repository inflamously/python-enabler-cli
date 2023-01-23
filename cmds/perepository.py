from typer import Typer
from tools.peprinter import pe_print_error
from tools.pecommand import PECommand
from tools.pecommand import PECommandDict
import os
import shutil


repository = Typer()


@repository.command()
def download(project_path: str, url: str, force_create: bool = False):
    os.chdir(project_path)
    if force_create: shutil.rmtree(".git")
    if not os.path.exists(".git"):
        PECommandDict(
            PECommand(["git", "init"], desc="initialize repository"),
            PECommand(["git", "remote", "add", "origin", url], desc="add remote url"),
            PECommand(["git", "pull", url], desc="pull remote repository")
        ).execute()
    else:
        pe_print_error("Git repository already initialized", "Path already exists")
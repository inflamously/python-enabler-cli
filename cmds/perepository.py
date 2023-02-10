from typer import Typer
from cmds.pesimpleerror import PE_ERROR_FILENOTFOUND
from tools.pecommand import PECommand
from tools.pecommand import PECommandDict
import os
import shutil


repository = Typer()


@repository.command()
def download(project_path: str, url: str, force_create: bool = False):
    if not os.path.exists(project_path):
        PE_ERROR_FILENOTFOUND(data=project_path).exception("Project path invalid")
    os.chdir(project_path)
    if force_create and os.path.exists(".git"):
        shutil.rmtree(".git")
    if not os.path.exists(".git"):
        PECommandDict(
            PECommand(["git", "init"], desc="initialize repository"),
            PECommand(["git", "remote", "add", "origin", url], desc="add remote url"),
            PECommand(["git", "pull", url], desc="pull remote repository"),
        ).execute()
    else:
        ...
        # TODO: Enable error
        # pe_print_error("Git repository already initialized", "Path already exists")

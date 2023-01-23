from subprocess import PIPE, Popen
from sys import platform
from typing import List
from tools.peprinter import pe_print_command
from cmds.pesimpleerror import PE_ERROR_FILENOTFOUND, PE_ERROR_PLATFORM, PE_SUCCESS, PE_ERROR_COMMAND
from cmds.pesimpleerror import PECodeMessage

DEBUG = True


def __sanitize(line: str) -> str:
    return line


"""
Starts running OS commands line by line from given command with params.
Also reports errors correctly.
"""
def runner(command: List[str], desc: str = "#", stdin: str = "", sanitize=True) -> PECodeMessage:
    try:
        if platform == "win32" or platform == "cygwin":
            process = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE, universal_newlines=True)
            output, error = process.communicate("YahVulgtagn15$")
            if error and len(error) > 0:
                return PE_ERROR_COMMAND(message=error)
            else:
                pe_print_command(desc, output)
            return PE_SUCCESS
        else:
            return PE_ERROR_PLATFORM
    except FileNotFoundError as FileNotFoundErrorData:
        return PE_ERROR_FILENOTFOUND.assign_data(FileNotFoundErrorData.errno)
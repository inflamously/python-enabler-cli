from subprocess import PIPE, CompletedProcess, Popen, run
from sys import platform
from typing import List, Union
from ..errors.pesimpleerror import PE_ERROR_COMMAND, PE_ERROR_FILENOTFOUND, PE_ERROR_PLATFORM, PE_SUCCESS, PECodeMessage
from ..tools.peprinter import pe_print_command


DEBUG = True


def __sanitize(line: str) -> str:
    return line


"""
Starts running OS commands line by line from given command with params.
Also reports errors correctly.
"""


def runner(
    command: str, desc: str = "#", sanitize=True, env=None, shell=False
) -> PECodeMessage:
    try:
        if platform == "win32" or platform == "cygwin":
            process: Union[Popen[str], None] = None
            if shell:
                # TODO: Implement custom shell selection.
                output = run(
                    ["cmd", "-c", command],
                    stdout=PIPE,
                    stderr=PIPE,
                    stdin=PIPE,
                    universal_newlines=True,
                    env=env,
                )
                pe_print_command(desc, output.stdout)
            else:
                process = Popen(
                    command,
                    stdout=PIPE,
                    stderr=PIPE,
                    stdin=PIPE,
                    universal_newlines=True,
                    env=env,
                )

            if not process:
                return PE_ERROR_COMMAND

            while process.poll() is None:
                output, error, input = process.stdin, process.stderr, process.stdin
                if error:
                    return PE_ERROR_COMMAND(message="\n".join(error.readlines()))
                if output:
                    pe_print_command(desc, output.readline())
            return PE_SUCCESS
        else:
            return PE_ERROR_PLATFORM
    # TODO: Better error output
    except FileNotFoundError as FileNotFoundErrorData:
        return PE_ERROR_FILENOTFOUND(data=FileNotFoundErrorData.errno)

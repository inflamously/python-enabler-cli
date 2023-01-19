from subprocess import PIPE, Popen
from sys import platform
from typing import List, Union
from cmds.pesimpleerror import PECodeMessage

DEBUG = True
PE_ERROR_CODE = 0xCE0000


PE_SUCCESS = PECodeMessage(PE_ERROR_CODE + 1, "Success")


PE_ERROR_GENERIC = PECodeMessage(PE_ERROR_CODE + 2, "Error occured")
PE_ERROR_PLATFORM = PECodeMessage(PE_ERROR_CODE + 3, "Platform not found")
PE_ERROR_FILENOTFOUND = PECodeMessage(message="File not found")


def runner(command: List[str], desc: str = "#") -> PECodeMessage:
    try:
        if platform == "win32" or platform == "cygwin":
            process = Popen(command, stdout=PIPE, stderr=PIPE)
            status: Union[int, None] = None
            while status is None:
                status = process.poll()
                if process.stdout:
                    line = process.stdout.readline().decode().strip()
                    if line == "": continue # TODO: Should we really ignore empty lines?
                    print('> ["{}"]:'.format(desc), line)
            return PE_SUCCESS
        else:
            return PE_ERROR_PLATFORM
    except FileNotFoundError as FileNotFoundErrorData:
        return PE_ERROR_FILENOTFOUND(FileNotFoundErrorData.errno)
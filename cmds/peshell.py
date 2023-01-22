from subprocess import PIPE, Popen
from sys import platform
from typing import List, Union
from cmds.pesimpleerror import PE_ERROR_FILENOTFOUND, PE_ERROR_PLATFORM, PE_SUCCESS
from cmds.pesimpleerror import PECodeMessage


DEBUG = True

"""
Starts running OS commands line by line from given commandlist.
Also reports errors correctly.
"""
def runner(commandlist: List[str], desc: str = "#") -> PECodeMessage:
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
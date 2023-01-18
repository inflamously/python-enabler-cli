from subprocess import PIPE, Popen
from sys import platform
from typing import List, Union

def runner(command: List[str], desc: str = "#"):
    if platform == "win32" or platform == "cygwin":
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        status: Union[int, None] = None
        while status is None:
            status = process.poll()
            if process.stdout:
                line = process.stdout.readline().decode().strip()
                if line == "": continue # TODO: Should we really ignore empty lines?
                print('> "{}":'.format(desc), line)
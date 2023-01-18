
from typer import Typer
from cmds.peshell import runner
from tools.pecommand import PECommandDict, pecommand

projects: Typer = Typer()

@projects.command()
@pecommand()
def load():
    return PECommandDict(
        {
            "get git version": ["git", "version"]
        }
    )
    
    
@projects.command()
@pecommand()
def create_file():
    return PECommandDict(
        {
            "create file": ["touch test.txt"]
        }
    )
    
        
@projects.command()
def test():
    runner(['cmd', '/c', 'echo', 'Hello World!'])
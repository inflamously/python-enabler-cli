
from typer import Typer
from cmds.peshell import runner
from tools.pecommand import PECommandDict, pecommand

projects: Typer = Typer()

@projects.command()
@pecommand(
    PECommandDict(
        {
            "retrieve git version": ["x", "version"]
        }
    )
)
def load():
    ...
    
    
@projects.command()
@pecommand(
    PECommandDict(
        {
            "create file": ["touch test.txt"]
        }
    )
)
def create_file():
    ...
    
        
@projects.command()
def test():
    runner(['cmd', '/c', 'echo', 'Hello World!'])
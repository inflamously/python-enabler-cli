from os import path
import sys
# TODO: Temporarily added ... until packaging properly learned...
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
print(path.dirname(path.abspath(__file__)))
print(sys.path)

from typer import Typer
from cli.cmds.peproject import project


app: Typer = Typer()
app.add_typer(project, name="project")


@app.command()
def version() -> None:
    print("0.1")


if __name__ == "__main__":

    app()
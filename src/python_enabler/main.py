from typer import Typer
from .cmds.peproject import project

app: Typer = Typer()
app.add_typer(project, name="project")

@app.command()
def version() -> None:
    print("0.1")

import typer
from cmds.peproject import projects


app = typer.Typer()
app.add_typer(projects, name="projects")


@app.command()
def version():
    print("0.0+0000")


if __name__ == "__main__":
    app()
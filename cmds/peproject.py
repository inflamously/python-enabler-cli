
from typer import Typer 
from cmds.perepository import repository


projects: Typer = Typer()
projects.add_typer(repository, name="repository")


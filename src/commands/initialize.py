from core.repository import Repository
import click

@click.command()
def inicializar():
    repository = Repository()
    repository.initialize()
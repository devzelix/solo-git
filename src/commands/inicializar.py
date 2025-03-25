from core.repositorio import Repositorio
import click

@click.command()
def inicializar():
    repo = Repositorio()
    repo.inicializar()
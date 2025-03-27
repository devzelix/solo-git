from commands.configure import configurar
from commands.initialize import inicializar
import click

@click.group()
def commands():
    pass

commands.add_command(inicializar)
commands.add_command(configurar)

if __name__ == "__main__":
    commands()
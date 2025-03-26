from commands.initialize import inicializar
import click

@click.group()
def commands():
    pass

commands.add_command(inicializar)

if __name__ == "__main__":
    commands()
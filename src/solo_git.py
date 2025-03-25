from commands.inicializar import inicializar
import click

@click.group()
def comandos():
    pass

comandos.add_command(inicializar)

if __name__ == "__main__":
    comandos()
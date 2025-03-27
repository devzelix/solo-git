from colorama import Fore
from core.repository import Repository
from io import StringIO
from pathlib import Path
import click
import configparser
import re

def get_global_configuration_path():
    global_configuration_path = Path.home() / ".sologitconfiguracion"
    global_configuration_path.touch(exist_ok=True)
    return global_configuration_path

def get_local_configuration_path():
    repository = Repository()
    if repository.configuration_path.exists():
        if repository.repository_path.exists():
            repository.configuration_path.touch()
            return repository.configuration_path
        else:
            print(Fore.RED + f"\nNo se encontro el directorio del repositorio solo-git.\n")
            return None
    else:
        return repository.configuration_path

def configure(path, key, value):
    if path:
        section, option = key.split(".")
        config = configparser.ConfigParser()
        config.read(path)
        if not config.has_section(section):
            config.add_section(section)
        config.set(section, option, value)
        output = StringIO()
        config.write(output)
        formatted_string = ""
        for line in output.getvalue().splitlines():
            if line.startswith("["):
                formatted_string += f"{line}\n"
            else:
                formatted_string += f"    {line}\n"
        path.write_text(formatted_string.strip())

@click.command()
@click.option("--global", "is_global", is_flag=True)
@click.argument("key")
@click.argument("value")
def configurar(is_global, key, value):
    key_pattern = re.compile(r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$")
    if key_pattern.match(key):
        if value != "":
            if is_global:
                configure(get_global_configuration_path(), key, value)
            else:
                configure(get_local_configuration_path(), key, value)
    else:
        print(Fore.RED + "\nLa clave debe estar en el formato 'campo.clave' (ejemplo: user.name, core.editor).\n")
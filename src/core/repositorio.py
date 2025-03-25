from colorama import Fore
from pathlib import Path

class Repositorio:
    def __init__(self):
        self.ruta_repositorio = Path(".") / ".solo-git/"

    def inicializar(self):
        if self.ruta_repositorio.exists():
            print(Fore.YELLOW + f"\nRepositorio solo-git ya inicializado en: {self.ruta_repositorio.resolve()}\n")
        else:
            self.ruta_repositorio.mkdir(parents=True)
            print(Fore.GREEN + f"\nRepositorio solo-git vacío inicializado en: {self.ruta_repositorio.resolve()}\n")
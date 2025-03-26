from colorama import Fore
from pathlib import Path

class Repository:
    def __init__(self):
        self.repository_path = Path(".") / ".solo-git/"
        self.objects_path = self.repository_path / "objetos/"
        self.references_path = self.repository_path / "referencias/"
        self.heads_path = self.references_path / "cabezas/"
        self.logs_path = self.repository_path / "registros/"
        self.head_path = self.repository_path / "CABEZA"
        self.configuration_path = self.repository_path / "configuracion"

    def initialize(self):
        try:
            if self.repository_path.exists():
                print(Fore.YELLOW + f"\nRepositorio solo-git ya inicializado en: {self.repository_path.resolve()}\n")
            else:
                self.repository_path.mkdir()
                self.objects_path.mkdir()
                self.references_path.mkdir()
                self.heads_path.mkdir()
                self.logs_path.mkdir()
                self.head_path.write_text(f"referencia: {self.heads_path}/main")
                self.configuration_path.write_text("")
                print(Fore.GREEN + f"\nRepositorio solo-git vacío inicializado en: {self.repository_path.resolve()}\n")
        except Exception as e:
            print(Fore.RED + f"\nHubo un error al incializar el repositorio: {e}\n")
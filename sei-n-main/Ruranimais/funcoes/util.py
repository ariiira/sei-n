from rich import print as rprint
from rich.console import Console
console = Console()
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Imports
import time
import platform
import subprocess
from pathlib import Path

class Util:

    # Mostra logo da ruranimais
    @staticmethod
    def mostrar_logo(caminho_logo=None):
        arquivo_logo = (
            Path(caminho_logo)
            if caminho_logo is not None
            else Path(__file__).with_name("ruranimaislogo.txt")
        )
        with arquivo_logo.open("r", encoding="utf-8") as f:
            logo= f.read()
        rprint(logo)
        time.sleep(4)
        Util.limpar_terminal()


    # Identificação de Sistema + Limpeza Inicial do Terminal
    @staticmethod
    def limpar_terminal():
        if platform.system() in ("Linux", "Darwin"):
            subprocess.run("clear", shell=True, check=False)
        elif platform.system() == "Windows":
            subprocess.run("cls", shell=True, check=False)


# Cores Utilizadas Frequentemente
amarelo = "#EEA103"
vermelho = "#D74013"
azul = "#2B283B"
verde = "#719029"
bege = "#F8E8CF"

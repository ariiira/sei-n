from rich import print as rprint
from rich.console import Console
console = Console()
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
from smtplib import SMTPException
from datetime import datetime, timedelta
from smtplib import SMTPException

# Imports
import time
import os
import re
import requests
import platform
from pathlib import Path


# Mostra logo da ruranimais
def mostrar_logo(caminho_logo=None):
    arquivo_logo = (
        Path(caminho_logo)
        if caminho_logo is not None
        else Path(__file__).with_name("ruranimaislogo.txt")
    )
    with arquivo_logo.open("r", encoding="utf-8") as f:
        logo= f.read()
    print(logo)
    time.sleep(4)
    limpar_terminal()


# Identificação de Sistema + Limpeza Inicial do Terminal
def limpar_terminal():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        comando_de_limpeza = "clear"
    if platform.system() == "Windows":
        comando_de_limpeza = "cls"
    os.system(comando_de_limpeza)


# Cores Utilizadas Frequentemente
amarelo = "#EEA103"
vermelho = "#D74013"
azul = "#2B283B"
verde = "#719029"
bege = "#F8E8CF"

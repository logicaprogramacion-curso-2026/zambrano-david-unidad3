"""
Punto de entrada del Sistema de Evaluaciones de Respuesta Cerrada.
Ejecutar con: python main.py
"""
import os

from capa3_cli.cli import Simulador


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_DATOS = os.path.join(BASE_DIR, "data")
CARPETA_BANCOS = os.path.join(BASE_DIR, "bancos")

if __name__ == "__main__":
    simulador = Simulador(carpeta_datos=CARPETA_DATOS, carpeta_bancos=CARPETA_BANCOS)
    simulador.iniciar()

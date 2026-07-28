"""
Módulo: gestor.py
Implementa GestorPreguntas: lógica de negocio para cargar preguntas
desde archivos (TXT, CSV, JSON) y convertirlas en objetos Pregunta.
"""
import csv
import json
from src.entidad import Pregunta

SEPARADOR = "-" * 40

CAMPOS_OBLIGATORIOS = ["pregunta", "opcion_a", "opcion_b", "opcion_c",
                        "opcion_d", "respuesta_correcta", "dificultad", "tema"]
RESPUESTAS_VALIDAS = ("A", "B", "C", "D")
DIFICULTADES_VALIDAS = ("Fácil", "Media", "Difícil")


class GestorPreguntas:
    """Carga preguntas desde archivos y las convierte en objetos Pregunta."""

    def __init__(self, dao=None):
        self.dao = dao  # se usará a partir de la Iteración 5

    @staticmethod
    def _validar_datos(datos, origen=""):
        """Valida campos obligatorios y el dominio de respuesta/dificultad."""
        faltantes = [c for c in CAMPOS_OBLIGATORIOS if not str(datos.get(c, "")).strip()]
        if faltantes:
            raise ValueError(f"{origen}: faltan campos obligatorios {faltantes}")

        respuesta = str(datos["respuesta_correcta"]).strip().upper()
        if respuesta not in RESPUESTAS_VALIDAS:
            raise ValueError(
                f"{origen}: respuesta_correcta inválida '{respuesta}' (debe ser A, B, C o D)"
            )

        dificultad = str(datos["dificultad"]).strip()
        if dificultad not in DIFICULTADES_VALIDAS:
            raise ValueError(
                f"{origen}: dificultad inválida '{dificultad}' (debe ser Fácil, Media o Difícil)"
            )

    @staticmethod
    def _construir_pregunta(datos):
        return Pregunta(
            pregunta=datos["pregunta"],
            opcion_a=datos["opcion_a"], opcion_b=datos["opcion_b"],
            opcion_c=datos["opcion_c"], opcion_d=datos["opcion_d"],
            respuesta_correcta=datos["respuesta_correcta"],
            dificultad=datos["dificultad"], tema=datos["tema"],
        )

    # ---------- TXT ----------
    def cargar_desde_txt(self, ruta):
        preguntas = []
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        bloques = [b.strip() for b in contenido.split(SEPARADOR) if b.strip()]
        for bloque in bloques:
            datos = {}
            for linea in bloque.splitlines():
                if ":" not in linea:
                    continue
                clave, _, valor = linea.partition(":")
                datos[clave.strip().lower()] = valor.strip()

            self._validar_datos(datos, origen=f"TXT ({ruta})")
            preguntas.append(self._construir_pregunta(datos))
        return preguntas

    # ---------- CSV ----------
    def cargar_desde_csv(self, ruta):
        preguntas = []
        with open(ruta, "r", encoding="utf-8", newline="") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                self._validar_datos(fila, origen=f"CSV ({ruta})")
                preguntas.append(self._construir_pregunta(fila))
        return preguntas

    # ---------- JSON ----------
    def cargar_desde_json(self, ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            datos_json = json.load(f)

        preguntas = []
        for item in datos_json:
            self._validar_datos(item, origen=f"JSON ({ruta})")
            preguntas.append(self._construir_pregunta(item))
        return preguntas
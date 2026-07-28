"""
Módulo: gestor.py
Implementa GestorPreguntas: lógica de negocio para cargar preguntas
desde archivos (TXT, CSV, JSON) y convertirlas en objetos Pregunta.
"""
import csv
import json
from src.entidad import Pregunta
from collections import Counter

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

        with open(ruta, "r", encoding="cp1252") as f:
            lineas = [linea.strip() for linea in f if linea.strip()]

        i = 0
        while i < len(lineas):
            if lineas[i].startswith("PREGUNTA #"):
                datos = {}

                i += 1
                while i < len(lineas) and not lineas[i].startswith("PREGUNTA #"):
                    linea = lineas[i].strip()

                    if linea.startswith("Tema:"):
                        datos["tema"] = linea.split(":", 1)[1].strip()

                    elif linea.startswith("Dificultad:"):
                        datos["dificultad"] = linea.split(":", 1)[1].strip()

                    elif linea.startswith("Enunciado:"):
                        datos["pregunta"] = linea.split(":", 1)[1].strip()

                    elif linea.startswith("A)"):
                        datos["opcion_a"] = linea[2:].strip()

                    elif linea.startswith("B)"):
                        datos["opcion_b"] = linea[2:].strip()

                    elif linea.startswith("C)"):
                        datos["opcion_c"] = linea[2:].strip()

                    elif linea.startswith("D)"):
                        datos["opcion_d"] = linea[2:].strip()

                    elif "correcta" in linea.lower():
                        if ":" in linea:
                            valor = linea.split(":", 1)[1].strip().upper()
                            if valor in ("A", "B", "C", "D"):
                                datos["respuesta_correcta"] = valor

                    i += 1

                print("DATOS EXTRAIDOS:", datos)  # temporal para depurar

                self._validar_datos(datos, origen=f"TXT ({ruta})")
                preguntas.append(self._construir_pregunta(datos))
            else:
                i += 1

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
    # ---------- BASE DE DATOS ----------
    def guardar_en_base_datos(self, preguntas):
        if self.dao is None:
            raise ValueError("No se ha configurado un DAO para guardar en la base de datos.")

        contador = 0
        for pregunta in preguntas:
            self.dao.insertar(pregunta)
            contador += 1
        print(f"Se guardaron {contador} preguntas en la base de datos.")


    # ---------- EXPORTACIÓN ----------
    def exportar_a_txt(self, ruta="preguntas_exportadas.txt"):
        preguntas = self.dao.obtener_todas()
        with open(ruta, "w", encoding="utf-8") as f:
            for p in preguntas:
                f.write(f"pregunta: {p.pregunta}\n")
                f.write(f"opcion_a: {p.opcion_a}\n")
                f.write(f"opcion_b: {p.opcion_b}\n")
                f.write(f"opcion_c: {p.opcion_c}\n")
                f.write(f"opcion_d: {p.opcion_d}\n")
                f.write(f"respuesta_correcta: {p.respuesta_correcta}\n")
                f.write(f"dificultad: {p.dificultad}\n")
                f.write(f"tema: {p.tema}\n")
                f.write(SEPARADOR + "\n")
        print(f"Exportación a TXT completada: {ruta}")


    def exportar_a_csv(self, ruta="preguntas_exportadas.csv"):
        preguntas = self.dao.obtener_todas()
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS_OBLIGATORIOS)
            writer.writeheader()
            for p in preguntas:
                writer.writerow({
                    "pregunta": p.pregunta, "opcion_a": p.opcion_a,
                    "opcion_b": p.opcion_b, "opcion_c": p.opcion_c,
                    "opcion_d": p.opcion_d, "respuesta_correcta": p.respuesta_correcta,
                    "dificultad": p.dificultad, "tema": p.tema,
                })
        print(f"Exportación a CSV completada: {ruta}")


    def exportar_a_json(self, ruta="preguntas_exportadas.json"):
        preguntas = self.dao.obtener_todas()
        datos = [{
            "pregunta": p.pregunta, "opcion_a": p.opcion_a,
            "opcion_b": p.opcion_b, "opcion_c": p.opcion_c,
            "opcion_d": p.opcion_d, "respuesta_correcta": p.respuesta_correcta,
            "dificultad": p.dificultad, "tema": p.tema,
        } for p in preguntas]
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
        print(f"Exportación a JSON completada: {ruta}")


    # ---------- ESTADÍSTICAS ----------
    def estadisticas_por_tema(self):
        preguntas = self.dao.obtener_todas()
        conteo = Counter(p.tema for p in preguntas)
        for tema, cantidad in conteo.items():
            print(f"Tema: {tema} -> {cantidad} preguntas")
        return dict(conteo)


    def estadisticas_por_dificultad(self):
        preguntas = self.dao.obtener_todas()
        conteo = Counter(p.dificultad for p in preguntas)
        for dificultad, cantidad in conteo.items():
            print(f"Dificultad: {dificultad} -> {cantidad} preguntas")
        return dict(conteo)
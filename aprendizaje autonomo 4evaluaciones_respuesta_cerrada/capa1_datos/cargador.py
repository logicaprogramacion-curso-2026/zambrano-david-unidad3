"""
Capa 1 - Datos
Responsable de cargar y validar los archivos de examen y de banco de preguntas (JSON).
"""
import json
import os


TIPOS_VALIDOS = {"opcion_multiple", "verdadero_falso", "emparejamiento", "completar_espacios"}


class CargadorDatos:
    """Carga exámenes y bancos de preguntas desde archivos JSON en sus respectivas carpetas."""

    def __init__(self, carpeta_datos="data", carpeta_bancos="bancos"):
        self.carpeta_datos = carpeta_datos
        self.carpeta_bancos = carpeta_bancos

    # -- Exámenes listos para rendir (carpeta 'data') -----------------------
    def listar_examenes(self):
        """Devuelve la lista de archivos .json disponibles en la carpeta de exámenes."""
        return self._listar_json(self.carpeta_datos)

    def cargar_examen(self, nombre_archivo):
        """Carga y valida un examen a partir de su nombre de archivo."""
        return self._cargar_json(self.carpeta_datos, nombre_archivo)

    # -- Bancos de preguntas para generación aleatoria (carpeta 'bancos') ---
    def listar_bancos(self):
        """Devuelve la lista de archivos .json disponibles en la carpeta de bancos."""
        return self._listar_json(self.carpeta_bancos)

    def cargar_banco(self, nombre_archivo):
        """Carga y valida un banco de preguntas a partir de su nombre de archivo."""
        return self._cargar_json(self.carpeta_bancos, nombre_archivo)

    # -- Utilidades internas --------------------------------------------------
    def _listar_json(self, carpeta):
        if not os.path.isdir(carpeta):
            return []
        return sorted(
            archivo for archivo in os.listdir(carpeta)
            if archivo.endswith(".json")
        )

    def _cargar_json(self, carpeta, nombre_archivo):
        ruta = os.path.join(carpeta, nombre_archivo)
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        self._validar_preguntas(datos)
        return datos

    def _validar_preguntas(self, datos):
        """Valida la lista de 'preguntas' de un examen o de un banco de preguntas."""
        if "preguntas" not in datos or not isinstance(datos["preguntas"], list):
            raise ValueError("El archivo no contiene una lista 'preguntas' válida.")
        if len(datos["preguntas"]) == 0:
            raise ValueError("El archivo no contiene preguntas.")

        for i, pregunta in enumerate(datos["preguntas"], start=1):
            tipo = pregunta.get("tipo")
            if tipo not in TIPOS_VALIDOS:
                raise ValueError(f"La pregunta {i} tiene un tipo inválido o ausente.")
            if "enunciado" not in pregunta:
                raise ValueError(f"La pregunta {i} no tiene enunciado.")
            if "puntaje" not in pregunta:
                pregunta["puntaje"] = 1  # puntaje por defecto si no se especifica

            if tipo == "opcion_multiple" and "opciones" not in pregunta:
                raise ValueError(f"La pregunta {i} (opción múltiple) no tiene 'opciones'.")
            if tipo == "emparejamiento" and "pares" not in pregunta:
                raise ValueError(f"La pregunta {i} (emparejamiento) no tiene 'pares'.")
            if tipo in ("opcion_multiple", "verdadero_falso", "completar_espacios") \
                    and "respuesta_correcta" not in pregunta:
                raise ValueError(f"La pregunta {i} no tiene 'respuesta_correcta'.")

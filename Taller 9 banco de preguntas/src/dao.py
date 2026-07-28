"""
Módulo: dao.py
Implementa PreguntaDAO: acceso a datos (CRUD) para la entidad Pregunta
usando SQLite como motor de almacenamiento persistente.
"""
import sqlite3
from src.entidad import Pregunta


class PreguntaDAO:
    """Encapsula todo el acceso a la tabla 'preguntas' en SQLite."""

    def __init__(self, ruta_bd="banco_preguntas.db"):
        self.ruta_bd = ruta_bd
        self.crear_tabla()

    def _conectar(self):
        """Abre una nueva conexión a la base de datos."""
        conexion = sqlite3.connect(self.ruta_bd)
        conexion.row_factory = sqlite3.Row  # permite leer columnas por nombre
        return conexion

    def crear_tabla(self):
        """Crea la tabla 'preguntas' si todavía no existe."""
        conexion = self._conectar()
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS preguntas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pregunta TEXT NOT NULL,
                opcion_a TEXT NOT NULL,
                opcion_b TEXT NOT NULL,
                opcion_c TEXT NOT NULL,
                opcion_d TEXT NOT NULL,
                respuesta_correcta TEXT NOT NULL CHECK (respuesta_correcta IN ('A','B','C','D')),
                dificultad TEXT NOT NULL CHECK (dificultad IN ('Fácil','Media','Difícil')),
                tema TEXT NOT NULL
            )
        """)
        conexion.commit()
        conexion.close()

    def insertar(self, pregunta: Pregunta) -> int:
        """Inserta una Pregunta y le asigna el id generado por la BD."""
        conexion = self._conectar()
        cursor = conexion.execute("""
            INSERT INTO preguntas
            (pregunta, opcion_a, opcion_b, opcion_c, opcion_d,
             respuesta_correcta, dificultad, tema)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            pregunta.pregunta, pregunta.opcion_a, pregunta.opcion_b,
            pregunta.opcion_c, pregunta.opcion_d,
            pregunta.respuesta_correcta, pregunta.dificultad, pregunta.tema
        ))
        conexion.commit()
        pregunta.id = cursor.lastrowid
        conexion.close()
        return pregunta.id

    def _fila_a_pregunta(self, fila) -> Pregunta:
        """Convierte una fila de SQLite en un objeto Pregunta."""
        return Pregunta(
            id=fila["id"], pregunta=fila["pregunta"],
            opcion_a=fila["opcion_a"], opcion_b=fila["opcion_b"],
            opcion_c=fila["opcion_c"], opcion_d=fila["opcion_d"],
            respuesta_correcta=fila["respuesta_correcta"],
            dificultad=fila["dificultad"], tema=fila["tema"]
        )

    def obtener_todas(self):
        """Devuelve una lista con todas las preguntas de la BD."""
        conexion = self._conectar()
        filas = conexion.execute("SELECT * FROM preguntas ORDER BY id").fetchall()
        conexion.close()
        return [self._fila_a_pregunta(f) for f in filas]

    def obtener_por_id(self, id):
        """Devuelve una Pregunta por su id, o None si no existe."""
        conexion = self._conectar()
        fila = conexion.execute(
            "SELECT * FROM preguntas WHERE id = ?", (id,)
        ).fetchone()
        conexion.close()
        return self._fila_a_pregunta(fila) if fila else None
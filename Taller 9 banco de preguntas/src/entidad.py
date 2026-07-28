"""
Módulo: entidad.py   lol 
Define la clase Pregunta, que representa una pregunta de selección
múltiple dentro del banco de preguntas.
"""


class Pregunta:
    """Representa una pregunta de opción múltiple con cuatro alternativas."""

    def __init__(self, pregunta, opcion_a, opcion_b, opcion_c, opcion_d,
                 respuesta_correcta, dificultad, tema, id=None):
        self.id = id
        self.pregunta = pregunta
        self.opcion_a = opcion_a
        self.opcion_b = opcion_b
        self.opcion_c = opcion_c
        self.opcion_d = opcion_d
        self.respuesta_correcta = respuesta_correcta.strip().upper()
        self.dificultad = dificultad
        self.tema = tema

    def __str__(self):
        return (
            f"[{self.id}] ({self.tema} - {self.dificultad}) {self.pregunta}\n"
            f"    A) {self.opcion_a}\n"
            f"    B) {self.opcion_b}\n"
            f"    C) {self.opcion_c}\n"
            f"    D) {self.opcion_d}\n"
            f"    Respuesta correcta: {self.respuesta_correcta}"
        )

    def to_dict(self):
        """Convierte la pregunta a un diccionario (útil para CSV/JSON/BD)."""
        return {
            "id": self.id,
            "pregunta": self.pregunta,
            "opcion_a": self.opcion_a,
            "opcion_b": self.opcion_b,
            "opcion_c": self.opcion_c,
            "opcion_d": self.opcion_d,
            "respuesta_correcta": self.respuesta_correcta,
            "dificultad": self.dificultad,
            "tema": self.tema,
        }


if __name__ == "__main__":
    p = Pregunta(
        pregunta="¿Cuál es el resultado de 2 ** 3 en Python?",
        opcion_a="6", opcion_b="8", opcion_c="9", opcion_d="5",
        respuesta_correcta="b", dificultad="Fácil", tema="Operadores", id=1
    )
    print(p)
    print(p.to_dict())
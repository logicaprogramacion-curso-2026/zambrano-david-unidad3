"""
Capa 2 - Lógica (extensión opcional del enunciado)
Generación automática de un examen a partir de un banco de preguntas,
seleccionando preguntas al azar sin repetición (random.sample).
No depende de ningún servicio ni API externa.
"""
import random


class GeneradorExamenes:
    """Arma un examen nuevo seleccionando preguntas al azar de un banco de preguntas."""

    def generar_examen_aleatorio(self, banco, cantidad, titulo=None):
        """
        banco: dict con clave 'preguntas' (lista) y opcionalmente 'nombre_banco'.
        cantidad: número de preguntas a incluir (se ajusta si excede el tamaño del banco).
        Retorna un dict con el mismo formato que un examen normal, listo para rendir.
        """
        preguntas_banco = banco["preguntas"]
        cantidad = max(1, min(cantidad, len(preguntas_banco)))
        seleccionadas = random.sample(preguntas_banco, cantidad)

        if titulo is None:
            nombre_banco = banco.get("nombre_banco", "banco de preguntas")
            titulo = f"Examen generado aleatoriamente ({cantidad} preguntas) - {nombre_banco}"

        return {
            "titulo": titulo,
            "preguntas": seleccionadas,
        }

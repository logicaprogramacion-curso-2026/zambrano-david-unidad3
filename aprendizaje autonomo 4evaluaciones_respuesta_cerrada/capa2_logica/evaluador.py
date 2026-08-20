"""
Capa 2 - Lógica
Responsable de normalizar texto, comparar respuestas y calcular puntajes.
"""
import unicodedata


def normalizar(texto):
    """Normaliza un texto para comparación: minúsculas, sin tildes, sin espacios extra."""
    if texto is None:
        return ""
    texto = str(texto).strip().lower()
    texto = "".join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )
    return " ".join(texto.split())


class Evaluador:
    """Evalúa respuestas del usuario contra las respuestas correctas de un examen."""

    EQUIVALENCIAS_VF = {
        "v": "verdadero", "verdadero": "verdadero", "true": "verdadero", "t": "verdadero",
        "f": "falso", "falso": "falso", "false": "falso",
    }

    def evaluar_pregunta(self, pregunta, respuesta_usuario):
        """
        Evalúa una respuesta y retorna (es_correcta, puntaje_obtenido, retroalimentacion).
        En 'emparejamiento' el puntaje puede ser parcial según los pares acertados.
        """
        tipo = pregunta["tipo"]
        puntaje_total = pregunta.get("puntaje", 1)

        if tipo == "opcion_multiple":
            correcta = self._eval_opcion_multiple(pregunta, respuesta_usuario)
            puntaje_obtenido = puntaje_total if correcta else 0

        elif tipo == "verdadero_falso":
            correcta = self._eval_verdadero_falso(pregunta, respuesta_usuario)
            puntaje_obtenido = puntaje_total if correcta else 0

        elif tipo == "completar_espacios":
            correcta = self._eval_completar_espacios(pregunta, respuesta_usuario)
            puntaje_obtenido = puntaje_total if correcta else 0

        elif tipo == "emparejamiento":
            correcta, fraccion = self._eval_emparejamiento(pregunta, respuesta_usuario)
            puntaje_obtenido = round(puntaje_total * fraccion, 2)

        else:
            raise ValueError(f"Tipo de pregunta no soportado: {tipo}")

        retro = self._retroalimentacion(pregunta, correcta)
        return correcta, puntaje_obtenido, retro

    def _eval_opcion_multiple(self, pregunta, respuesta_usuario):
        correcta = pregunta["respuesta_correcta"]
        # Soporta una única respuesta o varias respuestas correctas (lista)
        if isinstance(correcta, list):
            if not isinstance(respuesta_usuario, list):
                respuesta_usuario = [r.strip() for r in str(respuesta_usuario).split(",")]
            set_correcta = {normalizar(c) for c in correcta}
            set_usuario = {normalizar(r) for r in respuesta_usuario if r}
            return set_correcta == set_usuario
        return normalizar(respuesta_usuario) == normalizar(correcta)

    def _eval_verdadero_falso(self, pregunta, respuesta_usuario):
        correcta = self.EQUIVALENCIAS_VF.get(normalizar(pregunta["respuesta_correcta"]))
        usuario = self.EQUIVALENCIAS_VF.get(normalizar(respuesta_usuario))
        return correcta is not None and correcta == usuario

    def _eval_completar_espacios(self, pregunta, respuesta_usuario):
        aceptadas = pregunta["respuesta_correcta"]
        if not isinstance(aceptadas, list):
            aceptadas = [aceptadas]
        return normalizar(respuesta_usuario) in {normalizar(a) for a in aceptadas}

    def _eval_emparejamiento(self, pregunta, respuesta_usuario):
        """respuesta_usuario: dict {termino: definicion_elegida}."""
        pares = pregunta["pares"]
        total = len(pares)
        if total == 0:
            return True, 1.0
        aciertos = 0
        for par in pares:
            termino = par["termino"]
            definicion_correcta = par["definicion"]
            definicion_usuario = (respuesta_usuario or {}).get(termino, "")
            if normalizar(definicion_usuario) == normalizar(definicion_correcta):
                aciertos += 1
        fraccion = aciertos / total
        return (aciertos == total), fraccion

    def _retroalimentacion(self, pregunta, correcta):
        if correcta:
            return "¡Correcto!"
        return pregunta.get("retroalimentacion_incorrecta", "Respuesta incorrecta.")

class Examen:
    def __init__(self, examen_id: str, titulo: str, descripcion: str = "", tiempo_limite_min: int = 60):
        self.id = examen_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.tiempo_limite = tiempo_limite_min
        self.preguntas = []
        self.estado = "Pendiente"

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)


class DetalleRespuesta:

    def __init__(self, pregunta_id: int, respuesta_usuario: str, es_correcta: bool, puntaje_obtenido: float, retroalimentacion: str):
        self.pregunta_id = pregunta_id
        self.respuesta_usuario = respuesta_usuario
        self.es_correcta = es_correcta
        self.puntaje_obtenido = puntaje_obtenido
        self.retroalimentacion = retroalimentacion


class ResultadoExamen:

    def __init__(self, examen_id: str, estudiante_id: str = "Invitado"):
        self.examen_id = examen_id
        self.estudiante_id = estudiante_id
        self.puntaje_total = 0.0
        self.puntaje_maximo_posible = 0.0
        self.detalles = []
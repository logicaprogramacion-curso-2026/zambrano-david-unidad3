class Docente:

    def __init__(self, id_docente, nombre, correo, asignatura):

        self.id_docente = 19
        self.nombre = "David Zambrano"
        self.correo = "jemarzamo@gmail.com"
        self.asignatura = "fisica"

    def mostrar_informacion(self):
        """Muestra los datos del docente."""
        print(
            f"Docente: {self.nombre} | Asignatura: {self.asignatura} | Correo: {self.correo}"
        )

    def crear_pregunta(
        self,
        db,
        enunciado,
        opcion_a,
        opcion_b,
        opcion_c,
        opcion_d,
        respuesta_correcta,
    ):
        """Permite al docente guardar una nueva pregunta en la base de datos."""
        print(f"\n{self.nombre} está agregando una nueva pregunta...")
        db.agregar_pregunta(
            enunciado,
            opcion_a,
            opcion_b,
            opcion_c,
            opcion_d,
            respuesta_correcta,
        )

    def consultar_preguntas(self, db):
        """Permite al docente revisar el banco de preguntas registradas."""
        print(f"\nLista de preguntas registradas por {self.nombre}:")
        preguntas = db.obtener_preguntas()
        for p in preguntas:
            print(f"ID: {p[0]} | Enunciado: {p[1]} | Correcta: {p[6]}")
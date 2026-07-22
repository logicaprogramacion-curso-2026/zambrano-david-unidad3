class Estudiante:

    def __init__(self, id_estudiante, nombre, matricula, correo, carrera):

        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.matricula = matricula
        self.correo = correo
        self.carrera = carrera

    def mostrar_informacion(self):
        """Muestra la ficha técnica del estudiante."""
        print(
            f"Estudiante: {self.nombre} | Matrícula: {self.matricula} | Carrera: {self.carrera}"
        )

    def responder_evaluacion(self, evaluacion):
        """Simula al estudiante rindiendo un examen."""
        print(
            f"\n{self.nombre} ha iniciado la evaluación: {evaluacion.titulo}"
        )
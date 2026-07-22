from database import Database
from docente import Docente
from estudiante import Estudiante


def main():

    database_pe = Database()


    docente_1 = Docente(
        id_docente=1,
        nombre="David Zambrano",
        correo="jemarzamo@gmail.com",
        asignatura="Lógica de Programación",
    )

    estudiante_1 = Estudiante(
        id_estudiante=101,
        nombre="Marlon Moreira",
        matricula="2026001",
        correo="marlon@123.com",
        carrera="Ingeniería",
    )
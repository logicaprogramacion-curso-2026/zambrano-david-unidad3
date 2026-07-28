from src.dao import PreguntaDAO
from src.entidad import Pregunta

def probar_conexion():
    print("Probando conexión con la base de datos...")
    dao = PreguntaDAO("banco_preguntas.db")
    print("Conexión exitosa. Tabla 'preguntas' verificada/creada.")

    pregunta_prueba = Pregunta(
        pregunta="¿Qué función abre un archivo en Python?",
        opcion_a="open()", opcion_b="file()", opcion_c="read()", opcion_d="load()",
        respuesta_correcta="A", dificultad="Fácil", tema="Manejo de archivos"
    )
    id_generado = dao.insertar(pregunta_prueba)
    print(f"Pregunta de prueba insertada con id={id_generado}")

    encontrada = dao.obtener_por_id(id_generado)
    print("Pregunta recuperada desde la BD:")
    print(encontrada)

    total = len(dao.obtener_todas())
    print(f"Total de preguntas en la base de datos: {total}")
if __name__ == "__main__":
    probar_conexion()   

   #10
   
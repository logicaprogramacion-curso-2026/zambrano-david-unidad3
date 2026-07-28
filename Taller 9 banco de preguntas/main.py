from pathlib import Path
from src.dao import PreguntaDAO
from src.gestor import GestorPreguntas
from src.simulador import Simulador


def main():
    print("SISTEMA DE BANCO DE PREGUNTAS")

    base_dir = Path(__file__).resolve().parent

    ruta_db = base_dir / "banco_preguntas.db"
    ruta_txt = base_dir / "PREGUNTAS_PYTHON.TXT"

    print("\nConectando con la base de datos...")
    dao = PreguntaDAO(str(ruta_db))
    gestor = GestorPreguntas(dao=dao)
    print("Conexión exitosa.")

    print("\nCargando preguntas desde archivo TXT...")
    preguntas = gestor.cargar_desde_txt(str(ruta_txt))
    print(f"Preguntas cargadas desde el archivo: {len(preguntas)}")

    print("\nGuardando preguntas en la base de datos...")
    gestor.guardar_en_base_datos(preguntas)

    total_bd = len(dao.obtener_todas())
    print(f"Total de preguntas en la base de datos: {total_bd}")

    print("\nExportando preguntas desde la base de datos...")
    gestor.exportar_a_txt(str(base_dir / "preguntas_exportadas.txt"))
    gestor.exportar_a_csv(str(base_dir / "preguntas_exportadas.csv"))
    gestor.exportar_a_json(str(base_dir / "preguntas_exportadas.json"))

    print("\nEstadísticas por tema")
    gestor.estadisticas_por_tema()

    print("\nEstadísticas por dificultad")
    gestor.estadisticas_por_dificultad()

    print("\nSIMULADOR DE EVALUACIÓN")
    preguntas_bd = dao.obtener_todas()

    simulador = Simulador(preguntas_bd)

    try:
        cantidad = int(input("¿Cuántas preguntas deseas responder? "))
    except ValueError:
        cantidad = 5
        print("Entrada inválida. Se usarán 5 preguntas por defecto.")

    simulador.iniciar_simulacion(cantidad)


if __name__ == "__main__":
    main()
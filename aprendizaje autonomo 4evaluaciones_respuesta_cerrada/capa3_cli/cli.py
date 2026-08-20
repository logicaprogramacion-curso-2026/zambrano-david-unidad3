"""
Capa 3 - CLI
Menú de interacción con el usuario: seleccionar examen o generar uno desde
un banco de preguntas, responder preguntas y mostrar resultados con
retroalimentación.
"""
from capa1_datos.cargador import CargadorDatos
from capa2_logica.evaluador import Evaluador
from capa2_logica.generador import GeneradorExamenes


class Simulador:
    """Simulador de evaluaciones de respuesta cerrada por consola."""

    def __init__(self, carpeta_datos="data", carpeta_bancos="bancos"):
        self.cargador = CargadorDatos(carpeta_datos, carpeta_bancos)
        self.evaluador = Evaluador()
        self.generador = GeneradorExamenes()

    def iniciar(self):
        print("=" * 50)
        print(" SISTEMA DE EVALUACIONES DE RESPUESTA CERRADA")
        print("=" * 50)
        while True:
            opcion = self._menu_principal()
            if opcion == "1":
                self._flujo_examen()
            elif opcion == "2":
                self._flujo_banco()
            elif opcion == "3":
                print("\n¡Hasta luego!")
                break
            else:
                print("\nOpción inválida. Intenta de nuevo.")

    def _menu_principal(self):
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Rendir un examen")
        print("2. Generar examen aleatorio desde un banco de preguntas")
        print("3. Salir")
        return input("Selecciona una opción: ").strip()

    # -- Opción 1: exámenes predefinidos -------------------------------------
    def _flujo_examen(self):
        examenes = self.cargador.listar_examenes()
        if not examenes:
            print("\nNo se encontraron exámenes en la carpeta de datos.")
            return

        print("\n--- EXÁMENES DISPONIBLES ---")
        for i, nombre in enumerate(examenes, start=1):
            print(f"{i}. {nombre}")

        seleccion = input("Selecciona el número del examen: ").strip()
        if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(examenes)):
            print("\nSelección inválida.")
            return

        try:
            examen = self.cargador.cargar_examen(examenes[int(seleccion) - 1])
        except (ValueError, OSError) as e:
            print(f"\nError al cargar el examen: {e}")
            return

        self._rendir_examen(examen)

    # -- Opción 2: examen generado desde un banco de preguntas ---------------
    def _flujo_banco(self):
        bancos = self.cargador.listar_bancos()
        if not bancos:
            print("\nNo se encontraron bancos de preguntas en la carpeta 'bancos'.")
            return

        print("\n--- BANCOS DE PREGUNTAS DISPONIBLES ---")
        for i, nombre in enumerate(bancos, start=1):
            print(f"{i}. {nombre}")

        seleccion = input("Selecciona el número del banco: ").strip()
        if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(bancos)):
            print("\nSelección inválida.")
            return

        try:
            banco = self.cargador.cargar_banco(bancos[int(seleccion) - 1])
        except (ValueError, OSError) as e:
            print(f"\nError al cargar el banco de preguntas: {e}")
            return

        total_disponible = len(banco["preguntas"])
        print(f"\nEste banco tiene {total_disponible} preguntas disponibles.")
        cantidad_str = input(
            f"¿Cuántas preguntas quieres en el examen (1-{total_disponible})?: "
        ).strip()
        if not cantidad_str.isdigit() or not (1 <= int(cantidad_str) <= total_disponible):
            print("\nCantidad inválida.")
            return

        examen_generado = self.generador.generar_examen_aleatorio(banco, int(cantidad_str))
        self._rendir_examen(examen_generado)

    # -- Flujo común: responder y calificar un examen ya cargado -------------
    def _rendir_examen(self, examen):
        print(f"\n--- {examen.get('titulo', 'Examen')} ---")
        preguntas = examen["preguntas"]
        puntaje_obtenido_total = 0
        puntaje_maximo_total = 0
        resultados = []

        for idx, pregunta in enumerate(preguntas, start=1):
            print(f"\nPregunta {idx}: {pregunta['enunciado']}")
            respuesta_usuario = self._solicitar_respuesta(pregunta)
            correcta, puntaje_obtenido, retro = self.evaluador.evaluar_pregunta(
                pregunta, respuesta_usuario
            )
            puntaje_maximo = pregunta.get("puntaje", 1)
            puntaje_obtenido_total += puntaje_obtenido
            puntaje_maximo_total += puntaje_maximo

            resultados.append({
                "numero": idx,
                "enunciado": pregunta["enunciado"],
                "correcta": correcta,
                "puntaje_obtenido": puntaje_obtenido,
                "puntaje_maximo": puntaje_maximo,
                "retroalimentacion": retro,
            })
            print("Correcto" if correcta else f"Incorrecto - {retro}")

        self._mostrar_resultados(resultados, puntaje_obtenido_total, puntaje_maximo_total)

    def _solicitar_respuesta(self, pregunta):
        tipo = pregunta["tipo"]

        if tipo == "opcion_multiple":
            for opcion in pregunta["opciones"]:
                print(f"  {opcion}")
            if isinstance(pregunta.get("respuesta_correcta"), list):
                return input(
                    "Tu respuesta (una o varias letras separadas por coma, ej: A,C): "
                ).strip()
            return input("Tu respuesta (letra): ").strip()

        if tipo == "verdadero_falso":
            return input("¿Verdadero o Falso?: ").strip()

        if tipo == "completar_espacios":
            return input("Completa el espacio: ").strip()

        if tipo == "emparejamiento":
            pares = pregunta["pares"]
            definiciones = [p["definicion"] for p in pares]
            letras = [chr(65 + i) for i in range(len(definiciones))]
            print("  Definiciones:")
            for letra, definicion in zip(letras, definiciones):
                print(f"    {letra}) {definicion}")
            respuesta = {}
            for par in pares:
                letra_usuario = input(f"  '{par['termino']}' corresponde a: ").strip().upper()
                if letra_usuario in letras:
                    respuesta[par["termino"]] = definiciones[letras.index(letra_usuario)]
                else:
                    respuesta[par["termino"]] = ""
            return respuesta

        raise ValueError(f"Tipo de pregunta no soportado: {tipo}")

    def _mostrar_resultados(self, resultados, obtenido, maximo):
        print("\n" + "=" * 50)
        print(" RESULTADOS")
        print("=" * 50)
        for r in resultados:
            estado = "CORRECTA" if r["correcta"] else "INCORRECTA"
            print(f"\nPregunta {r['numero']} - {estado} "
                  f"({r['puntaje_obtenido']}/{r['puntaje_maximo']} pts)")
            print(f"  {r['enunciado']}")
            if not r["correcta"]:
                print(f"  Retroalimentacion: {r['retroalimentacion']}")

        porcentaje = (obtenido / maximo * 100) if maximo else 0
        print("\n" + "-" * 50)
        print(f"PUNTAJE TOTAL: {obtenido}/{maximo}  ({porcentaje:.1f}%)")
        print("-" * 50)

"""
Módulo: simulador.py
Implementa la clase Simulador para ejecutar una evaluación interactiva
con preguntas de opción múltiple.
"""

import random


class Simulador:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.preguntas_seleccionadas = []
        self.respuestas_registradas = []
        self.puntaje = 0

    def iniciar_simulacion(self, cantidad):
        if not self.preguntas:
            print("No hay preguntas disponibles para la simulación.")
            return

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        if cantidad > len(self.preguntas):
            cantidad = len(self.preguntas)

        self.preguntas_seleccionadas = random.sample(self.preguntas, cantidad)
        self.respuestas_registradas = []
        self.puntaje = 0

        print("\n=== INICIO DE LA SIMULACIÓN ===")
        print(f"Total de preguntas: {cantidad}\n")

        for i, pregunta in enumerate(self.preguntas_seleccionadas, start=1):
            print(f"\nPregunta {i} de {cantidad}")
            self.mostrar_pregunta(pregunta)

            respuesta_usuario = input("Tu respuesta (A, B, C o D): ").strip().upper()
            while respuesta_usuario not in ("A", "B", "C", "D"):
                respuesta_usuario = input("Respuesta inválida. Ingresa A, B, C o D: ").strip().upper()

            es_correcta = self.validar_respuesta(pregunta, respuesta_usuario)

            if es_correcta:
                self.puntaje += 1
                print("Correcto")
            else:
                print(f"Incorrecto. La respuesta correcta era: {pregunta.respuesta_correcta}")

            self.respuestas_registradas.append({
                "pregunta": pregunta.pregunta,
                "respuesta_usuario": respuesta_usuario,
                "respuesta_correcta": pregunta.respuesta_correcta,
                "es_correcta": es_correcta,
                "tema": pregunta.tema,
                "dificultad": pregunta.dificultad
            })

        self.generar_reporte()

    def mostrar_pregunta(self, pregunta):
        print(f"Enunciado: {pregunta.pregunta}")
        print(f"A) {pregunta.opcion_a}")
        print(f"B) {pregunta.opcion_b}")
        print(f"C) {pregunta.opcion_c}")
        print(f"D) {pregunta.opcion_d}")
        print(f"Tema: {pregunta.tema} | Dificultad: {pregunta.dificultad}")

    def validar_respuesta(self, pregunta, respuesta):
        return respuesta == pregunta.respuesta_correcta.strip().upper()

    def generar_reporte(self):
        total = len(self.respuestas_registradas)
        incorrectas = total - self.puntaje
        porcentaje = (self.puntaje / total * 100) if total > 0 else 0

        print("\n=== REPORTE FINAL ===")
        print(f"Total de preguntas: {total}")
        print(f"Correctas: {self.puntaje}")
        print(f"Incorrectas: {incorrectas}")
        print(f"Puntaje final: {porcentaje:.2f}%")

        print("\n--- Detalle de respuestas ---")
        for i, registro in enumerate(self.respuestas_registradas, start=1):
            estado = "Correcta" if registro["es_correcta"] else "Incorrecta"
            print(f"{i}. {registro['pregunta']}")
            print(f"   Tu respuesta: {registro['respuesta_usuario']}")
            print(f"   Respuesta correcta: {registro['respuesta_correcta']}")
            print(f"   Resultado: {estado}")
            print(f"   Tema: {registro['tema']} | Dificultad: {registro['dificultad']}")
            print("-" * 50)
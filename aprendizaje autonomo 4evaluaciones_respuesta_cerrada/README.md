# Sistema de Evaluaciones de Respuesta Cerrada

CLI en Python que carga exámenes desde archivos JSON, permite responderlos de forma
interactiva y calcula el puntaje con retroalimentación para cada pregunta incorrecta.

Soporta cuatro tipos de pregunta cerrada:

- **Opción múltiple** — una respuesta, o **varias respuestas** si `respuesta_correcta`
  es una lista (la CLI avisa cuándo se puede marcar más de una, separadas por coma)
- **Verdadero / Falso**
- **Emparejamiento** (con puntaje parcial según los pares acertados)
- **Completar espacios**

También incluye, como extensión opcional del enunciado, **generación automática de
exámenes a partir de un banco de preguntas** (selección aleatoria con `random.sample`,
sin usar ningún servicio ni API externa).

## Requisitos

- Python 3.8 o superior (no requiere librerías externas)

## Ejecución

```bash
python main.py
```

Desde el menú:

1. `1` — Rendir un examen predefinido (se listan los `.json` disponibles en `data/`)
2. `2` — Generar un examen aleatorio a partir de un banco de preguntas (se listan
   los `.json` disponibles en `bancos/`, se elige uno y cuántas preguntas incluir)
3. `3` — Salir

Al finalizar un examen se muestra, por cada pregunta, si fue correcta o incorrecta,
la retroalimentación en caso de error, y al final el **puntaje total** obtenido
sobre el puntaje máximo.

## Estructura del proyecto (arquitectura por capas)

```
evaluaciones_respuesta_cerrada/
├── main.py                    # Punto de entrada
├── data/
│   └── examen_python_basico.json   # Examen de ejemplo (9 preguntas)
├── bancos/
│   └── banco_python_basico.json    # Banco de preguntas (16 preguntas) para generación aleatoria
├── capa1_datos/
│   └── cargador.py            # Carga y valida exámenes y bancos desde JSON
├── capa2_logica/
│   ├── evaluador.py           # Normalización, comparación y cálculo de puntaje
│   └── generador.py           # Generación aleatoria de exámenes desde un banco (random.sample)
└── capa3_cli/
    └── cli.py                 # Menú interactivo (clase Simulador)
```

- **Capa 1 (datos)** — `CargadorDatos`: lee los `.json` de `data/` (exámenes) y
  `bancos/` (bancos de preguntas), y valida que cada pregunta tenga tipo, enunciado,
  puntaje y los campos propios de su tipo (`opciones`, `pares`, `respuesta_correcta`).
- **Capa 2 (lógica)** — `Evaluador`: compara la respuesta del usuario contra la
  respuesta correcta usando normalización (minúsculas, sin tildes, sin espacios
  extra) y calcula el puntaje obtenido, incluyendo puntaje parcial en emparejamiento.
  `GeneradorExamenes`: arma un examen nuevo tomando N preguntas al azar de un banco.
- **Capa 3 (CLI)** — `Simulador`: menú de consola para elegir examen o generar uno
  desde un banco, responder preguntas y mostrar resultados.

## Formato del JSON de examen

Cada archivo en `data/` debe tener esta forma:

```json
{
  "titulo": "Nombre del examen",
  "preguntas": [
    {
      "tipo": "opcion_multiple",
      "enunciado": "¿Pregunta?",
      "opciones": ["A) ...", "B) ...", "C) ...", "D) ..."],
      "respuesta_correcta": "B",
      "puntaje": 2,
      "retroalimentacion_incorrecta": "Explicación del error."
    }
  ]
}
```

Para **verdadero_falso**, `respuesta_correcta` es `"verdadero"` o `"falso"`.
Para **completar_espacios**, `respuesta_correcta` puede ser un string o una lista
de respuestas aceptadas. Para **emparejamiento**, en lugar de `opciones` se usa
`pares`: una lista de `{"termino": "...", "definicion": "..."}`.

Un **banco de preguntas** (carpeta `bancos/`) usa el mismo formato, pero en vez de
`titulo` se recomienda usar `nombre_banco`, ya que de él no se rinde el archivo
completo sino que se sortean N preguntas para armar un examen nuevo.

## Agregar un nuevo examen o banco de preguntas

Basta con crear un nuevo archivo `.json` (siguiendo el formato anterior) dentro
de `data/` (examen fijo) o `bancos/` (banco para generación aleatoria); aparecerá
automáticamente en el menú correspondiente al ejecutar el programa.

## Extensiones no incluidas en esta entrega

- Generación de preguntas nuevas con un LLM (mencionada como opcional en el
  enunciado; se dejó fuera a propósito, sin usar la API de Anthropic ni ninguna
  otra).

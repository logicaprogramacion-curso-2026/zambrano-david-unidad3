# 📚 Sistema de Preguntas y Respuestas - Proyecto Taller 9

## 👥 Integrantes del Grupo
- Marlon Zambrano Moreira - 
- Matthew Escalante - 
- Mel Elias - 

## 📅 Fechas
- Inicio: 27/07/2026
- Entrega: 04/08/2026

## 📝 Descripción del Proyecto
El proyecto consiste en el desarrollo de un sistema de Banco de Preguntas en Python, diseñado para administrar, almacenar y evaluar preguntas de opción múltiple de manera interactiva.

El sistema permite cargar preguntas desde archivos TXT, CSV y JSON, guardarlas en una base de datos SQLite y gestionarlas mediante distintos módulos aplicando programación orientada a objetos.

Cuenta con funcionalidades para visualizar preguntas, consultar estadísticas por tema y por dificultad, realizar simulaciones de evaluación con selección aleatoria de preguntas, validar respuestas, calcular puntajes y generar reportes de resultados en formatos TXT, CSV y JSON.

La aplicación se desarrolló con una estructura modular y separación de responsabilidades entre la entidad de preguntas (`entidad.py`), el acceso a datos (`dao.py`), el gestor de carga/exportación (`gestor.py`) y el simulador de evaluaciones (`simulador.py`), además de pruebas unitarias para verificar el correcto funcionamiento del sistema.

## 🛠️ Tecnologías Utilizadas
- Python 3.8+
- SQLite3
- Git

## 📁 Estructura del Proyecto
```
Taller 9 banco de preguntas/
├── main.py                    # Menú principal / punto de entrada
├── requeriments.txt
├── README.md
├── PREGUNTAS_PYTHON.txt       # Banco de 50 preguntas (origen TXT)
├── PREGUNTAS_PYTHON.csv       # Banco de 50 preguntas (origen CSV)
├── PREGUNTAS_PYTHON.json      # Banco de 50 preguntas (origen JSON)
├── database/
│   └── preguntas.db           # Base de datos SQLite
├── resultados/
│   ├── respuestas_usuario.txt # Reporte TXT de cada simulación
│   ├── estadisticas.csv       # Reporte CSV de cada simulación
│   └── reporte.json           # Reporte JSON completo
├── evidencia/                 # Capturas de pantalla por iteración
├── src/
│   ├── __init__.py
│   ├── entidad.py             # Clase Pregunta
│   ├── dao.py                 # Clase PreguntaDAO (acceso a SQLite)
│   ├── gestor.py               # Clase GestorPreguntas (carga/exportación)
│   └── simulador.py            # Clase Simulador (evaluación y reportes)
└── tests/
    ├── test_entidad.py
    └── test_dao.py
```

---

## 📊 Evidencias de Ejecución por Iteración

### Iteración 1: Configuración Inicial
Se creó la estructura base del proyecto, la clase `Pregunta` en `entidad.py` (atributos, `__init__`, `__str__`, `to_dict`) y el archivo `src/__init__.py`.


### Iteración 2: Creación de Archivos
Se generaron las 50 preguntas de programación en Python y se guardaron en tres formatos.

- ✅ PREGUNTAS_PYTHON.txt (50 preguntas)
- ✅ PREGUNTAS_PYTHON.csv (50 preguntas)
- ✅ PREGUNTAS_PYTHON.json (50 preguntas)


### Iteración 3: Implementación del DAO y Base de Datos
Se implementó `PreguntaDAO` en `dao.py`: conexión a SQLite, `crear_tabla()`, `insertar()`, `obtener_todas()` y `obtener_por_id()`. Se verificó la conexión desde `main.py`.

- ✅ Tabla 'preguntas' creada
- ✅ Conexión exitosa
- ✅ Métodos CRUD implementados


### Iteración 4: Carga de Datos desde Archivos
Se implementaron `cargar_desde_txt()`, `cargar_desde_csv()` y `cargar_desde_json()` en `gestor.py`, con validación de campos obligatorios y de dominio (respuesta_correcta, dificultad). Se agregó el menú en `main.py` para elegir el origen del archivo.

- ✅ Carga desde TXT: 50 preguntas cargadas
- ✅ Carga desde CSV: 50 preguntas cargadas
- ✅ Carga desde JSON: 50 preguntas cargadas


### Iteración 5: Guardado en Base de Datos y Exportación
Se implementó `guardar_en_base_datos()` en el Gestor, junto con `exportar_a_txt()`, `exportar_a_csv()` y `exportar_a_json()`. Se agregaron las consultas `estadisticas_por_tema()` y `estadisticas_por_dificultad()`.

- ✅ 50 preguntas guardadas en SQLite
- ✅ Exportación a TXT, CSV y JSON desde la base de datos


### Iteración 6: Implementación del Simulador
Se creó la clase `Simulador` en `simulador.py`: selección aleatoria de preguntas, presentación interactiva, validación de respuestas y cálculo de puntaje.

- ✅ Selección aleatoria de preguntas
- ✅ Interacción con el usuario
- ✅ Validación de respuestas
- ✅ Cálculo de puntaje


### Iteración 7: Generación de Reportes y Resultados
Se implementaron `reporte_txt()`, `reporte_csv()` y `reporte_json()`, guardados en la carpeta `resultados/` (`respuestas_usuario.txt`, `estadisticas.csv`, `reporte.json`). Cada reporte incluye fecha y hora de la simulación, detalle de preguntas y respuestas, puntaje obtenido y estadísticas por tema y por dificultad.

- ✅ Reporte TXT generado
- ✅ Reporte CSV generado
- ✅ Reporte JSON generado


### Iteración 8: Integración Final y Pruebas
Se implementó el menú completo en `main.py` (cargar preguntas, ver todas las preguntas, ver estadísticas, iniciar simulación, exportar datos, ver reportes, salir), manejo de errores en todo el sistema y pruebas unitarias para la entidad y el DAO.

- ✅ Pruebas unitarias pasadas
- ✅ Integración completa verificada
- ✅ Manejo de errores implementado



---

## 🧪 Pruebas Realizadas
✅ Carga desde TXT: 50 preguntas cargadas
✅ Carga desde CSV: 50 preguntas cargadas
✅ Carga desde JSON: 50 preguntas cargadas
txt csv json

## 📊 Estadísticas Finales
- Total preguntas: 50
- Temas cubiertos: [completa con el resultado del script de conteo]
- Dificultades: [completa: Fácil (X), Media (Y), Difícil (Z)]

## 🎯 Conclusiones

### Resumen del trabajo realizado
Durante el desarrollo del proyecto se implementó un sistema de banco de preguntas en Python, que permite cargar preguntas desde archivos TXT, CSV y JSON, almacenarlas en una base de datos SQLite y gestionarlas mediante una arquitectura organizada por módulos.

Se desarrollaron componentes para la entidad de preguntas, el acceso a datos mediante DAO, la gestión de carga y exportación de información, la simulación interactiva de evaluaciones, la validación de respuestas, el cálculo de puntajes y la generación de reportes en formatos TXT, CSV y JSON. Además, se implementó un menú principal para facilitar la interacción con el usuario, manejo de errores y pruebas unitarias para verificar el correcto funcionamiento de los módulos principales.

### Lecciones aprendidas
Durante la realización del proyecto se reforzaron conocimientos de programación orientada a objetos en Python, manejo de archivos en distintos formatos, conexión con bases de datos SQLite y organización de proyectos mediante separación de responsabilidades.

También se aprendió la importancia de manejar correctamente la codificación de texto (UTF-8) al trabajar con archivos que contienen tildes y caracteres especiales en español, de validar los datos de entrada, de crear pruebas unitarias y de mantener una estructura clara del código para facilitar el mantenimiento y futuras modificaciones.

### Mejoras futuras
Como mejoras futuras se podría implementar una interfaz gráfica para mejorar la experiencia del usuario, agregar un sistema de usuarios con historial de evaluaciones, incluir más formatos de importación y exportación, y desarrollar un sistema de preguntas con niveles de dificultad adaptativos.

También sería posible integrar inteligencia artificial para generar nuevas preguntas automáticamente o analizar el rendimiento de los usuarios a lo largo del tiempo.
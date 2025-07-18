# Survey API Backend

API RESTful para crear y gestionar encuestas, preguntas y opciones de respuesta. Construida con FastAPI y PostgreSQL, lista para desarrollo profesional, testing y despliegue.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación y configuración](#instalación-y-configuración)
- [Ejecución de la aplicación](#ejecución-de-la-aplicación)
- [Pruebas](#pruebas)
- [Uso con Postman](#uso-con-postman)
- [Integración continua (CI)](#integración-continua-ci)
- [Estructura del proyecto](#estructura-del-proyecto)

## Requisitos

- Python 3.11+
- PostgreSQL 13+
- pip

## Instalación y configuración

1. Clona el repositorio:
   ```bash
   git clone https://github.com/anderssongodoy/survey_backend.git
   cd survey_backend
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   # source .venv/bin/activate  # En Linux/Mac
   ```
3. Crea el archivo `.env` en la raíz con:
   ```env
   DATABASE_URL=postgresql://postgres:1234@localhost:5432/survey_db
   LOG_LEVEL=INFO
   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
5. Asegúrate de tener PostgreSQL corriendo y la base de datos `survey_db` creada:
   ```sql
   -- En psql
   CREATE DATABASE survey_db
       WITH
       OWNER = postgres
       ENCODING = 'UTF8'
       LC_COLLATE = 'C'
       LC_CTYPE = 'C'
       TEMPLATE = template0;
   ```

## Ejecución de la aplicación

Levanta el servidor de desarrollo con:

```bash
uvicorn app.main:app --reload
```

Las tablas se crean automáticamente al iniciar la app.

## Pruebas

Ejecuta todos los tests unitarios con:

```bash
pytest app/tests
```

## Uso con Postman

### 1. Crear una encuesta

**POST** `http://localhost:8000/surveys/`
Body (JSON):

```json
{
  "title": "Encuesta de satisfacción",
  "description": "Por favor califica nuestro servicio"
}
```

### 2. Agregar una pregunta a una encuesta

**POST** `http://localhost:8000/surveys/{survey_id}/questions/`
Body (JSON):

```json
{
  "text": "¿Cómo calificarías el servicio?",
  "question_type": "single_choice"
}
```

### 3. Agregar una opción a una pregunta

**POST** `http://localhost:8000/questions/{question_id}/options/`
Body (JSON):

```json
{
  "text": "Muy satisfecho"
}
```

Las respuestas de error son claras si envías datos inválidos o IDs inexistentes.

### 4. Listar todas las encuestas

**GET** `http://localhost:8000/surveys`
Respuesta:

```json
[
  {
    "id": 1,
    "title": "Encuesta de satisfacción",
    "description": "Por favor califica nuestro servicio",
    "created_at": "2025-07-18T12:00:00",
    "questions": []
  }
]
```

### 5. Obtener detalles de una encuesta (con preguntas y opciones)

**GET** `http://localhost:8000/surveys/{survey_id}`
Respuesta:

```json
{
  "id": 1,
  "title": "Encuesta de satisfacción",
  "description": "Por favor califica nuestro servicio",
  "created_at": "2025-07-18T12:00:00",
  "questions": [
    {
      "id": 1,
      "text": "¿Cómo calificarías el servicio?",
      "question_type": "single_choice",
      "options": [
        { "id": 1, "text": "Muy satisfecho" }
      ]
    }
  ]
}
```

### 6. Obtener detalles de una pregunta (con opciones)

**GET** `http://localhost:8000/questions/{question_id}`
Respuesta:

```json
{
  "id": 1,
  "text": "¿Cómo calificarías el servicio?",
  "question_type": "single_choice",
  "options": [
    { "id": 1, "text": "Muy satisfecho" }
  ]
}
```

## Integración continua (CI)

Cada push o pull request a `main` o `dev` ejecuta automáticamente un workflow de GitHub Actions que:

- Levanta un contenedor de PostgreSQL para pruebas
- Instala las dependencias del proyecto
- Ejecuta todos los tests unitarios con pytest
- Si algún test falla, el workflow marca el build como fallido

## Estructura del proyecto

```
app/
  api/           # Routers de FastAPI
  core/          # Configuración y utilidades
  models/        # Modelos SQLAlchemy
  repositories/  # Acceso a datos
  schemas/       # Esquemas Pydantic
  services/      # Lógica de negocio
  tests/         # Tests unitarios
```

- **Separación de responsabilidades:** Cada capa (modelos, esquemas, repositorios, servicios, API) tiene una única responsabilidad, facilitando el mantenimiento y la extensión.
- **Modularidad:** La estructura permite agregar nuevas funcionalidades (por ejemplo, autenticación, analítica, nuevos tipos de preguntas) sin afectar el resto del sistema.
- **Abstracción:** El uso de repositorios y servicios desacopla la lógica de negocio del acceso a datos, permitiendo cambios en la base de datos o reglas de negocio sin modificar los endpoints.
- **Validación robusta:** Los esquemas de Pydantic aseguran que los datos de entrada y salida sean correctos y seguros.
- **Preparado para testing:** La estructura facilita la creación de pruebas unitarias y de integración.
- **Automatización:** El workflow de GitHub Actions garantiza calidad continua con lint y tests automáticos.
- **Escalabilidad real:** Si el proyecto crece, se pueden dividir las capas en microservicios, agregar cachés, colas, o escalar horizontalmente sin reescribir la base.

**Fundamento:**
Esta arquitectura sigue principios de Clean Architecture y SOLID, ampliamente recomendados en la industria para proyectos de cualquier tamaño. Permite que el equipo evolucione el sistema rápidamente, minimizando deuda técnica y facilitando la colaboración.

## Notas

- Los nombres de variables, clases y archivos están en inglés para mantener el estándar internacional.
- Los comentarios y la documentación están en español para facilitar la comprensión.

## Estructura del proyecto

```
app/
  core/           # Configuración, logging, conexión a base de datos
  models/         # Modelos SQLAlchemy
  schemas/        # Esquemas Pydantic
  repositories/   # Capa de acceso a datos
  services/       # Lógica de negocio
  api/            # Routers (endpoints)
  tests/          # Pruebas unitarias
```

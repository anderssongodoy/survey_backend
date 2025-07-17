

# Backend de API de Encuestas

Una API RESTful modular, escalable y mantenible para crear y gestionar encuestas, construida con FastAPI y PostgreSQL.

## Objetivos
- Arquitectura limpia y extensible (SOLID, Clean Code)
- Estructura modular de carpetas para desarrollo rápido
- Pruebas unitarias, logging y capas de abstracción
- Lista para producción y colaboración sencilla

## Enfoque y Decisiones Arquitectónicas
El proyecto está diseñado para ser fácilmente escalable y mantenible, siguiendo principios SOLID y Clean Code. Se utiliza una estructura modular con capas bien definidas (modelos, esquemas, repositorios, servicios, API) para facilitar la extensión y el testing.

Se prioriza la claridad, la separación de responsabilidades y la facilidad para agregar nuevas funcionalidades o modificar las existentes.

## ¿Cómo correr el proyecto?

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/anderssongodoy/survey_backend.git
   cd survey_backend/backend
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   # source .venv/bin/activate  # En Linux/Mac
   ```

3. **Instala las dependencias:**
   ```bash
   pip install fastapi sqlalchemy psycopg2-binary pydantic uvicorn
   ```

4. **Configura la base de datos:**
   - Crea una base de datos PostgreSQL local llamada `survey_db` (o ajusta la variable de entorno `DATABASE_URL` en `app/core/database.py`).

5. **Crea las tablas:**
   Puedes usar un script o migraciones (por ejemplo, con Alembic) para crear las tablas a partir de los modelos SQLAlchemy.

6. **Ejecuta la aplicación:**
   ```bash
   uvicorn app.main:app --reload
   ```

7. **Pruebas y CI:**
   - El proyecto incluye un workflow de GitHub Actions para lint y pruebas automáticas en cada push o pull request.

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

## Licencia
MIT

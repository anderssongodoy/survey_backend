

# Backend de API de Encuestas

Una API RESTful modular, escalable y mantenible para crear y gestionar encuestas, construida con FastAPI y PostgreSQL.

## Objetivos
- Arquitectura limpia y extensible (SOLID, Clean Code)
- Estructura modular de carpetas para desarrollo rápido
   No necesitas crear las tablas manualmente. Al iniciar la aplicación, las tablas se crean automáticamente a partir de los modelos SQLAlchemy.
- Lista para producción y colaboración sencilla

   ```bash
   pip install -r requirements.txt
   ```
Se prioriza la claridad, la separación de responsabilidades y la facilidad para agregar nuevas funcionalidades o modificar las existentes.


   - Ejecuta los tests con:
     ```bash
     pytest app/tests
     ```
   - El proyecto incluye un workflow de GitHub Actions que ejecuta los tests automáticamente en cada push o pull request.
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

3. **Crea el archivo `.env` con la URL de la base de datos:**
   ```env
   DATABASE_URL=postgresql://postgres:1234@localhost:5432/survey_db
   ```

4. **Instala las dependencias:**
   ```bash
   pip install fastapi sqlalchemy psycopg2-binary pydantic uvicorn python-dotenv
   ```

5. **Configura la base de datos:**
   - Crea una base de datos PostgreSQL local llamada `survey_db` (usuario: postgres, contraseña: 1234).

6. **Crea las tablas:**
   Puedes usar un script o migraciones (por ejemplo, con Alembic) para crear las tablas a partir de los modelos SQLAlchemy.

7. **Ejecuta la aplicación:**
   ```bash
   uvicorn app.main:app --reload
   ```

8. **Pruebas y CI:**
   - El proyecto incluye un workflow de GitHub Actions para lint y pruebas automáticas en cada push o pull request.

## ¿Por qué esta arquitectura es escalable y profesional?

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

## Licencia
MIT

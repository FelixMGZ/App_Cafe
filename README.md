# API RESTful de Cafetería con Flask y Python

Este repositorio contiene el código fuente de una API RESTful completa y robusta, construida progresivamente para demostrar un flujo de desarrollo backend profesional. La API permite gestionar recursos de una cafetería, como tostadores y tipos de café, e implementa un sistema de seguridad completo basado en roles.

Este proyecto cubre conceptos desde los fundamentos de Flask hasta la arquitectura de aplicaciones, pruebas automatizadas y autenticación segura.

## ✨ Características Principales (Features)

* **Arquitectura Escalable:** Estructura de proyecto profesional utilizando el patrón **Application Factory** y **Blueprints** para una organización modular y mantenible.
* **Gestión de Base de Datos:** Interacción con una base de datos **SQLite** a través del ORM **Flask-SQLAlchemy**, incluyendo modelado de datos y relaciones.
* **Relaciones Uno a Muchos:** Implementación de una relación entre `Tostadores` y `Cafés`, con borrado en cascada para mantener la integridad de los datos.
* **Autenticación Segura:** Sistema de registro y login de usuarios con contraseñas hasheadas (`werkzeug.security`).
* **Seguridad Basada en Tokens:** Uso de **JSON Web Tokens (JWT)** para proteger los endpoints, implementado con `Flask-JWT-Extended`.
* **Autorización por Roles:** Creación de un decorador personalizado (`@admin_required`) para restringir el acceso a endpoints críticos (ej. `DELETE`) solo a usuarios con rol de `administrador`.
* **Validación y Serialización:** (Opcional, si lo implementaste) Uso de `Flask-Marshmallow` para validar datos de entrada y serializar las respuestas JSON de forma limpia y consistente.
* **Pruebas Automatizadas:** Una suite de pruebas completa con `pytest` que garantiza la fiabilidad de la API, utilizando una base de datos en memoria para un aislamiento total.

## 🚀 Tecnologías Utilizadas

* **Backend:** Python 3
* **Framework:** Flask
* **Base de Datos:** SQLite con Flask-SQLAlchemy
* **Autenticación:** Flask-JWT-Extended
* **Pruebas:** pytest

## 📂 Estructura del Proyecto

El proyecto sigue una estructura organizada para facilitar la escalabilidad:

```
/
|-- /instance/              # Base de datos y archivos de configuración locales (ignorada por Git)
|-- /app/                   # Código fuente principal de la aplicación
|   |-- __init__.py         # Application Factory (create_app)
|   |-- models.py           # Modelos de SQLAlchemy (User, Toaster, Cafe)
|   |-- decorators.py       # Decoradores personalizados (@admin_required)
|   |-- auth/               # Blueprint para autenticación
|   |   |-- routes.py
|   |-- toasters/           # Blueprint para tostadores
|   |   |-- routes.py
|   |-- cafes/              # Blueprint para cafés
|   |   |-- routes.py
|-- /tests/                 # Pruebas automatizadas
|   |-- conftest.py         # Fixtures de pytest
|   |-- test_toasters.py
|-- .gitignore              # Archivos y carpetas a ignorar por Git
|-- requirements.txt        # Lista de dependencias del proyecto
|-- main.py                  # Punto de entrada para ejecutar la aplicación
```

## ⚙️ Instalación y Puesta en Marcha

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/FelixMGZ/App_Cafe]
    cd [APP Cafe]
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Crear el entorno
    python -m venv venv

    # Activar en Windows (PowerShell)
    .\venv\Scripts\Activate.ps1

    # Activar en macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    ```bash
    python run.py
    ```
    La API se iniciará y estará disponible en `http://127.0.0.1:5000`. La primera vez que se ejecute, creará la base de datos `cafes.db` en la carpeta `instance`.

## 🧪 Ejecución de Pruebas

Para verificar la integridad y el correcto funcionamiento de la API, puedes ejecutar la suite de pruebas automatizadas.

```bash
python -m pytest
```
Las pruebas se ejecutarán utilizando una base de datos SQLite en memoria para no afectar los datos de desarrollo.

## 📋 Endpoints de la API

A continuación se detallan los principales endpoints disponibles:

### Autenticación (`/auth`)

* **`POST /auth/register`**: Registra un nuevo usuario.
    * **Body:** `{"username": "nombre_de_usuario", "password": "tu_contraseña"}`
* **`POST /auth/login`**: Inicia sesión y devuelve un `access_token` JWT.
    * **Body:** `{"username": "nombre_de_usuario", "password": "tu_contraseña"}`

### Tostadores (`/toasters`)

* **`GET /toasters/`**: Obtiene una lista de todos los tostadores.
* **`POST /toasters/`**: Crea un nuevo tostador.
    * **Requiere Autenticación:** Token JWT válido.
    * **Body:** `{"name": "Nombre del Tostador"}`
* **`DELETE /toasters/<int:id>`**: Elimina un tostador.
    * **Requiere Autorización:** Token JWT con rol de **`admin`**.

### Cafés (`/cafes`)

* **`GET /cafes/`**: Obtiene una lista de todos los cafés, incluyendo la información de su tostador.
* **`POST /cafes/`**: Crea un nuevo café y lo asocia a un tostador existente.
    * **Requiere Autenticación:** Token JWT válido (cualquier rol).
    * **Body:**
        ```json
        {
            "name": "Etiopía Yirgacheffe",
            "price": 35.50,
            "description": "Notas florales y cítricas.",
            "toaster_id": 1
        }
        ```
* **`GET /cafes/<int:id>`**: Obtiene un café específico por su ID.
* **`PUT /cafes/<int:id>`**: Actualiza la información de un café.
    * **Requiere Autenticación:** Token JWT válido.
    * **Body:**
        ```json
        {
            "name": "Etiopía Yirgacheffe Lavado",
            "price": 38.00,
            "description": "Notas a bergamota y té negro."
        }
        ```
* **`DELETE /cafes/<int:id>`**: Elimina un café.
    * **Requiere Autenticación:** Token JWT válido (rol "admin").
 
---

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

Copyright (c) 2025

## 📬 Contacto

Desarrollado por Felix Martinez.

# API de control de entrenamiento

** Entrega módulo 2: Programación Avanzada - Ane Martínez Orellana**

---

## Descripción del proyecto

Aplicación backend desarrollada con FastAPI, que tiene como objetivo el poder monitorizar sesiones de entrenamiento de forma fácil. Se pueden crear, mostrar, actualizar y eliminar entrenamientos. La idea es, a la hora de crear una sesión de entrenamiento, ir añadiendo ejercicios.

---

## Tecnologías utilizadas
- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- Requests

---

## Estructura del proyecto

training_backend/
  app/
    main.py # App FastAPI (endpoints)
    models.py # Clases: Exercise, Session
    storage.py 
    schemas.py 
    init.py
  tests/
    test_requests.py # Pruebas de funcionamiento
  requirements.txt
  README.md
  .gitignore

---

## Endpoints aplicados

| Método | Endpoint | Descripción |
|---------|-----------|-------------|
| `POST` | `/trainings` | Crear una nueva sesión de entrenamiento |
| `GET` | `/trainings` | Muestra todas las sesiones de entrenamiento |
| `GET` | `/trainings/{id}` | Muestra una sesión de entrenamiento concreta |
| `PUT` | `/trainings/{id}` | Actualiza los datos de una sesión de entrenamiento|
| `DELETE` | `/trainings/{id}` | Eliminar un entrenamiento |
| `POST` | `/trainings/{id}/exercises` | Añadir un ejercicio a una sesión de entrenamiento|

---

## Pasos para ejecutar el proyecto
### 1. Clonar el repositorio
### 2. Crear entorno virtual e instalar dependencias
### 3. Ejecutar el servidor: uvicorn app.main: app --reload
La API estará disponible en: http://127.0.0.1:8000

## Cómo probar la API
### 1. Acceder desde el navegador: http://127.0.0.1:8000/docs (aquí podemos ver todos los endpoints con ejemplos).
### 2. Ejecutar script de pruebas (verifica que todos los endpoints funcionen): python tests/test_requests.py


#!/bin/bash

# Instala Pipenv si no está instalado
pip install pipenv

# Crea un entorno virtual con Pipenv y activa el entorno
pipenv install --deploy
pipenv shell

# Ejecuta tu servidor
uvicorn app.main:app --port 9000
# uvicorn app.main:app --reload
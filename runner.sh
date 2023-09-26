#!/bin/bash

# Instala Pipenv si no está instalado
pip install pipenv

# Crea un entorno virtual con Pipenv y activa el entorno
pipenv install --deploy
pipenv shell

# Ejecuta tu servidor
pipenv run server
# uvicorn app.main:app --reload
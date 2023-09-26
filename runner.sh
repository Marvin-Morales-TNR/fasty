#!/bin/bash

# Instala Pipenv si no está instalado
pip install pipenv
pipenv lock -r > requirements.txt
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 9000
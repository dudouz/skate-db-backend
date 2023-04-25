from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, request, jsonify, redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas import *

app = OpenAPI(__name__)

# definir tags da doc
home_tag = Tag('Home', description='Documentação da API')
atletas_tag = Tag('Atletas', description='Operações relacionadas a atletas')
campeonatos_tag = Tag('Campeonatos', description='Operações relacionadas a campeonatos')
resultados_tag = Tag('Resultados', description='Operações relacionadas a resultados')

# importar rotas
from routes.atleta_routes import atleta_routes
from routes.campeonato_routes import campeonato_routes

# registrar rotas
app.register_blueprint(atleta_routes)
app.register_blueprint(campeonato_routes)

# declaa rota do open api!
@app.route('/', tags=[home_tag])
def hello_skaters():
    return redirect('/openapi')

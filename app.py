from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, request, jsonify, redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from logger import logger

info = Info(title="Skate Database", version="1.0.0")
app = OpenAPI(__name__, info=info)

# definir tags da doc
home_tag = Tag(name='Home', description='Documentação da Skate Database')
campeonatos_tag = Tag(name='Campeonatos', description='Operações relacionadas a campeonatos')
atletas_tag = Tag(name='Atletas', description='Operações relacionadas a atletas')

# importar rotas
from routes.atleta_routes import atleta_routes
from routes.campeonato_routes import campeonato_routes

# registrar rotas
app.register_api(atleta_routes)
app.register_api(campeonato_routes)

# declara rota do open api!
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

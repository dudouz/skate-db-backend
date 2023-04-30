from flask import jsonify, request
from model import Session
from model.campeonato import Campeonato
from datetime import date
from flask_openapi3 import Tag, APIBlueprint, Schema, Parameter
from model.campeonato import Campeonato
from schemas import ListarCampeonatosSchema, AdicionarCampeonatoSchema, FormAddCampeonatoSchema, ListarCampeonatoIdSchema, DeletarCampeonatoIdSchema, CampeonatoPath

from logger import logger

campeonatos_tag = Tag(name='Campeonatos', description='Operações relacionadas a campeonatos')

campeonato_routes = APIBlueprint('campeonato_routes', __name__, abp_tags=[campeonatos_tag])


@campeonato_routes.get('/campeonatos',  responses={"200": ListarCampeonatosSchema})
def listar_campeonatos():
    """ Retorna uma listagem de campeonatos cadastrados no banco de dados.

    """
    session = Session()
    campeonatos = session.query(Campeonato).all()
    campeonatos_arr = []

    # foi criado um metodo toDict para serializar os dados
    for campeonato in campeonatos:
        campeonatos_arr.append(campeonato.toDict())

    return jsonify(campeonatos_arr)

@campeonato_routes.post('/campeonatos', responses={"200": AdicionarCampeonatoSchema})
def adicionar_campeonato():
    """ Adiciona um campeonato no banco de dados.

    """    
    session = Session()
   
    # parsear date da string
    data = date.fromisoformat(request.form['data'])

    campeonato = Campeonato(request.form['nome'], request.form['cidade'], data=data)
    campeonato_obj = campeonato.toDict()
    
    session.add(campeonato)
    session.commit()

    return jsonify({'campeonato': campeonato_obj })

@campeonato_routes.put('/campeonatos/<int:id>', responses={"200": AdicionarCampeonatoSchema})
def editar_campeonato(path: CampeonatoPath):
    """ Edita um campeonato existente no banco de dados.

    """
    campeonato_id = path.id
    session = Session()
    
    # editar campeonato específico do banco:

    campeonato = session.query(Campeonato).filter(Campeonato.id == campeonato_id).first()
    if not campeonato:
        error_msg = "Campeonato não encontrado na base :/"
        logger.warning(f"Erro ao buscar campeonato '{campeonato_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    campeonato.nome = request.form['nome']
    campeonato.cidade = request.form['cidade']
    data = date.fromisoformat(request.form['data'])
    campeonato.data = data
    session.commit()
    
    return jsonify({ 'campeonato': campeonato.toDict()})

@campeonato_routes.get('/campeonatos/<int:id>',  responses={"200": ListarCampeonatoIdSchema})
def listar_campeonatos_por_id(path: CampeonatoPath):
    """ Retorna campeonato específico cadastrados no banco de dados, de acordo com o ID especificado.
    """

    # listar campeonato específico do banco:
    campeonato_id = path.id

    session = Session()
    campeonato = session.query(Campeonato).filter(Campeonato.id == campeonato_id).first()

    if not campeonato:
        # se o campeonato não foi encontrado
        error_msg = "Campeonato não encontrado na base :/"
        logger.warning(f"Erro ao buscar campeonato '{campeonato_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    
    return jsonify({ 'campeonato': campeonato.toDict()})


@campeonato_routes.delete('/campeonatos/<int:id>', responses={"200": DeletarCampeonatoIdSchema})
def deletar_atleta(path: CampeonatoPath):
    """ Deleta um campeonato no banco de dados.

    """
    campeonato_id = path.id

    session = Session()
    # remover campeonato do db
    campeonato = session.query(Campeonato).filter(Campeonato.id == campeonato_id).first()

    if not campeonato:
        # se o campeonato não foi encontrado
        error_msg = "Evento não encontrado na base :/"
        logger.warning(f"Erro ao deletar campeonato '{campeonato_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    session.delete(campeonato)
    campeonato_obj = campeonato.toDict()
    session.commit()

    return jsonify({'campeonato': campeonato_obj})
from flask_openapi3 import Tag, APIBlueprint
from flask import jsonify, request
from model import Session
from model.atleta import Atleta
from schemas import ListarAtletasSchema, AdicionarAtletasSchema, FormAddAtletaSchema, ListarAtletaIdSchema, DeletarAtletaIdSchema
from logger import logger
from schemas.atleta import AtletaPath

atletas_tag = Tag(
    name='Atletas', description='Operações relacionadas a atletas')

atleta_routes = APIBlueprint('atletas', __name__, abp_tags=[atletas_tag])


@atleta_routes.get('/atletas',  responses={"200": ListarAtletasSchema})
def listar_atletas():
    """ Retorna uma listagem de atletas cadastrados no banco de dados.

    """
    # listar atletas do banco
    session = Session()
    atletas = session.query(Atleta).all()
    atletas_arr = []

    # foi criado um metodo toDict para serializar os dados
    for atleta in atletas:
        atletas_arr.append(atleta.toDict())

    # retorna erro se o array for vazio:
    if not atletas_arr:
        error_msg = "Nenhum Atleta foi  encontrado na base."
        logger.warning(f"Erro ao listar atletas:', {error_msg}")
        return {"mesage": error_msg}, 404

    return jsonify(atletas_arr)


@atleta_routes.get('/atletas/<int:id>',  responses={"200": ListarAtletaIdSchema})
def listar_atletas_por_id(path: AtletaPath):
    """ Retorna atleta específico cadastrados no banco de dados, de acordo com o ID especificado.
    """

    # listar atleta específico do banco:
    atleta_id = path.id
    session = Session()
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()

    if not atleta:
        # se o atleta não foi encontrado
        error_msg = "Atleta não encontrado na base :/"
        logger.warning(f"Erro ao buscar atleta '{atleta_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    return jsonify({'atleta': atleta.toDict()})


@atleta_routes.post('/atletas', responses={"200": AdicionarAtletasSchema})
def adicionar_atleta(form: FormAddAtletaSchema):
    """ Adiciona um atleta no banco de dados.

    """
    session = Session()
    atleta = Atleta(request.form['nome'], request.form['sexo'],
                    request.form['idade'], request.form['cidade'], request.form['categoria'])
    atleta_obj = atleta.toDict()
    session.add(atleta)

    session.commit()

    return jsonify({'atleta': atleta_obj})


@atleta_routes.put('/atletas/<int:id>', responses={"200": AdicionarAtletasSchema})
def editar_atleta(path: AtletaPath):
    """ Edita um atleta existente no banco de dados.

    """
    atleta_id = path.id

    session = Session()
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()
    if not atleta:
        # se o atleta não foi encontrado
        error_msg = "Atleta não encontrado na base :/"
        logger.warning(f"Erro ao buscar atleta '{atleta_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    atleta.nome = request.form['nome']
    atleta.sexo = request.form['sexo']
    atleta.idade = request.form['idade']
    atleta.cidade = request.form['cidade']
    atleta.categoria = request.form['categoria']

    atleta_obj = {"nome": request.form["nome"], "sexo": request.form["sexo"], "idade": request.form["idade"],
                  "cidade": request.form["cidade"], "categoria": request.form["categoria"]}

    session.commit()

    return jsonify({'atleta': atleta_obj})


@atleta_routes.delete('/atletas/<int:id>', responses={"200": DeletarAtletaIdSchema})
def deletar_atleta(path: AtletaPath):
    """ Deleta um atleta no banco de dados.

    """
    atleta_id = path.id

    session = Session()
    # remove athlete from database
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()

    if not atleta:
        # se o atleta não foi encontrado
        error_msg = "Atleta não encontrado na base :/"
        logger.warning(f"Erro ao deletar atleta '{atleta_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    session.delete(atleta)
    atleta_obj = atleta.toDict()
    session.commit()

    return jsonify({'atleta': atleta_obj})

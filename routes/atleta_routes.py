from flask_openapi3 import Tag, APIBlueprint
from flask import jsonify, request
from model import Session
from model.atleta import Atleta
from schemas import ListarAtletasSchema, AdicionarAtletasSchema, FormAddAtletaSchema, ListarAtletaIdSchema, DeletarAtletaIdSchema, ErrorEditarAtletaSchema, ErrorEditarAtletaIdSchema, ErrorDeletarAtletaSchema, ErrorAdicionarAtletaSchema, ErrorAtletaIdSchema
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

    return jsonify(atletas_arr)


@atleta_routes.get('/atletas/<int:id>',  responses={"200": ListarAtletaIdSchema, "404": ErrorAtletaIdSchema})
def listar_atletas_por_id(path: AtletaPath):
    """ Retorna atleta específico cadastrados no banco de dados, de acordo com o ID especificado.
    """

    # listar atleta específico do banco:
    atleta_id = path.id
    session = Session()
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()

    if not atleta:
        # se o atleta não foi encontrado
        error_msg = "Id Não Encontrado / inválido."
        logger.warning(f"Erro ao buscar atleta '{atleta_id}', {error_msg}")
        return {"mesage": error_msg, "error": "Erro ao buscar Atleta"}, 404 

    return jsonify({'atleta': atleta.toDict()})


@atleta_routes.post('/atletas', responses={"200": AdicionarAtletasSchema, "400": ErrorAdicionarAtletaSchema})
def adicionar_atleta(form: FormAddAtletaSchema):
    """ Adiciona um atleta no banco de dados.

    """
    session = Session()
    # valida se o form tem os dados esperados, caso nao tenha retorna erro 400:
    if not request.form['name'] or not request.form['sexo'] or not request.form['idade'] or not request.form['cidade'] or not request.form['categoria']:
        error_msg = "Formulário inválido"
        logger.warning(f"Erro ao adicionar atleta, {error_msg}")
        return {"mesage": error_msg, "error": "Erro ao adicionar atleta"}, 400

    atleta = Atleta(request.form['nome'], request.form['sexo'],
                    request.form['idade'], request.form['cidade'], request.form['categoria'])
    atleta_obj = atleta.toDict()
    session.add(atleta)

    session.commit()

    return jsonify({'atleta': atleta_obj})


@atleta_routes.put('/atletas/<int:id>', responses={"200": AdicionarAtletasSchema, "400": ErrorEditarAtletaSchema, "404": ErrorEditarAtletaIdSchema})
def editar_atleta(path: AtletaPath):
    """ Edita um atleta existente no banco de dados.

    """
    atleta_id = path.id

    session = Session()
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()
    if not atleta:
        # se o atleta não foi encontrado
        error_msg = "Id Não Encontrado / inválido."
        logger.warning(f"Erro ao buscar atleta '{atleta_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    
    # valida se o form tem os dados esperados, caso nao tenha retorna erro 400:
    if not request.form['name'] or not request.form['sexo'] or not request.form['idade'] or not request.form['cidade'] or not request.form['categoria']:
        error_msg = "Formulário inválido. Todos os campos são obrigatórios."
        logger.warning(f"Erro ao adicionar atleta, {error_msg}")
        return {"mesage": error_msg, "error": "Erro ao encontrar Atleta"}, 400

    atleta.nome = request.form['nome']
    atleta.sexo = request.form['sexo']
    atleta.idade = request.form['idade']
    atleta.cidade = request.form['cidade']
    atleta.categoria = request.form['categoria']

    atleta_obj = {"nome": request.form["nome"], "sexo": request.form["sexo"], "idade": request.form["idade"],
                  "cidade": request.form["cidade"], "categoria": request.form["categoria"]}

    session.commit()

    return jsonify({'atleta': atleta_obj})


@atleta_routes.delete('/atletas/<int:id>', responses={"200": DeletarAtletaIdSchema, "404": ErrorDeletarAtletaSchema})
def deletar_atleta(path: AtletaPath):
    """ Deleta um atleta no banco de dados.

    """
    atleta_id = path.id

    session = Session()
    # remove athlete from database
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()

    if not atleta:
        # se o atleta não foi encontrado
        error_msg = "Id Não Encontrado / inválido."
        logger.warning(f"Erro ao deletar atleta '{atleta_id}', {error_msg}")
        return {"mesage": error_msg, "error": "Erro ao deletar Atleta"}, 404

    session.delete(atleta)
    atleta_obj = atleta.toDict()
    session.commit()

    return jsonify({'atleta': atleta_obj})

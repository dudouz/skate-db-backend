from flask import Blueprint, jsonify, request
from model import Session
from model.atleta import Atleta

atleta_routes = Blueprint('atleta_routes', __name__)

@atleta_routes.route('/atletas', methods=['GET'])
def listar_atletas():
    # listar atletas do banco
    session = Session()
    atletas = session.query(Atleta).all()
    atletas_arr = []

    # foi criado um metodo toDict para serializar os dados
    for atleta in atletas:
        atletas_arr.append(atleta.toDict())

    return jsonify(atletas_arr)

@atleta_routes.route('/atletas', methods=['POST'])
def adicionar_atleta():
    session = Session()
    atleta = Atleta(request.form['nome'], request.form['sexo'], request.form['idade'], request.form['cidade'], request.form['categoria'])

    session.add(atleta)
    session.commit()

    return jsonify({'message': 'Sucesso ao adicionar atleta.', atleta: jsonify(atleta.toDict())})
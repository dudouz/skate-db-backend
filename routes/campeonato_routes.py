from flask import Blueprint, jsonify, request
from model import Session
from model.campeonato import Campeonato
from datetime import date

campeonato_routes = Blueprint('campeonato_routes', __name__)

@campeonato_routes.route('/campeonatos', methods=['GET'])
def listar_campeonatos():
    # listar campeonatos do banco
    session = Session()
    campeonatos = session.query(Campeonato).all()
    campeonatos_arr = []

    # foi criado um metodo toDict para serializar os dados
    for campeonato in campeonatos:
        campeonatos_arr.append(campeonato.toDict())

    return jsonify(campeonatos_arr)

@campeonato_routes.route('/campeonatos', methods=['POST'])
def adicionar_campeonato():
    session = Session()

    print(request.form['data'])
    # parse date from string
    data = date.fromisoformat(request.form['data'])

    campeonato = Campeonato(request.form['nome'], request.form['cidade'], data=data)

    session.add(campeonato)
    session.commit()

    return jsonify({'message': 'Sucesso ao adicionar campeonato.', })
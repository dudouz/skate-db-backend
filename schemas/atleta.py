from typing import List
from pydantic import BaseModel
from model.atleta import Atleta

class AtletaSchema(BaseModel):
    """ Define como um novo atleta a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "João"
    categoria: str = "Master"
    cidade: str = "São Paulo"
    sexo: str = "Masculino"
    idade: int = 30

class ListarAtletasSchema(BaseModel)
    """ Define como uma lista de atletas é retornada.
    """
    atletas: List[AtletaSchema]

def listaAtletas(atletas: List[Atleta]):
    """ Retorna uma lista de atletas
    """
    result = []
    for atleta in atletas:
        result.append({
            "nome": atleta.nome,
            "cidade": atleta.cidade,
            "categoria": atleta.categoria,
            "sexo": atleta.sexo,
            "idade": atleta.idade
        })
    return {"atletas": result}
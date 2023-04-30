from typing import List, AnyStr, Dict
from pydantic import BaseModel, Field
from model.atleta import Atleta

successMessage = "Sucesso ao adicionar atleta."
class AtletaSchema(BaseModel):
    """ Define como um novo atleta a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "João"
    categoria: str = "Master"
    cidade: str = "São Paulo"
    sexo: str = "Masculino"
    idade: int = 30

class ListarAtletasSchema(BaseModel):
    """ Define como uma lista de atletas é retornada.
    """
    atletas: List[AtletaSchema]


class ListarAtletaIdSchema(BaseModel):
    """ Define como uma lista de atletas é retornada.
    """
    id: str = "1"

class DeletarAtletaIdSchema(BaseModel):
    """ Define como uma lista de atletas é retornada.
    """
    id: str = "1"



class AdicionarAtletasSchema(BaseModel):
    """ Retorno de Sucesso ao adicionar o atleta.
    """

    atleta: AtletaSchema
class FormAddAtletaSchema(BaseModel):
    nome: str
    categoria: str
    cidade: str
    sexo: str
    idade: int

def lista_atletas(atletas: List[Atleta]):
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

class AtletaPath(BaseModel):
    id: int = Field(..., description='ID do atleta')
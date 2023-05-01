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
    atleta: AtletaSchema

class DeletarAtletaIdSchema(BaseModel):
    """ Define como uma lista de atletas é retornada.
    """
    atleta: AtletaSchema



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
class AtletaPath(BaseModel):
    id: int = Field(..., description='ID do atleta')


class ErrorAtletaIdSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao buscar Atleta."
    message: str = "Id Não Encontrado / inválido."
    code: int = 404

class ErrorAdicionarAtletaSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao adicionar Atleta."
    message: str = "Formulário inválido."
    code: int = 400

class ErrorDeletarAtletaSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao deletar Atleta."
    message: str = "Id Não Encontrado / inválido."
    code: int = 404


class ErrorEditarAtletaIdSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao editar Atleta."
    message: str = "Id Não Encontrado / inválido."
    code: int = 404

class ErrorEditarAtletaSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao editar Atleta."
    message: str = "Formulário inválido."
    code: int = 400

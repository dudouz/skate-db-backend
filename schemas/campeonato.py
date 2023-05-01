from datetime import date
from datetime import date, datetime
from typing import List
from pydantic import BaseModel, Field
from typing import List, AnyStr, Dict
from model.campeonato import Campeonato


date_format = '%Y-%m-%d'
placeholderDate = datetime.strptime('2024-06-06', date_format).date()

successMessage = "Sucesso ao adicionar campeonato."
class CampeonatoSchema(BaseModel):
    """ Define como um novo Campeonato a ser inserido deve ser representado
    """
    nome: str = "STU International"
    cidade: str = "São Paulo"
    data: date = placeholderDate
    id: int = 1

class ListarCampeonatosSchema(BaseModel):
    """" Define como uma lista de campeonatos é retornada.
    """
    campeonatos: List[CampeonatoSchema]

class ListarCampeonatoIdSchema(BaseModel):
    """ Define como uma lista de Campeonatos é retornada.
    """
    campeonato: CampeonatoSchema

class DeletarCampeonatoIdSchema(BaseModel):
    """ Define como uma lista de Campeonatos é retornada.
    """
    campeonato: CampeonatoSchema

class AdicionarCampeonatoSchema(BaseModel):
    """ Retorno de Sucesso ao adicionar o campoenoato.
    """
    campeonato: CampeonatoSchema
class FormAddCampeonatoSchema(BaseModel):
    nome: str
    data: date
    cidade: str

class CampeonatoPath(BaseModel):
    id: int = Field(..., description='ID do Campeonato')


class ErrorCampeonatoIdSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao buscar Campeonato."
    message: str = "Id Não Encontrado / inválido."
    code: int = 404


class ErrorAdicionarCampeonatoSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao adicionar campeonato."
    message: str = "Formulário inválido."
    code: int = 400

class ErrorDeletarCampeonatoSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao deletar campeonato."
    message: str = "Id Não Encontrado / inválido."
    code: int = 404


class ErrorEditarCampeonatoIdSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao editar campeonato."
    message: str = "Id Não Encontrado / inválido."
    code: int = 404

class ErrorEditarCampeonatoSchema(BaseModel):
    """ Define como um erro é retornado.
    """
    error: str = "Erro ao editar campeonato."
    message: str = "Formulário inválido."
    code: int = 400

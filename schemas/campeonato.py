from datetime import date
from typing import List
from pydantic import BaseModel

class CampeonatoSchema(BaseModel):
    """ Define como um novo Campeonato a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "STU International"
    cidade: str = "São Paulo"
    data = date.fromisoformat("2021-01-01")

class ListarCampeonatosSchema(BaseModel)
    """" Define como uma lista de campeonatos é retornada.
    """
    campeonatos: List[CampeonatoSchema]
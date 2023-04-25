from pydantic import BaseModel

class BateriaSchema(BaseModel):
    """ Define como uma nova bateria a ser inserida deve ser representada
    """
    id: int = 1
    tipo: str = "classificatoria"
    campeonato_id: int = 1

class ResultadoSchema(BaseModel):
    """ Define como um novo resultado a ser inserido deve ser representado
    """
    id: int = 1
    bateria_id: int = 1
    atleta_id: int = 1
    volta: int = 1
    pontuacao: int = 100

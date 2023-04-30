from pydantic import BaseModel

class BateriaSchema(BaseModel):
    """ Define como uma nova bateria a ser inserida deve ser representada
    """
    tipo: str = "classificatoria"
    campeonato_id: int = 1

class ResultadoSchema(BaseModel):
    """ Define como um novo resultado a ser inserido deve ser representado
    """
    bateria_id: int = 1
    atleta_id: int = 1
    volta: int = 1
    pontuacao: int = 100

from sqlalchemy import Column, Integer, String, Date, inspect
from sqlalchemy.orm import relationship
from model import Base

class Campeonato(Base):
    def __init__(self, nome, cidade, data):
        self.nome = nome
        self.cidade = cidade
        self.data = data
    
    __tablename__ = "campeonatos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cidade = Column(String)
    data = Column(Date)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

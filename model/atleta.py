from sqlalchemy import Column, Integer, String, Enum, inspect
from sqlalchemy.orm import relationship
from model import Base

class Atleta(Base):
    def __init__(self, nome, sexo, idade, cidade, categoria):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.cidade = cidade
        self.categoria = categoria

    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    categoria = Column(Enum("Mirim", "Amador", "Profissional", "Master", "Grand Master", "Legend", "Grand Legend"))
    cidade = Column(String)
    sexo = Column(Enum("Masculino", "Feminino"))
    idade = Column(Integer)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

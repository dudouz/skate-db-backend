from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from model import Base

class Bateria(Base):
    __tablename__ = "baterias"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum("classificatoria", "eliminatoria", "final"))
    campeonato_id = Column(Integer, ForeignKey("campeonatos.id"))
    campeonato = relationship("Campeonato", back_populates="baterias")
    resultados = relationship("Resultado", back_populates="bateria")

class Resultado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    bateria_id = Column(Integer, ForeignKey("baterias.id"))
    bateria = relationship("Bateria", back_populates="resultados")
    atleta_id = Column(Integer, ForeignKey("atletas.id"))
    atleta = relationship("Atleta", back_populates="resultados")
    volta = Column(Integer)
    pontuacao = Column(Integer)

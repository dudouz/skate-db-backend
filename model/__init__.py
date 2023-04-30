from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

# inicializando o db
from model.base import Base
from model.atleta import Atleta
from model.campeonato import Campeonato


# declarar url do db
db_url = 'sqlite:///database/skaters.sqlite3'

# cria a conexão com o db
engine = create_engine(db_url)

# instancia a sessão
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir ainda
if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas
Base.metadata.create_all(engine)

# adiciona uns atletas, caso nao existam
session = Session()
if session.query(Atleta).count() == 0:
    atletas = [
        Atleta(nome='Christian Hosoi', categoria='Profissional', idade=54, sexo='Masculino', cidade='Los Angeles'),
        Atleta(nome='Tony Hawk', categoria='Profissional', idade=53, sexo='Masculino', cidade='San Diego'),
        Atleta(nome='Steve Caballero', categoria='Profissional', idade=57, sexo='Masculino', cidade='San Jose'),
        Atleta(nome='Bucky Lasek', categoria='Profissional', idade=49, sexo='Masculino', cidade='Baltimore'),
        Atleta(nome='Lizzie Armanto', categoria='Profissional', idade=29, sexo='Feminino', cidade='Santa Monica'),
        Atleta(nome='Pedro Barros', categoria='Profissional', idade=26, sexo='Masculino', cidade='Florianópolis'),
        Atleta(nome='Nora Vasconcellos', categoria='Profissional', idade=28, sexo='Feminino', cidade='Los Angeles'),
        Atleta(nome='Brighton Zeuner', categoria='Profissional', idade=17, sexo='Feminino', cidade='Encinitas'),
    ]

    session.add_all(atletas)
    session.commit()

# adiciona um campeonato, caso nao exista
# data deve ser um date object

if session.query(Campeonato).count() == 0:
    campeonato = Campeonato(nome='Campeonato Brasileiro de Skate 2023', cidade='Criciúma', data=date(2023, 10, 10))
    session.add(campeonato)
    session.commit()
    session.close()

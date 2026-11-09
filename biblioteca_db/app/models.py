from sqlalchemy import Column ,Integer , String , Boolean, ForeignKey
from .database import Base

class Genero(Base):
    __tablename__="generos"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    nacionalidade = Column(String, nullable=True)

class Autor(Base):
    __tablename__="autores"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    nacionalidade = Column(String, nullable=True)

class Livro(Base):
    __tablename__="livros"
    id = Column(Integer, primary_key=True)
    titulos = Column(String, nullable=False)
    ano_publicacao = Column(Integer)
    disponivel = Column(Boolean, default=True)
    genero_id = Column(Integer, ForeignKey("generos.id"))
    autor_id = Column(Integer, ForeignKey("autores_id"))
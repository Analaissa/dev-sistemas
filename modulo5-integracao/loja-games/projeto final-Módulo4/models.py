from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

# # Colunas
class Plataforma(Base):
    __tablename__ = "plataformas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)
    

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(20), nullable=False)
    preco = Column(Float, nullable=False, default=0.0)
    plataforma_id = Column(Integer, ForeignKey("plataformas.id"), nullable=False)

class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True)
    nota = Column(Float, nullable=False)
    comentario = Column(String(300), nullable=False)
    jogo_id = Column(Integer, ForeignKey("jogos.id"), nullable=False)
    
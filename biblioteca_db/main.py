from app.database import engine, SessionLocal
from app import models 
from app.models import Genero,Autor,Livro

models.base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")

db = SessionLocal()
genero1 = models.Genero(nome="Romance")
genero2 = models.Genero(nome="Fantasia")
genero3 = models.Genero(nome="Mistério")

db.add_all([genero1, genero2, genero3])
db.commit()

autor1 = models.Autor(
nome="Machado de Assis",
nacionalidade="Brasileiro"
)

autor2 = models.Autor(
    nome="J.K.Rowling",
    nacionalidade="Britânico"
)

autor2 = models.Autor(
    nome="Agatha Christie",
    nacionalidade="Britânica"
)

db.add_all([autor1, autor2, autor3])
db.commit

livro1 = models.Livro(
    titulo="Dom Casmurro",
    ano_publicacao=1899,
    disponivel=True,
    genero_id=genero1.id,
    autor_id=autor1.id
)
livro2 = models.Livro(
    titulo="Harry potter e a pedra Filosofal",
    ano_publicacao=1997,
    disponivel=True,
    genero_id=genero2.id,
    autor_id=autor2.id
)
livro3 = models.Livro(
    titulo="O Assasinato no Expresso Oriente",
    ano_publicacao=1934,
    disponivel=True,
    genero_id=genero3.id,
    autor_id=autor3.id
)
livro4 = models.Livro(
    titulo="Memórias póstumas de Brás Cubas",
    ano_publicacao=1881,
    disponivel=True,
    genero_id=genero4.id,
    autor_id=autor4.id
)
livro5 = models.Livro(
    titulo="Harry potter e a câmara secreta"
    ano_publicacao=1998,
    disponivel=True,
    genero_id=genero5.id,
    autor_id=autor5.id
)

db.add_all([livro1,livro2, livro3, livro4, livro5])
db.commit()

print("Dados inseridos com sucesso!")

db.close()
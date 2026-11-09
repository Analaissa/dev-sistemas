from app.database import engine, Base
from app import models # import para registrar os modelos na base
from app.seed import popular_banco

# create_all: cria as tabelas que não existem ainda
# se a tabela já existe:não apaga, não muda nada
Base.metadata.create_all(bind=engine)
popular_banco()
print('pronto')
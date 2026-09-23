from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker ,DeclarativeBase

# URL do banco SQLite - vai criar o arquivo escola.db
DB_URL = 'sqlite:///./escola.db'
engine= create_engine (DB_URL,echo=True,connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

class Base(DeclarativeBase):
    pass
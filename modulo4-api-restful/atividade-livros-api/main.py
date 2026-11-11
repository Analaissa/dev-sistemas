from fastapi import FastAPI
from database import engine, Base
from router import router as livro_router
from tags import tags_metadata

Base.metadata.create_all(bind=engine)

app = FastAPI(
    tittle="API de Livros",
    description="CRUD com FastAPI + SQLAlchemy + SQLite",
    version="1.0.0", 
    openapi_tags=tags_metadata
)

app.include_router(livro_router)

@app.get('/')
def raiz():
    return {"status":"online", "docs":"/docs", "versao":"1.0.0"}
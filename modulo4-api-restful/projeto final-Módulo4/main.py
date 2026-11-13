from fastapi import FastAPI
from database import engine, Base
import models
from routers import plataforma, jogo, avaliacao

app = FastAPI(
    title="Loja de  game api",
    description="API para  gereciamento de jogos",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(plataforma.router)
app.include_router(jogo.router)
app.include_router(avaliacao.router)

@app.get("/")
def raiz():
    return {"mensagem": "API da loja de games funcionando!"}
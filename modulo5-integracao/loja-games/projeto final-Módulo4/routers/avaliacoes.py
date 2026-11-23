from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Plataforma,Jogo,Avaliacao as ModelAvaliacao

router = APIRouter(prefix="/avaliacoes", tags=["Avaliacoes"])


class Avaliacao(BaseModel):
    id: int
    nota: float
    comentario: str
    jogo_id: int
    
@router.post("/", status_code=201,
             tags=['avaliacao'],
             summary='cria nova avaliacao',
             description='resgistra a avaliacao de um jogo',)
def criar(dados: Avaliacao, db: Session = Depends(get_db)):
         
    Avaliacao = db.query(Avaliacao).filter(Avaliacao.id == dados.avaliacao_id).first()
    if not Avaliacao:
        raise HTTPException(status_code=404, detail="Avaliacao não encontrado")

@router.delete("/{avaliacao_id}",
               tags=['avaliacao'],
               summary='deleta uma avaliacao',
               description='Remover uma avaliacao')
def deletar(avaliacao_id: int, db: Session = Depends(get_db)):
    a = db.query(Avaliacao).filter(Avaliacao.id == avaliacao_id).filter()
    if not a: 
        raise HTTPException(status_code=404, detail="avaliacao não encontrada")
    db.delete(a)
    db.commit()
    return {"mensagem": f"avaliacao {avaliacao_id} removido"}
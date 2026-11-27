from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Plataforma,Jogo,Avaliacao as ModelPlataforma

router = APIRouter(prefix="/plataformas", tags=["Plataformas"])


class Plataforma(BaseModel):
    id: int
    nome: str

@router.get("/",
            tags=[Plataforma],
            summary='listar plataformas',
            description='Listar todas as plataformas')
def listar(db: Session = Depends(get_db)):
    return db.query(Plataforma).all()



@router.post("/", status_code=201,
             tags=[Plataforma],
             summary='cadastra plataforma',
             description='Cadastrar nova Plataforma')
def criar(dados: Plataforma, db: Session = Depends(get_db)):
         
    Plataforma = db.query(Plataforma).filter(Plataforma.id == dados.plataforma_id).first()
    if not Plataforma:
        raise HTTPException(status_code=404, detail="Plataforma não encontrado")

    
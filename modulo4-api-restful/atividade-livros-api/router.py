from fastapi import APIRouter, Depends, HTTPException
from  sqlalchemy.orm import Session
from typing import List
from  models import Livro
from schemas import LivroCreate,LivroResponse,LivroUpdate
from database import get_db


router = APIRouter(prefix='/livros', tags=['livro'])

@router.get("/", response_model=List[LivroResponse])
def listar_livros(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return db.query(Livro). filter(Livro.disponivel == True).offset(skip).limit(limit).all()


@router.get('/{livro_id}', response_model=LivroResponse)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(livro).filter(livro.id == livro_id).first()
    if not livro or not livro.disponivel:
        raise HTTPException(status_code=404, detail=f"{livro_id}Livro não encontrado")
    return livro

@router.post('/', response_model=LivroResponse, status_code=201)
def criar(dados: LivroCreate, db: Session = Depends(get_db)):
    livro = Livro(**dados.model_dump())
    db.add(livro); db.commit(); db.refresh(livro)
    return livro
   
@router.patch('/{livro_id}', response_model=LivroResponse)
def atualizar(livro_id: int, dados: LivroUpdate, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro: raise HTTPException(404, 'Livro não encontrado')
    for campo, valor in dados.model_dump(exclude_none=True).items():
        setattr(livro, campo, valor)
    db.commit(); db.refresh(livro)
    return livro


@router.delete('/{livro_id}')
def remover(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro: raise HTTPException(404, 'Livro não encontrado')
    livro.disponivel = False
    db.commit()
    return {'mensagem': f'Livro {livro_id} removido'}

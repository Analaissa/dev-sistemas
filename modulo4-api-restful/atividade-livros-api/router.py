from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from models import Livro
from schemas import LivroCreate, LivroPatch, LivroResponse
from tags import tags_metadata
router = APIRouter(prefix='/livros', tags=['Livros'])

@router.get('/',
            tags=['Livros'],
            summary='Listar todos os livros',
            responses={
                200: {'descreption':'lista de livros retornada com sucesso'},
            })

def listar(db: Session = Depends(get_db)):
    return db.query(Livro).filter(Livro.disponivel == True).all()

@router.get('/{livro_id}',response_model=LivroResponse,
            tags=['Livro'],
            summary='Buscar livro por id',
            responses={
               200: {'description': 'Livro encontrado'},
               404: {'descrption': 'Livro não encontrado'}
            })

def buscar(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro: raise HTTPException(404, 'Livro não encontrado')
    return livro

@router.post('/', response_model=LivroResponse, 
             status_code=201,
             tags=['Livros'],
             summary='Cadastrar novo livro',
             responses={
                 201: {'description': 'Livro criado'},
                 400: {'description': 'Dados inválidos'}
             })
def criar(dados: LivroCreate, db: Session = Depends(get_db)):
    livro = Livro(**dados.model_dump())
    db.add(livro); db.commit(); db.refresh(livro)
    return livro

@router.patch('/{livro_id}', response_model=LivroResponse,
              tags=['Livros'],
              summary='Atualizar livro',
              response={
                  200: {'description': 'Atualizado livro'},
                  404: {'descritpion': 'Não encontrado'}
              })

def atualizar(livro_id: int, dados: LivroPatch, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro: raise HTTPException(404, 'Livro não encontrado')
    for campo, valor in dados.model_dump(exclude_none=True).items():
        setattr(livro, campo, valor)
    db.commit(); db.refresh(livro)
    return livro

@router.delete('/{livro_id}',
               tags=['Livros'],
               summary='Excluir livro',
               responses={
                   204: {'description': 'Não encontrado'}
               })
def remover(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro: raise HTTPException(404, 'Livro não encontrado')
    livro.disponivel = False
    db.commit()
    return {'mensagem': f'Livro {livro_id} removido'}

# Filtro por título
@router.get('/buscar/', response_model=List[LivroResponse],
            tags=['Livros'],
            summary='Filtrar livros por título',
            responses={
                200: {'description': 'Lista de livros filtrados retornada'},
            })
def buscar_titulo(titulo: str, db: Session = Depends(get_db)):
    return db.query(Livro).filter(Livro.titulo.ilike(f'%{titulo}%')).filter(Livro.disponivel == True).all()
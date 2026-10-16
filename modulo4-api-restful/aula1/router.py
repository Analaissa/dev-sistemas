from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import produto
from schemas import ProdutoCreate, ProdutoPatch, ProdutoResponse

# APIRouter agrupa os endpoints - registramos no main.py
router = APIRouter(prefix='/produtos', tags=['produto'])

# GET /produtos - Lista todos os produtos ativos
# response_model=List[ProdutoResponse] - fasAPI formata a saída
# skip elimit - páginação simples
@router.get('/', response_model=List[ProdutoResponse])
def listar_produtos(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return db.query(produto).filter(produto.ativo == True).offset(skip).limit(limit).all()


# GET / produtos/ (id) - Busca produto pelo ID
@router.get('/{produto_id}' , response_model=ProdutoResponse)
def buscar_produto(produto_id: int, db:Session = Depends(get_db)):
    produto = db.query(produto).filter(produto.id == produto_id).first()
    if not produto or not produto.ativo:
        raise HTTPException(status_code=404, detail=f'produto {produto_id} não encontrado')
    return produto

# POST /produtos - Criar novo produto
@router.post('/', response_model=ProdutoResponse, status_code=201)
def criar_produto(dados: ProdutoCreate, db: Session = Depends(get_db)):
    produto= produto(  # cria o objeto em python
        nome = dados.nome,
        preco = dados.preco,
        estoque = dados.estoque,
    )
    db.add(produto)      # enfileira o INSERT
    db.commit()          # executa no banco
    db.refresh(produto)  # atualiza o objeto com id e criando_em no banco
    return produto



# PUT /produtos/(id) - Substitui o produto inteiro
@router.put('/{produto_id}', response_model=ProdutoResponse)
def susbtituir_produto(produto_id: int, dados: ProdutoCreate, db: Session = Depends(get_db)):
  produto = db.query(produto).filter(produto.id == produto.id).first()
  if not produto or not produto.ativo:
      raise HTTPException(status_code=404, details='Não Encontrado')
  produto.nome = dados.nome
  produto.preco = dados.preco
  produto.estoque = dados.estoque
  db.commit()
  db.refresh(produto)
  return produto


# PACTCH /produtos/(id) - ATualiaza só os campos enviados
@router.patch('/{produto_id}', response_model=ProdutoResponse)
def atualiazar_produto(produto_id: int, dados: ProdutoPatch, db: Session = Depends(get_db)):
    produto = db.query(produto).filter(produto_id == produto_id).first()
    if not produto or not produto.ativo:
        raise HTTPException(status_code=404, detail='Não Encontrado')
    if dados.nome is not None: produto.nome = dados.nome
    if dados.preco is not None: produto.preco = dados.preco
    if dados.estoque is not None: produto.estoque = dados.estoque
    db.commit()
    db.refresh(produto)
    return produto


# DELETE /produtos/(id) - soft delete (marca ativo=False)
@router.delete('/{produto_id}')
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(produto).filter(produto.id == produto_id).first()
    if not produto or not produto.ativo:
        raise HTTPException(status_code=404, detail='Não Encontrado')
    produto.ativo = False
    db.commit()
    return {'mensagem': f'produto {produto_id} removido com sucesso'}
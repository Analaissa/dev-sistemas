from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import get_db
from models import Plataforma, Jogo, Avaliacao as ModelJogo

router = APIRouter(prefix="/jogos", tags=["Jogos"])


class JogoCreate(BaseModel):
    id: int
    titulo: str
    genero:str
    preco: float
    plataforma_id: int
   
@app.get('/jogos',
tags=['jogos'],
summary='Listar todas de jogos',
description='Retornar a lista completa de jogos (acesso pública)',
responses={
    200: {'description': 'lista de  jogos retornada com sucesso'},
    })

def listar(): 
    return Jogo

@app.get('/jogo/{jogo_id}')
def buscar(jogo_id: int): return achar_Jogo(Jogo_id)

@app.post('/jogos', 
        status_code=201,
        tags=['Jogo'],
        summary='Criar novo jogo',
        description='Criar uma novo jogo. qualquer usuario',
        responses={
            201: {'description': 'jogo criada com sucesso'},
            404: {'description': 'Não autenticado'},
        })

def criar(dados: JogoCreate,
        id: int = Depends(get_db)):
    global proximo_id_jogo
    nova = {'id': proximo_id_jogo,
            'titulo': dados.titulo,
            'genero': dados.genero,
            'preco': dados.preco
    }
    Jogo.append(nova)
    proximo_id_jogo += 1
    return nova

@app.patch('/jogos/{jogo_id}',
           tags=['jogos'],
           summary='Atualizar jogo',
           description='Atualiza parcialmente do dados de um jogo existente',
           responses={
               200: {'description': 'Jogo atualizada com sucesso'},
               401: {'description':'Não autenticado'},
               404: {'description': 'Jogo não encontrada'},
           })
def atualizar(jogo_id: int, dados: JogoPatch, id: str = Depends(get_db)):
    t = achar_jogo(Jogo_id)
    if dados.titulo    is not None: t['titulo']    = dados.titulo
    if dados.genero is not None: t['genero'] = dados.genero
    if dados.preco is not None: t['preco'] = dados.preco
    return t

@app.delete('/jogos/{jogo_id}',
            tags=['Jogo'],
            summary='Remover jogo()',
            description='Remove um jogo existente do sistema',
            responses={
                200: {'description': 'Jogo removido com sucesso'},
                401: {'description': 'Não autenticado'},
                400: {'description': 'Jogo não encontrada'},
            })
def remover(Jogo_id: int, id: str = Depends(get_db)):
    global Jogo
    achar_jogo(Jogo_id)
    jogos = [t for t in jogos if t['id'] != jogos_id]
    return {'mensagem': f'jogos {Jogo_id} removida'}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional
from fastapi import Response

app = FastAPI(title='API de Cadastro - SENAI', version='0.2.0')

# Modelo Pydantic: define a estrutura e os tipos
class Usuario(BaseModel):
    nome: str
    email: str
    cargo: str
    ativo: bool = True # valor padrão
    salario: Optional[float] = None # campo opcional
# Adicionar dentro da classe Usuario, após o validaor de cargo

@field_validator('') # qual campo vamos validar?
@classmethod
def validar_salario(cls, v):
  if v is None:  # se não enviou salário, deixa passar
      return v
  if v <= 0:  # qual comparação bloqueia negativo e zero?
   raise ValueError('salário inválido') # escreva uma mensagem de erro
  return v
  
@field_validator('nome')
@classmethod
def validar_nome(cls, v):
        v = v.strip()
        if len(v) < 3:
            raise ValueError('Nome deve ter pelo menos 3 caracteres')
        return v.title()

# Modelo de resposta: icluir o ID gerado pelo servidor
class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str
    ativo: bool
    salario: Optional[float] = None

usuarios_db: list[UsuarioResposta] = [
    UsuarioResposta(id=1, nome='Celina Souza', email='celina@email.com', cargo='Design', ativo=True, salario=3800.0),
    UsuarioResposta(id=2, nome='Daniele Santos', email='daniele@email.com', cargo='QA', ativo=True, salario=3200.0),
    UsuarioResposta(id=3, nome='Ana Laissa', email='ana@email.com', cargo='Dev', ativo=True, salario=4500.0),
    UsuarioResposta(id=4, nome='Diana', email='diana@email.com', cargo='Product manager', ativo=True, salario=3900.0),
]
proximo_id = 5

# GET /usuarios - Lista todos os usuários
@app.get('/usuarios', response_model=list[UsuarioResposta])
def listar_usuario():
    return usuarios_db
# Rota que retorna só os usuário ativos
@app.get('/usuario/ativos', response_model=list[UsuarioResposta]) # qual modelo de resposta?
def listar_ativos():
    return [u for u in usuarios_db if u.ativo == True] # qual campo? qual valor?

# Rota que filtra por cargo
@app.get('/usuario/cargo/{cargo}', response_model=list[UsuarioResposta]) # nome do parãmetro
def listar_por_cargo(cargo: str):
    return [u for u in usuarios_db if u.cargo.lower()== cargo.lower()]

# Rota de informações
@app.get('/info', tags=['Geral']) # qual tag? use 'Geral'
def info():
    total = len(usuarios_db)  # qual função conta elementos de uma lista?
    ativos = len([u for u in usuarios_db if u.ativo==True]) # filtrar os ativos
    return{
        'total_usuario': total,
        'usuario_ativo': ativos,
        'cargos_aceitos': ['Desenvolvedor', 'Designer', 'QA', 'Product manager'],
    }
# GET - busca pelo id
@app.get('/usuarios/{usuario_id}', response_model=UsuarioResposta) 
def buscar_usuario(usuario_id: int): 
    for usuario in usuarios_db: 
        if usuario.id == usuario_id: 
            return usuario 
    raise HTTPException(status_code=404, detail='Usuário não encontrado') 

# POST - Cria um novo usuário
@app.post('/usuarios', response_model=UsuarioResposta, status_code=201)
def criar_usuario(dados: Usuario):
    global proximo_id
    #Verificar e-mail duplicado
    for u in usuarios_db:
        if u.email == dados.email:
            raise HTTPException(400, 'E-mail já cadastrado')
    novo = UsuarioResposta(id=proximo_id, **dados.model_dump())
    usuarios_db.append(novo)
    proximo_id += 1
    return novo

# PUT - Substitui o usuário inteiro
@app.put('/usuarios/{usuario_id}', response_model=UsuarioResposta) 
def atualizar_usuario(usuario_id: int, dados: Usuario): 
    for i, u in enumerate(usuarios_db): 
        if u.id == usuario_id: 
            atualizado = UsuarioResposta(id=usuario_id, **dados.model_dump()) 
            usuarios_db[i] = atualizado 
            return atualizado 
    raise HTTPException(404, 'Usuário não encontrado')

# DELETE - Deleta um usuário
@app.delete('/usuarios/{usuario_id}', status_code=204)
def deletar_usuario(usuario_id: int):
    for i, u in enumerate(usuarios_db):
        if u.id == usuario_id:
            usuarios_db.pop(i)
            return Response(status_code=204)
    raise HTTPException(404, 'Usuário não encontrado')
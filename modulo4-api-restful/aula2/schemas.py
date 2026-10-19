from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime

class UsuarioCreate(BaseModel):
    nome:str = Field(...,
    min_length=2,
    max_length=100,
    description='Nome completo do usuário')
    
    email: EmailStr
    senha:str = Field(...,min_length=8, description='Mínimo 8 caracteres')
#@filed_validator valida o campo 'nome' antes de salvar
# se a validação falhar: raise ValueError com a mensagem de erro
# Se passar: return valor (o valor é validado)
    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls, valor:str) -> str:
        if any(char.isdigit() for char in valor):
         raise ValueError('Nome não pode conter números')
        if not valor.strip():
            raise ValueError('Nome não pode ser só espaços')
        return valor.strip()

    @field_validator('senha')
    @classmethod
    def senha_deve_ter_letra_e_numeros(cls, valor:str) -> str:
        tem_letra = any(caracter.isalpha() for caracter in valor)
        tem_numero = any(caracter.isdigit() for caracter in valor)
        if not tem_letra or not tem_numero:
            raise ValueError('Senha deve conter letras e números')
        return valor
# UsuarioPatch - todos os campos são opcionais
# O usuario envia só o que mudou
class UsuarioPatch(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_lenght=100)
    email: Optional[EmailStr] = None

    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls, valor):
        if valor and any(char.isdigit() for char in valor):
            raise ValueError('Nome não pode conter números')
        return valor.strip() if valor else valor
  
# 3. usuarioResponse - RESPOSTA (o que a API retorna)
class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool
    criado_em:datetime

    class config:
        from_attributes = True

class ErroResponse(BaseModel):
    erro: str
    detalhe: Optional[str] = None

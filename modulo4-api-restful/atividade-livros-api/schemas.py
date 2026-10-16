from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class LivroCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=200)
    autor: str = Field(..., min_length=2, max_length=150)
    ano_publicacao: Optional[int] = None
    disponivel: bool = True

class LivroUpdate(BaseModel):
    tiutlo: Optional[str] = Field(None, min_length=2, max_length=200)
    autor: Optional[str] = Field(None, min_length=2, max_length=150)
    ano_publicacao: Optional[int] = None
    disponivel: Optional[bool] = None

class LivroResponse(BaseModel):
    id: int
    titulo: str
    ano_publicacao: Optional[int]
    disponivel: bool
    criado_em: datetime

class config:
    from_attributes = True
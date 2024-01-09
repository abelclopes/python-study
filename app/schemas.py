from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class ProdutoSchema(BaseModel):
    nome: str
    descricao: str
    preco: float
    is_active: bool

class Produto(ProdutoSchema):
    id: str
    
        


class PedidoSchema(BaseModel):
    id: int
    items: list[Produto]
    status: str


class UsuarioBase(BaseModel):
    username: str
    email: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

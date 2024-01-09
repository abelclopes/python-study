# app/routers/usuarios.py

from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import UsuarioCreate, Usuario

router = APIRouter()

# Simulando um banco de dados com uma lista
usuarios_db = []

@router.post("/usuarios/", response_model=Usuario)
async def criar_usuario(usuario: UsuarioCreate):
    novo_usuario = usuario.dict()
    novo_usuario["id"] = len(usuarios_db) + 1
    novo_usuario["is_active"] = True
    usuarios_db.append(novo_usuario)
    return novo_usuario

@router.get("/usuarios/", response_model=List[Usuario])
async def ler_usuarios():
    return usuarios_db

@router.get("/usuarios/{usuario_id}", response_model=Usuario)
async def ler_usuario(usuario_id: int):
    usuario = next((u for u in usuarios_db if u["id"] == usuario_id), None)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.put("/usuarios/{usuario_id}", response_model=Usuario)
async def atualizar_usuario(usuario_id: int, usuario: UsuarioCreate):
    index = next((i for i, u in enumerate(usuarios_db) if u["id"] == usuario_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    update_data = usuario.dict()
    update_data["id"] = usuario_id
    update_data["is_active"] = usuarios_db[index]["is_active"]
    usuarios_db[index] = update_data
    return update_data

@router.delete("/usuarios/{usuario_id}", response_model=Usuario)
async def deletar_usuario(usuario_id: int):
    index = next((i for i, u in enumerate(usuarios_db) if u["id"] == usuario_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario = usuarios_db.pop(index)
    return usuario

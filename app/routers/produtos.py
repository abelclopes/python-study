# app/routers/produtos.py

from bson import ObjectId
from fastapi import APIRouter, HTTPException
from typing import List
from fastapi import APIRouter, HTTPException
from app.schemas import ProdutoSchema,Produto
from app.database import get_database
from bson import ObjectId

router = APIRouter()

@router.post("/produtos/", response_model=ProdutoSchema)
async def criar_produto(produto: ProdutoSchema):
    db = get_database()
    novo_produto = await db["produtos"].insert_one(produto.dict())
    created_produto = await db["produtos"].find_one({"_id": novo_produto.inserted_id})
    return Produto(**created_produto, id=str(created_produto["_id"]))

@router.get("/produtos/", response_model=List[Produto])
async def ler_produtos():
    db = get_database()
    produtos = []
    async for produto in db["produtos"].find():
        produtos.append(Produto(**produto, id=str(produto["_id"])))
    return produtos

@router.get("/produtos/{produto_id}", response_model=ProdutoSchema)
async def ler_produto(produto_id: str):
    db = get_database()
    produto = await db["produtos"].find_one({"_id": ObjectId(produto_id)})
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return Produto(**produto, id=str(produto["_id"]))

@router.put("/produtos/{produto_id}", response_model=Produto)
async def atualizar_produto(produto_id: str, produto: ProdutoSchema):
    db = get_database()
    update_result = await db["produtos"].update_one(
        {"_id": ObjectId(produto_id)}, {"$set": produto.dict()}
    )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {**produto.dict(), "id": produto_id}

@router.delete("/produtos/{produto_id}", response_model=Produto)
async def deletar_produto(produto_id: str):
    db = get_database()
    delete_result = await db["produtos"].delete_one({"_id": ObjectId(produto_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"id": produto_id}

# Dentro do seu arquivo de rotas, por exemplo, routes.py

from fastapi import APIRouter, HTTPException
from app.schemas import PedidoSchema
from app.database import get_database
from bson import ObjectId

router = APIRouter()

@router.get("/pedidos/", response_model=list[PedidoSchema])
async def buscar_todos_pedidos():
    db = get_database()
    pedidos = await db["pedidos"].find().to_list(length=100)  # Ajuste 'length' conforme necessário
    return pedidos

@router.post("/pedidos/", response_model=PedidoSchema)
async def criar_pedido(pedido: PedidoSchema):
    db = get_database()
    novo_pedido = await db["pedidos"].insert_one(pedido.dict())
    created_pedido = await db["pedidos"].find_one({"_id": novo_pedido.inserted_id})
    return created_pedido

@router.get("/pedidos/{pedido_id}", response_model=PedidoSchema)
async def buscar_pedido(pedido_id: str):
    db = get_database()
    pedido = await db["pedidos"].find_one({"id": pedido_id})
    if pedido:
        return pedido
    raise HTTPException(status_code=404, detail=f"Pedido {pedido_id} não encontrado")


# @router.post("/items/")
# async def create_item(item: ItemSchema):
#     db = get_database()
#     new_item = await db["colecao"].insert_one(item.dict())
#     created_item = await db["colecao"].find_one({"_id": new_item.inserted_id})
#     return created_item
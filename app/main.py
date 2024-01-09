# app/main.py
from fastapi import FastAPI
from app.routers import pedidos, usuarios, produtos
from app.database import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(pedidos.router)
app.include_router(usuarios.router)
app.include_router(produtos.router)

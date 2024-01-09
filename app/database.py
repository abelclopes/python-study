from motor.motor_asyncio import AsyncIOMotorClient

class DataBase:
    client: AsyncIOMotorClient = None

db = DataBase()

def get_database() -> AsyncIOMotorClient:
    return db.client

async def connect_to_mongo():
    db.client = AsyncIOMotorClient("mongodb://root:exemploSenha@localhost:27017/")
    db.client = db.client['mclivery']

async def close_mongo_connection():
    db.client.close()

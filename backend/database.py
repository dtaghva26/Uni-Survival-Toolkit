from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from models.user import User
# from models.chore import Chore
# from models.shopping import ShoppingItem
from models.households import Household

async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["UniSurvival"]

    await init_beanie(
        database=db,
        # TODO ADD OTHER MODELS
        document_models=[User, Household]  
        # TODO add more 
    )
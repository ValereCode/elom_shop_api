from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from dotenv import  load_dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models.user import User
# from .models.cart import Cart
# from .models.category import Category
# from .models.order import Order
# from .models.payment import Payment
# from .models.product import Product
# from .models.review import Review
from .routes import task_routes

load_dotenv()

@asynccontextmanager
async def connect_database(app: FastAPI):
    # Create Motor client
    client = AsyncIOMotorClient(os.getenv("DATABASE_URL"))

    # Initialize beanie with documents classes and a database
    await init_beanie(
        database=client.db_name,
        document_models=[User] # , Product, Category, Cart, Order, Payment, Review
    )
    print("Startup complete")
    yield
    print("Shutdown complete")

app = FastAPI(lifespan=connect_database,docs_url="/")

origins = ["*"]

app.include_router(task_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
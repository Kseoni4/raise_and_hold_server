from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home():
   return {"data": "Hello World"}

@app.post("/users")
async def add_user(user: User):
   return {"user":user}

@app.get("/basic-auth")
async def auth_by_basic(
    credentials
):
    pass
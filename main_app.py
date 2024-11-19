from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from repository import UserRepository
from scheme import UserModel, UserEntity

@asynccontextmanager
async def lifespan_(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")

app = FastAPI(lifespan=lifespan_)

@app.get('/cat')
def get_cat():
    return {'cat_name1':'Mark',
            'cat_name2':'Trish'}

@app.get('/users')
async def get_all_users():
    users = await UserRepository.get_users()
    return users

@app.post('/users')
async def add_new_user(user: UserModel):
    await UserRepository.add_user(user)
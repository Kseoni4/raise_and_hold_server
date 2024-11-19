from database import UserOrm, new_session
from sqlalchemy import select
from scheme import UserEntity, UserModel


class UserRepository:

    @classmethod
    async def add_user(cls, user: UserModel) -> int:
        async with new_session() as session:
            data = user.model_dump() # преобразование из UserModel в словарь
            new_user = UserOrm(**data)
            session.add(new_user)
            await session.flush()
            await session.commit()
            return new_user.id
    
    @classmethod
    async def get_users(cls) -> list[UserEntity]:
        async with new_session() as session:
            query = select(UserOrm) # создаёт запрос SELECT * FROM users
            result = await session.execute(query) # выполняет запрос
            user_model = result.scalars().all() # возвращает список найденных пользователей
            users = [UserEntity.model_validate(user_model) for user_model in user_model]
            return users
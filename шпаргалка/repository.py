from database import UserOrm, new_session
from schemas import User, UserEntity
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_user(cls, user: UserEntity) -> int:
        async with new_session() as session:
            data = user.model_dump()
            new_user = UserOrm(**data)
            session.add(new_user)
            await session.flush()
            await session.commit()
            return new_user.id

    @classmethod
    async def get_users(cls) -> list[UserEntity]:
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            user_model = result.scalars().all()
            users = [User.model_validate(user_model) for user_model in user_model]
            return users
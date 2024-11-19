from pydantic import BaseModel

class User(BaseModel):
   username: str
   password: str


class UserEntity(User):
   id: int
   model_config = ConfigDict(from_attributes=True)
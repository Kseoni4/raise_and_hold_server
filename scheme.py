from pydantic import BaseModel, ConfigDict

class UserModel(BaseModel):
    username: str
    password: str

class UserEntity(UserModel):
    id: int
    model_config = ConfigDict(from_attributes=True)
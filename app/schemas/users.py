from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool = True

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

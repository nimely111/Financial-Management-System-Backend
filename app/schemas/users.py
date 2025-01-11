from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserBase(BaseModel):
    firstname: str
    lastname: str | None = None
    role: str
    password: str
    username: str
    profilePicture: str
    dob: str
    nationality: str
    contactPhone: str
    contactEmail: EmailStr  # Email validation via Pydantic
    gender: str
    address: str
    city_name: str
    about_user: str | None = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

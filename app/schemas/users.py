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
    firstname: str
    lastname: str
    role: str
    password: str
    username: str
    profilePicture: str
    dob: str
    nationality:str
    contactPhone: str
    contactEmail: EmailStr
    gender: str
    address: str
    city_name: str
    about_user: str | None = None

class UserUpdate(UserBase):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    role: Optional[str] = None
    password: Optional[str] = None
    username: Optional[str] = None
    profilePicture: Optional[str] = None
    dob: Optional[str] = None
    nationality:Optional[str] = None
    contactPhone: Optional[str] = None
    contactEmail: Optional[EmailStr] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    city_name: Optional[str] = None
    about_user: Optional[str] = None 

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

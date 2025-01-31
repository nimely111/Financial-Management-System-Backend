from pydantic import BaseModel, EmailStr
from typing import Optional, List


class TransactionResponse(BaseModel):
    id: int
    savings_amount: str
    savings_type: str
    savings_currency: str
    description: Optional[str]
    date: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    firstname: str
    lastname: Optional[str] = None
    role: str
    password: str
    username: str
    profile_picture: str
    dob: str
    nationality: str
    contact_phone: str
    contact_email: str  
    gender: str
    address: str
    city_name: str
    about_user: Optional[str] = None


class UserCreate(UserBase):
    transactions: Optional[List[TransactionResponse]] = []  # Making it optional


class UserUpdate(UserBase):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    role: Optional[str] = None
    password: Optional[str] = None
    username: Optional[str] = None
    profile_picture: Optional[str] = None
    dob: Optional[str] = None
    nationality: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    city_name: Optional[str] = None
    about_user: Optional[str] = None
    transactions: Optional[List[TransactionResponse]] = []


class UserResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    address: str
    city_name: Optional[str] = None
    profile_picture: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    transactions: List[TransactionResponse] = []  # Ensuring transactions appear in response

    class Config:
        orm_mode = True

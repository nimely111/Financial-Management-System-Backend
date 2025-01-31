from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserBase(BaseModel):
    firstname: str
    lastname: str | None = None
    role: str
    password: str
    username: str
    profile_picture: str
    dob: str
    nationality: str
    contact_phone: str
    contact_email: EmailStr  # Email validation via Pydantic
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
    profile_picture: str
    dob: str
    nationality:str
    contact_phone: str
    contact_email: EmailStr
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
    profile_picture: Optional[str] = None
    dob: Optional[str] = None
    nationality:Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[EmailStr] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    city_name: Optional[str] = None
    about_user: Optional[str] = None 
    
class TransactionResponse(BaseModel):
    id: int
    savings_amount: str
    savings_type: str
    savings_currency: str
    description: Optional[str]
    date: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    address: str
    city_name: Optional[str] = None
    profile_picture: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[EmailStr] = None
    transactions: List[TransactionResponse]  # Include nested transactions

    class Config:
        orm_mode = True
from pydantic import BaseModel
from typing import Optional

# Base Transaction Model
class TransactionBase(BaseModel):
    savings_amount: float
    savings_type: str
    savings_currency: str
    description: Optional[str] = None
    date: str

# Model for Transaction Creation
class TransactionCreate(TransactionBase):
    user_id: int

# Model for Transaction Update
class TransactionUpdate(BaseModel):
    savings_amount: Optional[float] = None
    savings_type: Optional[str] = None
    savings_currency: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None

# Model for Transaction Response
class TransactionResponse(BaseModel):
    id: int
    savings_amount: float
    savings_type: str
    savings_currency: str
    description: Optional[str]
    date: str
    user_id: int  # Include user_id for relational purposes

    class Config:
        orm_mode = True
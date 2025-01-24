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
class TransactionResponse(TransactionBase):
    id: int
    user_id: int
    type: str
    saving: float
    currency: str

    class Config:
        orm_mode = True

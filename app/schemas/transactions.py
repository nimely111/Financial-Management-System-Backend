from pydantic import BaseModel
from typing import Optional

# Base Transaction Model
class TransactionBase(BaseModel):
    amount: float
    description: Optional[str] = None
    date: str
    savings_amount: float
    savings_type: str
    savings_currency: str

# Model for Transaction Creation
class TransactionCreate(TransactionBase):
    user_id: int  # Required field for associating a transaction with a user

# Model for Transaction Update
class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    date: Optional[str] = None
    savings_amount: Optional[float] = None
    savings_type: Optional[str] = None
    savings_currency: Optional[str] = None
    user_id: Optional[int] = None

# Model for Transaction Response
class TransactionResponse(TransactionBase):
    id: int  # Primary key of the transaction
    user_id: int  # Associated user ID

    class Config:
        orm_mode = True
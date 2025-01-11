from fastapi import FastAPI
from db.db_setup import get_db
from models.models import User, Transaction
from schemas.users import (
    UserBase,
    UserCreate,
    UserResponse,
    UserUpdate
)

from schemas.transactions import (
    TransactionBase,
    TransactionCreate,
    TransactionResponse,
    TransactionUpdate
    )

app = FastAPI(title="Try and See Financial Management system Backend", docs_url="/docs")

@app.get("/")
async def read_root():
    return {"message": "Hello, There!"}
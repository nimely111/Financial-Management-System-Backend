from fastapi import APIRouter, Depends, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db_setup import get_db
from crud.transactions import get_transactions, get_transaction, create_transaction, update_transaction, delete_transaction
from schemas.transactions import TransactionCreate, TransactionUpdate, TransactionResponse

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.post("/transactions/", response_model=TransactionResponse)
def create_new_transaction(
    transaction: TransactionCreate,
    user_id: int,
    db: Session = Depends(get_db)
):
    return create_transaction(db=db, transaction=transaction, user_id=user_id)
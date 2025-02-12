from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db_setup import get_db
from crud.transactions import (
    create_transaction, get_transactions, get_transaction_by_id, update_transaction, delete_transaction
)
from schemas.transactions import TransactionCreate, TransactionUpdate, TransactionResponse

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# Create a New Transaction
@router.post("/", response_model=TransactionResponse)
def create_new_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return create_transaction(db=db, transaction=transaction)

# Read All Transactions
@router.get("/", response_model=list[TransactionResponse])
def read_all_transactions(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    transactions = get_transactions(db=db, skip=skip, limit=limit)
    return transactions

# Read a Single Transaction by ID
@router.get("/{transaction_id}", response_model=TransactionResponse)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction_by_id(db=db, transaction_id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

# Update an Existing Transaction
@router.put("/{transaction_id}", response_model=TransactionResponse)
def update_existing_transaction(
    transaction_id: int,
    transaction_update: TransactionUpdate,
    db: Session = Depends(get_db)
):
    updated_transaction = update_transaction(
        db=db, transaction_id=transaction_id, transaction_update=transaction_update
    )
    if not updated_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated_transaction

# Delete a Transaction
@router.delete("/{transaction_id}")
def delete_existing_transaction(transaction_id: int, db: Session = Depends(get_db)):
    success = delete_transaction(db=db, transaction_id=transaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"detail": "Transaction deleted successfully"}

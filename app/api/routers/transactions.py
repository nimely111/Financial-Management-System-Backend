from fastapi import APIRouter, Depends, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db_setup import get_db
from crud.transactions import create_transaction, get_transactions, get_transaction_by_id, update_transaction, delete_transaction
from schemas.transactions import TransactionCreate, TransactionUpdate, TransactionResponse

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("/transactions/", response_model=TransactionResponse)
def create_new_transaction(
    transaction: TransactionCreate,
    user_id: int,
    db: Session = Depends(get_db)
):
    return create_transaction(db=db, transaction=transaction, user_id=user_id)


def read_transactions(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_transactions(db=db, user_id=user_id, skip=skip, limit=limit)


@router.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction_by_id(db=db, transaction_id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.put("/transactions/{transaction_id}", response_model=TransactionResponse)
def update_existing_transaction(
    transaction_id: int,
    transaction_update: TransactionUpdate,
    db: Session = Depends(get_db),
):
    updated_transaction = update_transaction(
        db=db, transaction_id=transaction_id, transaction_update=transaction_update
    )
    if not updated_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated_transaction


@router.delete("/transactions/{transaction_id}")
def delete_existing_transaction(transaction_id: int, db: Session = Depends(get_db)):
    success = delete_transaction(db=db, transaction_id=transaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"detail": "Transaction deleted successfully"}
from sqlalchemy.orm import Session 
from models.models import Transaction
from schemas.transactions import TransactionCreate, TransactionUpdate


def create_transaction(
    db: Session, 
    transaction: TransactionCreate, 
    user_id: int
):
    db_transaction = Transaction(
        amount=transaction.amount,
        category=transaction.category,
        description=transaction.description,
        date=transaction.date,
        savings_amount=transaction.savings_amount,
        savings_type=transaction.savings_type,
        savings_currency=transaction.savings_currency,
        user_id=user_id,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction



def get_transactions(
    db: Session, 
    user_id: int, 
    skip: int = 0, 
    limit: int = 10
):
    return db.query(Transaction).filter(Transaction.user_id == user_id).offset(skip).limit(limit).all()

def get_transaction_by_id(
    db: Session, 
    transaction_id: int
):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

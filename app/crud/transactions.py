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



def update_transaction(
    db: Session, 
    transaction_id: int, 
    transaction_update: TransactionUpdate
):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not db_transaction:
        return None

    for key, value in transaction_update.dict(exclude_unset=True).items():
        setattr(db_transaction, key, value)

    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def delete_transaction(
    db: Session, 
    transaction_id: int
):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return True
    return False
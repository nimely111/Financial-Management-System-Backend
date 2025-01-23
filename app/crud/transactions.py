from sqlalchemy.orm import Session
from models.models import Transaction
from schemas.transactions import TransactionCreate, TransactionUpdate

# Create a New Transaction
def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

# Get All Transactions
def get_all_transactions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Transaction).offset(skip).limit(limit).all()


# Get a Single Transaction by ID
def get_transaction_by_id(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

# Update an Existing Transaction
def update_transaction(db: Session, transaction_id: int, transaction_update: TransactionUpdate):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not db_transaction:
        return None

    for key, value in transaction_update.dict(exclude_unset=True).items():
        setattr(db_transaction, key, value)

    db.commit()
    db.refresh(db_transaction)
    return db_transaction

# Delete a Transaction
def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return True
    return False

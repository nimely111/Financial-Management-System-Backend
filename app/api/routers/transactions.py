from fastapi import APIRouter, Depends, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db_setup import get_db
from crud.transactions import get_transactions, get_transaction, create_transaction, update_transaction, delete_transaction
from schemas.transactions import TransactionCreate, TransactionUpdate, Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)
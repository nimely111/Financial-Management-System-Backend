from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(500), unique=True)
    password =Column(String(500), nullable=False)
    username = Column(String(500))
    firstname = Column(String(500), nullable=False)
    lastname = Column(String(500))
    profile_picture = Column(String(700))
    dob = Column(String(500))
    nationality = Column(String(500))
    phone = Column(String(500))
    gender = Column(String(500))
    address = Column(String(500))

    # one to many relationship
    transactions = relationship('Transaction', back_populates='user')

# transaction table
class Transaction(Base):
    __tablename__ = 'transactions'
    # creating columns and datatypes for each record
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    is_income = Column(Boolean)
    date = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # one to many relationship
    user = relationship('User', back_populates='transactions')

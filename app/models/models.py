from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(500), nullable=False)
    lastname = Column(String(500))
    role = Column(String(500), nullable=False)
    password =Column(String(500), nullable=False)
    username = Column(String(500), nullable=False)
    profile_picture = Column(String(700), nullable=True)
    dob = Column(String(500), nullable=False)
    nationality = Column(String(500), nullable=False)
    contact_phone = Column(String(500), nullable=False)
    contact_email = Column(String(500), unique=True, nullable=False)
    gender = Column(String(500), nullable=False)
    address = Column(String(500), nullable=False)
    city_name = Column(String(500), nullable=False)
    about_user = Column(String(500), nullable=False)

    # one to many relationship with t ransaction
    transactions = relationship('Transaction', back_populates='user', cascade='all, delete-orphan')

# transaction table
class Transaction(Base):
    __tablename__ = 'transactions'
    # creating columns and datatypes for each record
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    date = Column(String)
    savings_amount = Column(Float, nullable=False)
    savings_type = Column(String, nullable=False)
    savings_currency = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # relationship back to user
    user = relationship('User', back_populates='transactions')

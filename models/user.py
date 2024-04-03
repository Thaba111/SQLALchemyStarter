from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    # creation of the table .
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)


    def __init__(self,username,email):
        self.username = username
        self.email = email


    def __repr__(self):
        return f"User {self.username}"
    
    

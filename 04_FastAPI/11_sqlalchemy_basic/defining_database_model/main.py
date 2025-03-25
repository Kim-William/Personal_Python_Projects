# defining_database_model > main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

# Database connection string
# This string includes username, password, host, and the database name.
DB_URL = "mysql+pymysql://root:Rladndrjf!23@localhost/ppp_defining"
db_engine = create_engine(DB_URL)

# SQLAlchemy base class for models
BaseModelClass = declarative_base()

class UserTable(BaseModelClass):
    # This class maps to the 'users' table in the database
    __tablename__ = 'users'
    
    # id column as primary key
    id = Column(Integer, primary_key=True, index=True)
    # username column with constraints
    username = Column(String(50), unique=True, index=True)
    # email column with length limit
    email = Column(String(120))
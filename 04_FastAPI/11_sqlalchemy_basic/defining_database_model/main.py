# defining_database_model > main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

# Database connection string
# This string includes username, password, host, and the database name.
DB_URL = "mysql+pymysql://root:Rodzl!23@localhost/ppp_defining"
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


# defining_database_model > main.py (2)
class UserInput(BaseModel):
    username: str
    email: str


# defining_database_model > main.py (3)
# Create a session as a dependency
def get_session():
    session = Session(bind=db_engine)
    try:
        yield session
    finally:
        session.close()


# defining_database_model > main.py (4)
# Create all tables based on the models if they don't already exist
BaseModelClass.metadata.create_all(bind=db_engine)


# defining_database_model > main.py (5)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/users/")
def create_user(user: UserInput, session: Session = Depends(get_session)):
    # Validate the incoming data using Pydantic's UserInput
    new_user = UserTable(username=user.username, email=user.email)
    session.add(new_user)              # Add instance to session
    session.commit()                   # Commit changes
    session.refresh(new_user)          # Refresh to get the latest state from DB
    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    }
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


# defining_database_model > main_1.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

BaseModelClass = declarative_base()

class UserTable(BaseModelClass):
    __tablename__ = 'users_1'

    # 'id' with autoincrement
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Primary Key")
    # 'username' with length limit, unique constraint, and an index
    username = Column(String(50), unique=True, nullable=False, index=True, comment="User Name")
    # 'email' with length limit, unique constraint
    email = Column(String(120), unique=True, nullable=False, comment="Email Address")
    # 'is_active' is a Boolean with a default value
    is_active = Column(Boolean, default=True, comment="Account Status")
    # 'created_at' is a DateTime with a default
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        comment="Creation Timestamp"
    )
    # 'grade' is a Float for scores or levels
    grade = Column(Float, comment="User Grade")



class UserInput(BaseModel):
    username: str
    email: str

# Create a session as a dependency
def get_session():
    session = Session(bind=db_engine)
    try:
        yield session
    finally:
        session.close()

# Create all tables based on the models if they don't already exist
BaseModelClass.metadata.create_all(bind=db_engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/users/")
def create_user(user: UserInput, session: Session = Depends(get_session)):
    # Validate the incoming data using Pydantic's UserInput
    new_user = UserTable(username=user.username, email=user.email, grade=1.1)
    session.add(new_user)              # Add instance to session
    session.commit()                   # Commit changes
    session.refresh(new_user)          # Refresh to get the latest state from DB
    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    }

# defining_database_model > main_1.py (2)
@app.post("/users_1/")
def create_user(
    user: UserInput, 
    session: Session = Depends(get_session)
):
    # Create and add to the session
    created_user = UserTable(username=user.username, email=user.email)
    session.add(created_user)
    session.commit()
    session.refresh(created_user)
    return {
        "id": created_user.id,
        "username": created_user.username,
        "email": created_user.email
    }


# defining_database_model > main_1.py (3)
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=db_engine
)

@app.post("/users_2/")
def create_user(user: UserInput):
    session = SessionLocal()
    try:
        db_user = UserTable(username=user.username, email=user.email)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email
        }
    finally:
        session.close()
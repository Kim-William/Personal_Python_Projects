# 04_02_main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define the Pydantic model for item data
class Item(BaseModel):
    name: str  # Required string field
    description: Optional[str] = None  # Optional string field with a default value of None
    price: float  # Required floating-point number
    tax: float = 0.1  # Optional field with a default value

@app.post("/items/")
async def items(item: Item):
    return {"item": item.dict()}  # Convert Pydantic model to dictionary
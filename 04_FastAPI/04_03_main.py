# 04_03_main.app
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Define the Pydantic model with field constraints
class Item(BaseModel):
    name: str = Field(..., title="Item Name", min_length=2, max_length=50)  
    description: str = Field(None, description="The description of the item", max_length=300)  
    price: float = Field(..., gt=0, description="The price must be greater than zero")  
    tag: List[str] = Field(default=[], alias="item-tags")  # Default empty list with an alias

@app.post("/items/")
async def items(item: Item):
    return {"item": item.dict()}  # Convert Pydantic model to dictionary
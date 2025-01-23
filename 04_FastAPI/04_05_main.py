# 04_05_main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

# Define an Item model with a list and union field
class Item(BaseModel):
    name: str  # A string field for the item name
    tags: List[str]  # A list of strings for tags
    variant: Union[int, str]  # A field that can be either an integer or a string

@app.post("/items/")
def items(item: Item):
    return {"item": item.dict()}  # Convert Pydantic model to dictionary
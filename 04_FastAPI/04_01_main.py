# 04_01_main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for data validation and serialization
class Item(BaseModel):  
    name: str  # The name of the item (string type)
    price: float  # The price of the item (float type)
    is_offer: bool = None  # Optional field to indicate if the item is on offer (default: None)

@app.post("/items/")
def items(item: Item):
    # Convert Pydantic model to dictionary and return it as a JSON response
    return {"item": item.dict()}  
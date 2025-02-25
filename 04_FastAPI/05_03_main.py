# Example Code 05_03_main.py
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# The `Item` class defines the structure of an item
class Item(BaseModel):
    name: str

# The `get_items` function returns a list of `Item` instances as JSON, 
# ensuring the response follows the defined model structure.
@app.get("/items/", response_model=List[Item])
async def get_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]


# uvicorn 05_03_main:app --reload
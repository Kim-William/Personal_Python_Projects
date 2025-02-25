# Example Code 05_01_main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    desc: str = None
    price: float

def get_item_detail(id):
    return {
        "name": "Item Name",
        "desc": "Item description",
        "price": 10.0,
        "final_price": 7.5
    }

@app.get("/item/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = get_item_detail(item_id)
    return item

# uvicorn 05_01_main:app --reload
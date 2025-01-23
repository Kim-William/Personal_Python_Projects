# 02_03_main.py
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

app = FastAPI()

@app.post('/items/')
async def create_item(item: Item):
    return item
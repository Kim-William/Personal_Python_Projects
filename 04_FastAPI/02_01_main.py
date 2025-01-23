# 02_01_main.py
from fastapi import FastAPI
app = FastAPI()
@app.get('/item/{item_id}')
def item(item_id: int):
    return {'item_id': item_id}

@app.get('/items')
def items(data: str = 'wkkim'):
    return {'data':data}
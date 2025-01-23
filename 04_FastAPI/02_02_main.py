# 02_02_main.py
from fastapi import FastAPI, Query
from typing import List,Dict
app = FastAPI()
@app.get('/item/{item_id}')
async def item(q:List[int] = Query([1,3,5])): # default value 설정 가능 '1, 3, 5'
    return {'query':q}

@app.post('/additem')
async def additem(items: Dict[str, int]):
    return items
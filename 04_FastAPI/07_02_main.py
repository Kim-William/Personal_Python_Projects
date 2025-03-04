# 07_02_main.py
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def read_items(internal_query: str = Query(None, alias="search")):
    return {"query_handled": internal_query}
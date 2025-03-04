# 07_01_main.py
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/users/")
def read_users(q: str = Query(None, max_length=50)):
    return {"q": q}
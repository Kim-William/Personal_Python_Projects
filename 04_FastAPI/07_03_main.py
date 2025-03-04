# 07_03_main.py
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/items/")
def create_item(item: dict = Body(...)):
    return {"item": item}

# # 07_03_main(2)
# from fastapi import FastAPI, Body

# app = FastAPI()

# @app.post("/items/")
# def create_item(item: dict = Body(None)):
#     return {"item": item}
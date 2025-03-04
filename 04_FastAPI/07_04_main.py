# 07_04_main.py
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/advanced_items/")
def create_advanced_item(
    item: dict = Body(
        default=None,
        example={"key": "value"},
        alias="item_alias",
        title="Sample Item",
        description="This is a sample item",
        deprecated=False
    )
):
    return {"item": item}
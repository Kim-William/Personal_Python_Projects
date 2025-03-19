# Example Code for Exception Handling
# 08_01_main.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    try:
        if item_id < 0:
            raise ValueError("Negative values are not allowed.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the application:
# uvicorn 08_01_main:app --reload
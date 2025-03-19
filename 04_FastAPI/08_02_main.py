# Example Code for Using HTTPException
# # 08_02_main.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id == 921111:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

# Run the application:
# uvicorn 08_02_main:app --reload
# 03_01_main.py
from fastapi import FastAPI

app = FastAPI()

# Root endpoint - Returns a welcome message
@app.get("/")
def index():
    return {"message": "Hello, FastAPI Index method"}

# Retrieve an item by its ID (Path Parameter)
@app.get("/item/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# Retrieve items with optional query parameters for pagination
@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Create a new item (expects a dictionary payload in the request body)
@app.post("/items/")
def create_items(item: dict):
    return {"item": item}

# Update an existing item by its ID
@app.put("/item/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}

# Delete an item by its ID
@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted"}

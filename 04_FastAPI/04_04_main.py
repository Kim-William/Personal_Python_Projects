# 04_04_main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define an Image model to hold image-related information
class Image(BaseModel):
    url: str  # URL of the image
    name: str  # Name of the image

# Define an Item model that includes the Image model as a nested field
class Item(BaseModel):
    name: str  # Name of the item
    description: str  # Description of the item
    image: Image  # Nested model field

@app.post("/items/")
def items(item: Item):
    return {"item": item.dict()}  # Convert Pydantic model to dictionary
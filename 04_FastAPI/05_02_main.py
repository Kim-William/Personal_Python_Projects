# Example Code 05_02_main.py
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Cat(BaseModel):
    name: str
    species:str = 'Cat'
    

class Dog(BaseModel):
    name: str
    species:str = 'Dog'

@app.get("/animal/", response_model=Union[Cat, Dog])
async def get_animal(animal: str):
    if animal == "cat":
        return Cat(name="Whiskers")
    else:
        return Dog(name="Fido")
    

# uvicorn 05_02_main:app --reload
# 01_main.py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"message":"Hello, this is FastAPI"}

@app.get('/info')
def info():
    return {"message":"Hello, this is Info API"}

@app.get('/hello')
def hello():
    return {"message":"Hello, this is hello API"}

@app.get('/hello2')
def hello2():
    return {"message":"Hello, this is hello2 API"}
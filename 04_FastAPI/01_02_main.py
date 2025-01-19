# 02_main.py
from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def index():
    return {'message':'Hello, this is Index API'}

@app.get('/item/{item_id}')
def path_1(item_id):
  return {'item_id':item_id}

@app.get('/users/{user_id}/items/{item_name}')
def path_2(user_id, item_name):
  return {'user_id':user_id, 'item_name':item_name}

@app.get('/items/')
def query(skip, limit):
  return {'skip':skip, 'limit':limit}
# static_project > main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def index(request:Request):
    return templates.TemplateResponse('index.html', {'request': request})
# uvicorn main:app --reload
# 06_02_main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/html", response_class=HTMLResponse)
def read_html():
    return "<h1>This is HTML</h1>"
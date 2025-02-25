# 06_03_main.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/text", response_class=PlainTextResponse)
def read_text():
    return "This is Plain Text"
# 06_04_main.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/redirect")
def read_redirect():
    return RedirectResponse(url="/text")
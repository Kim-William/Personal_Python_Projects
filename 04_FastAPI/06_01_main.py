# 06_01_main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/json", response_class=JSONResponse)
def read_json():
    return {"msg": "This is JSON"}
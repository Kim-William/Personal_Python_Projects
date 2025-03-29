# main_02.py
from fastapi import FastAPI
import asyncio

app = FastAPI()

async def fetch_data():
    await asyncio.sleep(2)
    return {"data": "some_data"}

@app.get("/")
async def read_root():
    data = await fetch_data()
    return {"message": "Hello", "fetched_data": data}
# To run: uvicorn main_02:app --reload
# Access http://127.0.0.1:8000 in a browser.
# After 2 seconds, you'll receive a response like:
# {"message": "Hello", "fetched_data": {"data": "some_data"}}
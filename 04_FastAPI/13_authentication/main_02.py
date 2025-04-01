# main_02.py
from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

@app.post("/set/")
async def set_session(request: Request):
    request.session["username"] = "william"
    return {"message": "Session value set"}

@app.get("/get/")
async def get_session(request: Request):
    # Retrieve the 'username' from the session. If not found, default to "Guest".
    username = request.session.get("username", "Guest")
    return {"username": username}
# To run: uvicorn main_02:app --reload
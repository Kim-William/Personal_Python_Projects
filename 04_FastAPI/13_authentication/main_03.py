# main_03.py
from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

# Add session middleware; replace 'your_secret_key' with a secure key in production.
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

@app.post("/login/")
async def login(request: Request, username: str, password: str):
    if username == "william" and password == "1234":
        request.session["username"] = username
        return {"message": "Successfully logged in"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/dashboard/")
async def dashboard(request: Request):
    username = request.session.get("username")
    if not username:
        raise HTTPException(status_code=401, detail="Not authorized")
    return {"message": f"Welcome to the dashboard, {username}"}
# To run: uvicorn main_03:app --reload
# my_project > main.py (1)
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# my_project > main.py (2)
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "username": "William Kim"})
# uvicorn main:app --reload

# my_project > main.py (3)
@app.get("/user/{username}")
def get_user(request: Request, username: str):
    return templates.TemplateResponse("index.html", {"request": request, "username": username})
# uvicorn main:app --reload

# my_project > main.py (4)
@app.get("/items/")
def read_items(request: Request, item_list: str = ""):
    items = item_list.split(",")
    return templates.TemplateResponse("index.html", {"request": request, "items": items})
# uvicorn main:app --reload

# my_project > main.py (5) & index_with_safe.html
@app.get("/safe")
def read_root_safe(request: Request):
    my_variable_with_html = "<h1>Hello, FastAPI!</h1>"
    return templates.TemplateResponse("index_with_safe.html", {"request": request, "my_variable_with_html": my_variable_with_html})
# uvicorn main:app --reload
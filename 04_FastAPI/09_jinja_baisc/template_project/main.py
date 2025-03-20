# template_project > main.py (1)
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# template_project > main.py (2)
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# template_project > main.py (2)
@app.get("/")
def read_root(request: Request):
    current_hour = datetime.now().hour
    greet_by_time='evening'
    # If the hour is before 12, print "morning"
    if current_hour < 12:
        greet_by_time = "morning"
    # Else if the hour is before 18, print "afternoon"
    elif current_hour < 18:
        greet_by_time = "afternoon"
    # Otherwise, print "evening"
    else:
        greet_by_time = "evening"
    return templates.TemplateResponse("index.html", {"request": request, "time_of_day": greet_by_time})
# uvicorn main:app --reload

@app.get("/loop/")
def read_root(request: Request, item_list: str = ""):
    items = item_list.split(",")
    return templates.TemplateResponse("index.html", {"request": request, "items": items})
# uvicorn main:app --reload

# template_project > main.py
@app.get("/inherit")
def template_inherit(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "text": "FastAPI and Jinja2 Inheritance Example."})
# uvicorn main:app --reload
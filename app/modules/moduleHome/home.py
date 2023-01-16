from fastapi import APIRouter,Request
from app import run

router = APIRouter()

@router.get("/")
def home(request:Request):
    return run.templates.TemplateResponse("home.html",{
        "request":request
    })
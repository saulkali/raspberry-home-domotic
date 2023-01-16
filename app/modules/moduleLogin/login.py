from fastapi import APIRouter,Request
from app import run

router = APIRouter(
    tags=["login"],
    prefix="/login",
    responses={
        404:{
            "description":"page not found"
        }
    }
)

@router.get("/")
def login(request:Request):
    return run.templates.TemplateResponse("login.html",{"request":request})
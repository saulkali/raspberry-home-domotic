from fastapi import APIRouter
from app.modules.moduleLogin import login
from app.modules.moduleHome import home

routers = APIRouter()
routers.include_router(login.router)
routers.include_router(home.router)
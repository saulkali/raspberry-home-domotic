from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from helper import get_file
from app.common.utils import routers
import uvicorn
from main import config
app = FastAPI()
app.include_router(routers.routers)
templates = Jinja2Templates(
    directory = get_file(
        config["SERVER"]["path_templates"]
    )
)

def run_app():
    uvicorn.run(
        app,
        host=config.server["SERVER"]["host"],
        port=config.server["SERVER"]["port"]
    )


import asyncio
import logging
import uvicorn

from fastapi import FastAPI

from fastapi.openapi.utils import get_openapi

from starlette.staticfiles import StaticFiles

from models.BaseModel import init
from routers.v1.AddressRouter import AddressRouter
from routers.v1.UsersRouter import UsersRouter
from routers.v1.ChallengeRouter import ChallengeRouter

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache




# Core Application Instance
app = FastAPI(
    title='fastapi-prgx-challenge-backend',
    version='1.0.0'
)

static_files_app = StaticFiles(directory=".")
app.mount(path="/static", app=static_files_app, name="static")

# Add Routers
app.include_router(AddressRouter)
app.include_router(UsersRouter)
app.include_router(ChallengeRouter)

# Initialise Data Model Attributes
init()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI - Backend - Challenge - prgx - python",
        version="1.0.0",
        description="This is a challenge for Backend position",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())

if __name__ == "__main__":
    uvicorn.run()
from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi_cache.decorator import cache

from schemas.Schema import (
    UsersSchema,
)

from services.UsersService import UsersService

UsersRouter = APIRouter(
    prefix="/v1/users", tags=["users"]
)


@UsersRouter.get("/", response_model=List[UsersSchema])
@cache(expire=300)
async def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    usersService: UsersService = Depends(),
):
    return [
        users.normalize()
        for users in usersService.list(
            name, pageSize, startIndex
        )
    ]


@UsersRouter.get("/{id}", response_model=UsersSchema)
@cache(expire=300)
async def get(id: int, usersService: UsersService = Depends()):
    return usersService.get(id).normalize()


@UsersRouter.post(
    "/",
    response_model=UsersSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    users: UsersSchema,
    usersService: UsersService = Depends(),
):
    return usersService.create(users).normalize()


@UsersRouter.patch("/{id}", response_model=UsersSchema)
def update(
    id: int,
    users: UsersSchema,
    usersService: UsersService = Depends(),
):
    return usersService.update(id, users).normalize()


@UsersRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    id: int, usersService: UsersService = Depends()
):
    return usersService.delete(id)
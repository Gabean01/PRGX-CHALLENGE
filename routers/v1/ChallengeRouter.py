from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi_cache.decorator import cache

from schemas.Schema import (
    UsersSchema
)
from models.UserFilterRequestModel import UserFilterRequest

from services.ChallengeService import ChallengeService

ChallengeRouter = APIRouter(
    prefix="/v1/challenge/users", tags=["challenge"]
)

@ChallengeRouter.get("/", response_model=List[UsersSchema])
@cache(expire=300)
async def index(
    filter: UserFilterRequest,
    challengeService: ChallengeService = Depends(),
): return [
        users.normalize()
        for users in challengeService.filter(filter)
    ]
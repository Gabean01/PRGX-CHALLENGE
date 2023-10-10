from typing import List

from fastapi import Depends
from models.UserFilterRequestModel import UserFilterRequest
from repositories.ChallengeRepository import ChallengeRepository
from models.UsersModel import Users

class ChallengeService:
    challengeRepository: ChallengeRepository

    def __init__(
        self, challengeRepository: ChallengeRepository = Depends()
    ) -> None:
        self.challengeRepository = challengeRepository

    def filter(
        self,
        filter: UserFilterRequest,
    ) -> List[Users]:
        return self.challengeRepository.list(filter)
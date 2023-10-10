from typing import List, Optional

from fastapi import Depends
from models.UsersModel import Users
from repositories.UsersRepository import UsersRepository
from schemas.Schema import UsersSchema, ChallengeSchema

class UsersService:
    usersRepository: UsersRepository

    def __init__(
        self, usersRepository: UsersRepository = Depends()
    ) -> None:
        self.usersRepository = usersRepository

    def create(self, users_body: ChallengeSchema):
        return self.usersRepository.create(users_body)

    def delete(self, users_id: int) -> None:
        return self.usersRepository.delete(
            Users(id=users_id)
        )

    def get(self, users_id: int) -> Users:
        return self.usersRepository.get(
            Users(id=users_id)
        )

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Users]:
        return self.usersRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, users_id: int, users_body: UsersSchema
    ) -> Users:
        return self.usersRepository.update(
            users_id, Users(name=users_body.name)
        )

from typing import List, Optional
import numpy as np
from fastapi import Depends
from sqlalchemy.orm import Session

import logging

from configs.database import (
    get_db_connection,
)

from models.UsersModel import Users
from models.AddressModel import Address
from models.UsersAddressModel import UsersAddress
from schemas.Schema import UsersSchema, ChallengeSchema

logger = logging.getLogger(__name__)

class UsersRepository:
    db: Session
    
    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db
    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Users]:
        query = self.db.query(Users)
        if name:
            query = query.filter_by(name=name)
        users : List[Users] = query.offset(start).limit(limit).all()
        
                
        return users
    def get(self, users: Users) -> Users:
        return self.db.get(
            Users,
            users.id,
        )

    def create(self, data: ChallengeSchema) -> Users:
        user = Users(
                firts_name=data.user.firts_name,
                last_name=data.user.last_name,
                email=data.user.email,
                password=data.user.password,
            )
        self.db.add(user)
        self.db.flush()

        if data.addresses:
            for address in data.addresses:
                address_db = self.db.query(Address).filter_by(**address.dict()).first()
                if not address_db:
                    address_db = Address(**address.dict())
                    self.db.add(address_db)
                    self.db.flush()

                userAddress = UsersAddress(user_id=user.id, address_id=address_db.id)
                self.db.add(userAddress)

        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, id: int, users: Users) -> Users:
        users.id = id
        self.db.merge(users)
        self.db.commit()
        return users
        
    def delete(self, users: Users) -> None:
        self.db.delete(users)
        self.db.commit()
        self.db.flush()
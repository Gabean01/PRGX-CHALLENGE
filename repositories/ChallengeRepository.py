from typing import List, Optional
import numpy as np
from fastapi import Depends
from sqlalchemy.orm import Session, joinedload
from models.UserFilterRequestModel import UserFilterRequest

import logging

from configs.database import (
    get_db_connection,
)
from models.UsersModel import Users
from models.UsersAddressModel import UsersAddress
from models.AddressModel import Address
from utils.utils import FilterBy

logger = logging.getLogger(__name__)

class ChallengeRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        filter: UserFilterRequest,
    ) -> List[Users]:
        query = self.db.query(Users).\
            join(UsersAddress, Users.id == UsersAddress.user_id).\
            join(Address, UsersAddress.address_id == Address.id).\
            options(joinedload(Users.addresses))

        if filter.filter_type == FilterBy.COUNTRY:
            query = query.filter(Address.country == filter.filter_value)

        elif filter.filter_type == FilterBy.STATE:
            query = query.filter(Address.state == filter.filter_value)

        elif filter.filter_type == FilterBy.CITY:
            query = query.filter(Address.city == filter.filter_value)

        elif filter.filter_type == FilterBy.ZIP:
            query = query.filter(Address.zip == filter.filter_value)

        users = query.distinct().all()

        return users
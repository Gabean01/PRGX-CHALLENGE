from typing import List, Optional
import numpy as np
from fastapi import Depends
from sqlalchemy.orm import Session

import logging

from configs.database import (
    get_db_connection,
)
from models.AddressModel import Address

logger = logging.getLogger(__name__)

class AddressRepository:
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
    ) -> List[Address]:
        query = self.db.query(Address)

        if name:
            query = query.filter_by(name=name)

        address : List[Address] = query.offset(start).limit(limit).all()


        return address

    def get(self, address: Address) -> Address:
        return self.db.get(
            Address,
            address.id,
        )

    def create(self, address: Address) -> Address:
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address

    def update(self, id: int, address: Address) -> Address:
        address.id = id
        self.db.merge(address)
        self.db.commit()
        return address

    def delete(self, address: Address) -> None:
        self.db.delete(address)
        self.db.commit()
        self.db.flush()
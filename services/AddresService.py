from typing import List, Optional

from fastapi import Depends
from models.AddressModel import Address
from repositories.AddressRepository import AddressRepository
from schemas.Schema import AddressSchema

class AddressService:
    addressRepository: AddressRepository

    def __init__(
        self, addressRepository: AddressRepository = Depends()
    ) -> None:
        self.addressRepository = addressRepository

    def create(self, address_body: AddressSchema) -> Address:
        return self.addressRepository.create(
            Address(
                    address_1=address_body.address_1,
                    address_2=address_body.address_2,
                    city=address_body.city,
                    state=address_body.state,
                    zip=address_body.zip,
                    country=address_body.country
                )
        )

    def delete(self, address_id: int) -> None:
        return self.addressRepository.delete(
            Address(id=address_id)
        )

    def get(self, address_id: int) -> Address:
        return self.addressRepository.get(
            Address(id=address_id)
        )

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Address]:
        return self.addressRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, address_id: int, address_body: AddressSchema
    ) -> Address:
        return self.addressRepository.update(
            address_id, Address(name=address_body.name)
        )
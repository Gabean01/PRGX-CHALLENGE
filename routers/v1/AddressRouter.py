from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi_cache.decorator import cache

from schemas.Schema import (
    AddressSchema
)

from services.AddressService import AddressService

AddressRouter = APIRouter(
    prefix="/v1/address", tags=["address"]
)


@AddressRouter.get("/", response_model=List[AddressSchema])
@cache(expire=300)
async def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    addressService: AddressService = Depends(),
):
    return [
        address.normalize()
        for address in addressService.list(
            name, pageSize, startIndex
        )
    ]


@AddressRouter.get("/{id}", response_model=AddressSchema)
@cache(expire=300)
async def get(id: int, addressService: AddressService = Depends()):
    return addressService.get(id).normalize()


@AddressRouter.post(
    "/",
    response_model=AddressSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    address: AddressSchema,
    addressService: AddressService = Depends(),
):
    return addressService.create(address).normalize()


@AddressRouter.patch("/{id}", response_model=AddressSchema)
def update(
    id: int,
    address: AddressSchema,
    addressService: AddressService = Depends(),
):
    return addressService.update(id, address).normalize()


@AddressRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    id: int, addressService: AddressService = Depends()
):
    return addressService.delete(id)
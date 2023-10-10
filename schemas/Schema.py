from pydantic import BaseModel, Field
from typing import List, Optional


class UsersBase(BaseModel):
    id: int = Field(alias='user_id')
    firts_name: str = Field(alias='user_firts_name')
    last_name: str = Field(alias='user_last_name')
    email: str = Field(alias='user_email')
    password: str = Field(alias='user_password')
    blurb: Optional[str]


 class Config:
        from_attributes = True
        populate_by_name = True

class AddressBase(BaseModel):
    id: int = Field(alias='address_id')
    address_1: str = Field(alias='address_address_1')
    address_2: str = Field(alias='address_address_2')
    city: str = Field(alias='address_city')
    state: str = Field(alias='address_state')
    zip: str = Field(alias='address_zip')
    country: str = Field(alias='address_country')
    blurb: Optional[str]

    class Config:
        from_attributes = True
        populate_by_name = True

class UsersSchema(BaseModel):
    addresses: List[AddressBase]

class AddressSchema(BaseModel):
     users: List[UsersBase]
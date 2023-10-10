from pydantic import BaseModel
from typing import List

class AddressSchema(BaseModel):
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str


class UsersSchema(BaseModel):
    firts_name: str
    last_name: str
    email: str
    password: str
  #addressess: List[AddressSchema]


class ChallengeSchema(BaseModel):
    user: UsersSchema
    addresses: List[AddressSchema]
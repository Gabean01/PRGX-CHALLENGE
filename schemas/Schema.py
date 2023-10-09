from pydantic import BaseModel


class UsersSchema(BaseModel):
    firts_name: str
    last_name: str
    email: str
    password: str



class AddressSchema(BaseModel):
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str
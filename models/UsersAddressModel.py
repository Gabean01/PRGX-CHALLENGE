from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy import(
    Column,
    ForeignKey,
    String
)

from models.BaseModel import EntityMeta

class UsersAddress(EntityMeta):
    __tablename__= "users_address"

    user_id = Column(ForeignKey('users.id'), primary_key=True)
    address_id = Column(ForeignKey('address.id'), primary_key=True)
    user = relationship("Users", back_populates="addresses")
    address = relationship("Address", back_populates="users")

    # proxies
    user_name = association_proxy(target_collection='users', attr='first_name')
    address_address_1 = association_proxy(target_collection='address', attr='address_1')
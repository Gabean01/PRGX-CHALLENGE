from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from sqlalchemy import(
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    DateTime
)

from models.BaseModel import EntityMeta

class Address(EntityMeta):
    __tablename__= "address"

    id = Column(Integer)
    address_1 = Column(String(36), nullable=False)
    address_2 = Column(String(36), nullable=False)
    city = Column(String(245), nullable=False)
    state = Column(String(200), nullable=False)
    zip = Column(String(200), nullable=False)
    country = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    


    PrimaryKeyConstraint(id)

    def normalize(self):
        return{
            "id": self.id.__str__(),
            "address_1": self.address_1.__str__(),
            "address_2": self.address_2.__str__(),
            "city": self.city.__str__(),
            "state": self.state.__str__(), 
            "zip": self.zip.__str__(),
            "country": self.country.__str__(),
            "created_at": self.created_at.__str__(),
            "updated_at": self.updated_at.__str__(),     
        }
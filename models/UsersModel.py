from sqlalchemy.sql import func

from sqlalchemy import(
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)

from models.BaseModel import EntityMeta

class Users(EntityMeta):
    __tablename__= "users"

    id = Column(Integer)
    firts_name = Column(String(36), nullable=False)
    last_name = Column(String(36), nullable=False)
    email = Column(String(245), nullable=False)
    password = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


    PrimaryKeyConstraint(id)

    def normalize(self):
        return{
            "id": self.id.__str__(),
            "firts_name": self.firts_name.__str__(),
            "last_name": self.last_name.__str__(),
            "email": self.email.__str__(),
            "password": self.password.__str__(), 
            "created_at": self.created_at.__str__(),
            "updated_at": self.updated_at.__str__(),     
        }
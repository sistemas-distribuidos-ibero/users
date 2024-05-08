from datetime import datetime as dt
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean
from .base import Base

class User(Base):
    '''
    User model
    '''
    __tablename__ = 'users'

    Id = Column(Integer(), primary_key=True)
    Name = Column(String(20), nullable=False)
    LastName = Column(String(30), nullable=False)
    Email = Column(String(40), nullable=False, unique=True)
    Password = Column(String(32), nullable=False)
    CreatedDate = Column(TIMESTAMP(), nullable=False, default=dt.now())
    UpdatedDate = Column(TIMESTAMP(), nullable=False, default=dt.now())
    IsBanned = Column(Boolean(), nullable=False, default=False)

    def serialize(self):
        """
        Serialize the data

        Returns:
            dict: The serialized data
        """

        return {
            "Id": self.Id,
            "Name": self.Name,
            "LastName": self.LastName,
            "Email": self.Email,
            "IsBanned": self.IsBanned
        }
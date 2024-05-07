from sqlalchemy import Column, Integer, String
from .base import Base

class Role(Base):
    '''
    Role model
    '''
    __tablename__ = 'roles'
    Id = Column(Integer(), primary_key=True)
    Name = Column(String(20), nullable=False)

    def serialize(self):
        """
        Serialize the data

        Returns:
            dict: The serialized data
        """

        return {
            "Id": self.Id,
            "Name": self.Name,
        }
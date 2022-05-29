# DATABASE tables and schemas

from numpy import integer
from tables import Col
from database import Base
from sqlalchemy import Column, Integer, String


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    model = Column(String)
    quantity = Column(Integer)

from sqlalchemy import Column, Integer, String

from .database import Base

class Token(Base):
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    url = Column(String, unique=True, index=True)
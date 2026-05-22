from sqlalchemy import Column, Integer, String
from database import Base

class Calculation(Base):

    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)

    calculation = Column(String)

    result = Column(String)
    
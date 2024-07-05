from sqlalchemy import Column, Integer, String, Float

from database import Base

class Person(Base):
    __tablename__ = "person"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), nullable=False)
    income: float = Column(Float, nullable=False)

class Bill(Base):
    __tablename__ = "bill"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), nullable=False)
    price: float = Column(Float, nullable=False)


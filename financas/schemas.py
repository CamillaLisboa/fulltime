from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str
    income: float
    

class PersonRequest(PersonBase):
    ...

class PersonResponse(PersonBase):
    id: int

    class Config:
        orm_mode = True

class BillBase(BaseModel):
    name: str
    price: float
    

class BillRequest(BillBase):
    ...

class BillResponse(BillBase):
    id: int

    class Config:
        orm_mode = True

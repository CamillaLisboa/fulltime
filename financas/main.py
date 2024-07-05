from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models import Person, Bill
from database import engine, Base, get_db
from repositories import PersonRepository, BillRepository
from schemas import PersonRequest, PersonResponse, BillRequest, BillResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


#cadastro de pessoa e conta 
@app.post("/api/person/new", response_model=PersonResponse, status_code=status.HTTP_201_CREATED)
def create(request: PersonRequest, db: Session = Depends(get_db)):
    person = PersonRepository.save(db, Person(**request.dict()))
    return person

@app.post("/api/bill/new", response_model=BillResponse, status_code=status.HTTP_201_CREATED)
def create(request: BillRequest, db: Session = Depends(get_db)):
    bill = BillRepository.save(db, Bill(**request.dict()))
    return bill


#listagem de todas as pessoas e contas
@app.get("/api/person", response_model=list[PersonResponse])
def find_all(db: Session = Depends(get_db)):
    person = PersonRepository.find_all(db)
    return [person for person in person]

@app.get("/api/bill", response_model=list[BillResponse])
def find_all(db: Session = Depends(get_db)):
    bill = BillRepository.find_all(db)
    return [bill for bill in bill]


#busca de pessoas e contas por id
@app.get("/api/person/{id}", response_model=PersonResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    person = PersonRepository.find_by_id(db, id)
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada"
        )
    return person

@app.get("/api/bill/{id}", response_model=BillResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    bill = BillRepository.find_by_id(db, id)
    if not bill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
        )
    return bill


#exclusão de pessoas e contas
@app.delete("/api/person/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not PersonRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada"
        )
    PersonRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.delete("/api/bill/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not BillRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
        )
    BillRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#edição de pessoas e contas
@app.put("/api/person/{id}", response_model=PersonResponse)
def update(id: int, request: PersonRequest, db: Session = Depends(get_db)):
    if not PersonRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada"
        )
    person = PersonRepository.save(db, Person(id=id, **request.dict()))
    return person

@app.put("/api/bill/{id}", response_model=BillResponse)
def update(id: int, request: BillRequest, db: Session = Depends(get_db)):
    if not BillRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada"
        )
    bill = BillRepository.save(db, Person(id=id, **request.dict()))
    return bill


#relatorio com total de renda, despesas e renda liquida
@app.get("/report/")
def report(db: Session = Depends(get_db)):
    total_income = db.query(Person).with_entities(func.sum(Person.income)).scalar()
    total_bill = db.query(Bill).with_entities(func.sum(Bill.price)).scalar()
    final_capital = total_income - total_bill
    return {"total_income": total_income,
            "total_bill": total_bill,
            "final_capital": final_capital
            }



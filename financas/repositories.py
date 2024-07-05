from sqlalchemy.orm import Session

from models import Person, Bill

class PersonRepository:
    @staticmethod
    def find_all(db: Session) -> list[Person]:
        return db.query(Person).all()

    @staticmethod
    def save(db: Session, person: Person) -> Person:
        if person.id:
            db.merge(person)
        else:
            db.add(person)
        db.commit()
        return person

    @staticmethod
    def find_by_id(db: Session, id: int) -> Person:
        return db.query(Person).filter(Person.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Person).filter(Person.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        person = db.query(Person).filter(Person.id == id).first()
        if person is not None:
            db.delete(person)
            db.commit()

class BillRepository:
    @staticmethod
    def find_all(db: Session) -> list[Bill]:
        return db.query(Bill).all()

    @staticmethod
    def save(db: Session, bill: Bill) -> Bill:
        if bill.id:
            db.merge(bill)
        else:
            db.add(bill)
        db.commit()
        return bill

    @staticmethod
    def find_by_id(db: Session, id: int) -> Bill:
        return db.query(Bill).filter(Bill.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Bill).filter(Bill.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        bill = db.query(Bill).filter(Bill.id == id).first()
        if bill is not None:
            db.delete(bill)
            db.commit()
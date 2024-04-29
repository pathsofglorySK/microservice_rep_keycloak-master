# 1. Поменять int на UUID в функциях

from datetime import datetime
from uuid import UUID, uuid4

from fastapi import Depends

from app.models.person import Person
from app.repositories.db_person_repo import PersonRepo




class PersonService():
    order_repo: PersonRepo


    def __init__(self, person_repo: PersonRepo = Depends(PersonRepo)) -> None:
        self.person_repo = person_repo
        # self.deliveryman_repo = DeliverymenRepo()

    def get_person(self) -> list[Person]:
        return self.person_repo.get_person()

    def get_person_by_id(self, id: UUID) -> Person:
        return self.person_repo.get_person_by_id(id)

    def create_person(self, ord_id: UUID, type: str) -> Person:
        person = Person(per_id=uuid4(), ord_id=ord_id, type=type)

        return self.person_repo.create_person(person)

    def delete_person(self, per_id: UUID) -> None:
        return self.person_repo.delete_person_by_id(per_id)

    


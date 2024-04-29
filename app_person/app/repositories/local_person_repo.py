import datetime
from uuid import UUID

from app.models.person import Person
from typing import Optional

# person: list[Person] = [
#     Person(per_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'), ord_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
#              type='test_per_type_1'),
#     Person(per_id=UUID('45309954-8e3c-4635-8066-b342f634252c'), ord_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
#              type='test_per_type_2'),
# ]

persons = []

class PersonRepo():
    def __init__(self, clear: bool = False) -> None:
        if clear:
            persons.clear()

    def get_person(self) -> list[Person]:
        return persons



    def get_person_by_id(self, id: UUID) -> Person:
        for d in persons:
            if d.per_id == id:
                return d

        raise KeyError

    def create_person(self, per: Person) -> Person:
        if len([d for d in persons if d.per_id == per.per_id]) > 0:
            raise KeyError

        persons.append(per)
        return per

    def delete_per(self, id: UUID) -> Optional[Person]:
        for i, person in enumerate(persons):
            if person.per_id == id:
                deleted_person = persons.pop(i)
                return deleted_person

        return None




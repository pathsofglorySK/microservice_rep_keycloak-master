import traceback
from uuid import UUID
from sqlalchemy.orm import Session

from app.database import get_db_per
from app.models.person import Person
from app.schemas.person import Person as DBPerson


class PersonRepo():
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db_per())

    def _map_to_model(self, person: DBPerson) -> Person:
        result = Person.from_orm(person)

        return result

    def _map_to_schema(self, person: Person) -> DBPerson:
        data = dict(person)
        result = DBPerson(**data)

        return result

    def get_person(self) -> list[Person]:
        person = []
        for d in self.db.query(DBPerson).all():
            person.append(self._map_to_model(d))

        return person

    def get_person_by_id(self, id: UUID) -> Person:
        person = self.db \
            .query(DBPerson) \
            .filter(DBPerson.per_id == id) \
            .first()

        if person == None:
            raise KeyError
        return self._map_to_model(person)

    def create_person(self, person: Person) -> Person:
        try:
            db_person = self._map_to_schema(person)
            self.db.add(db_person)
            self.db.commit()
            return self._map_to_model(db_person)
        except:
            traceback.print_exc()
            raise KeyError


    def delete_person_by_id(self, id: UUID) -> Person:
        try:
            # Find the order by its ord_id
            person = self.db.query(DBPerson).filter(DBPerson.per_id == id).one()

            # If the order is found, map it to the model and commit the deletion
            if person:
                deleted_person = self._map_to_model(person)
                self.db.delete(person)
                self.db.commit()
                return deleted_person
            else:
                # Handle the case where no order is found
                raise ValueError(f"No order found with ord_id {id}")
        except Exception as e:
            # Rollback any changes if there's an error
            self.db.rollback()
            # Re-raise the exception so it can be handled elsewhere
            raise e

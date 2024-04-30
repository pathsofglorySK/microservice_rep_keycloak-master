# /tests/unit/test_printing_repo.py

from datetime import datetime
from uuid import uuid4, UUID

import pytest

from app.models.person import Person
from app.repositories.local_person_repo import PersonRepo

person_test_repo = PersonRepo()


def test_empty_list() -> None:
    assert person_test_repo.get_person() == []


def test_add_first_person() -> None:
    person = Person(per_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                    ord_id=uuid4(),
                    type='test_per_type_1')
    assert person_test_repo.create_person(person) == person


def test_add_first_person_repeat() -> None:
    person = Person(per_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                    ord_id=uuid4(),
                    type='test_per_type_1')
    # person_test_repo.create_person(person)
    with pytest.raises(KeyError):
        person_test_repo.create_person(person)


def test_get_person_by_id() -> None:
    person = Person(per_id=uuid4(),
                    ord_id=uuid4(),
                    type='test_per_type_1')
    person_test_repo.create_person(person)
    assert person_test_repo.get_person_by_id(person.per_id) == person


def test_get_person_by_id_error() -> None:
    with pytest.raises(KeyError):
        person_test_repo.get_person_by_id(uuid4())



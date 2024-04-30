# /tests/integration/app_repositories/test_db_delivery_repo.py

from datetime import datetime
from uuid import UUID, uuid4

import pytest

from app.models.person import Person
from app.repositories.db_person_repo import PersonRepo


@pytest.fixture()
def person_repo() -> PersonRepo:
    repo = PersonRepo()
    return repo


@pytest.fixture(scope='session')
def person_id() -> UUID:
    return uuid4()


@pytest.fixture(scope='session')
def first_person() -> Person:
    return Person(per_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                  ord_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                  type='test_per_type_1')


@pytest.fixture(scope='session')
def second_person() -> Person:
    return Person(per_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
                  ord_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
                  type='test_per_type_2')


# def test_empty_list(person_repo: PersonRepo) -> None:
#     person_repo.delete_all_person()
#     assert person_repo.get_person() == []


def test_add_first_person(first_person: Person, person_repo: PersonRepo) -> None:
    assert person_repo.create_person(first_person) == first_person


def test_add_first_person_repeat(first_person: Person, person_repo: PersonRepo) -> None:
    with pytest.raises(KeyError):
        person_repo.create_person(first_person)


def test_get_person_by_id(first_person: Person, person_repo: PersonRepo) -> None:
    assert person_repo.get_person_by_id(first_person.per_id) == first_person


def test_get_person_by_id_error(person_repo: PersonRepo) -> None:
    with pytest.raises(KeyError):
        person_repo.get_person_by_id(uuid4())


def test_add_second_person(first_person: Person, second_person: Person, person_repo: PersonRepo) -> None:
    assert person_repo.create_person(second_person) == second_person
    persons = []
    persons.append(person_repo.get_person_by_id(first_person.per_id))
    persons.append(person_repo.get_person_by_id(second_person.per_id))
    assert len(persons) == 2
    assert persons[0] == first_person
    assert persons[1] == second_person


def test_delete_created_order(first_person: Person, second_person: Person, person_repo: Person) -> None:
    assert person_repo.delete_person_by_id(first_person.per_id) == first_person
    assert person_repo.delete_person_by_id(second_person.per_id) == second_person

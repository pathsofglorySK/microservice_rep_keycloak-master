
from uuid import uuid4, UUID

import pytest

from app.repositories.local_person_repo import PersonRepo
from app.services.person_service import PersonService

#from app_person.tests.unit.test_person_model import per_id, ord_id, type
from app_person.tests.unit.test_person_model import info


@pytest.fixture(scope='session')
def person_service() -> PersonService:
    return PersonService(PersonRepo(clear=True))


@pytest.fixture(scope='session')
def first_person_data() -> tuple[UUID, str]:
    return (uuid4(), 'test_person_type_1')


@pytest.fixture(scope='session')
def second_person_data() -> tuple[UUID, str]:
    return (uuid4(), uuid4(), 'test_person_type_2')


def test_empty_person(person_service: PersonService) -> None:
    assert person_service.get_person() == []


def test_create_first_person(
        first_person_data: tuple[UUID, str],
        person_service: PersonService
) -> None:
    ord_id, type
    person = person_service.create_person(ord_id, type)

    assert person.ord_id == ord_id
    assert person.type == type



def test_create_second_person(
        second_person_data: tuple[UUID, str],
        person_service
) -> None:
    ord_id, type
    person = person_service.create_person(ord_id, type)

    assert person.ord_id == ord_id
    assert person.type == type



def test_get_person_full(
        first_person_data: tuple[UUID, str],
        second_person_data: tuple[UUID, str],
        person_service
) -> None:
    persons = person_service.get_person()
    assert len(persons) == 2
    assert persons[0].ord_id == first_person_data[0]
    assert persons[0].type == first_person_data[1]

    assert persons[1].ord_id == second_person_data[0]
    assert persons[1].type == second_person_data[1]


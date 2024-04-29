
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
def first_person_data() -> tuple[UUID, str, str]:
    return (uuid4(), 'test_person_type_1', 'test_person_info_1')


@pytest.fixture(scope='session')
def second_person_data() -> tuple[UUID, str, str]:
    return (uuid4(), uuid4(), 'test_person_type_2', 'test_person_info_1')


def test_empty_person(person_service: PersonService) -> None:
    assert person_service.get_person() == []


def test_create_first_person(
        first_person_data: tuple[UUID, str, str],
        person_service: PersonService
) -> None:
    ord_id, type, info
    person = person_service.create_person(ord_id, type, info)

    assert person.ord_id == ord_id
    assert person.type == type
    assert person.info == info


def test_create_second_person(
        second_person_data: tuple[UUID, str, str],
        person_service
) -> None:
    ord_id, type, info
    person = person_service.create_person(ord_id, type, info)

    assert person.ord_id == ord_id
    assert person.type == type
    assert person.info == info


def test_get_person_full(
        first_person_data: tuple[UUID, str, str],
        second_person_data: tuple[UUID, str, str],
        person_service
) -> None:
    persons = person_service.get_person()
    assert len(persons) == 2
    assert persons[0].ord_id == first_person_data[0]
    assert persons[0].type == first_person_data[1]
    assert persons[0].info == first_person_data[2]

    assert persons[1].ord_id == second_person_data[0]
    assert persons[1].type == second_person_data[1]
    assert persons[1].info == second_person_data[2]


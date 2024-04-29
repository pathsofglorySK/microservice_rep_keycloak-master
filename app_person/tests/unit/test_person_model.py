# /tests/unit/test_printing_model.py

from datetime import datetime
from uuid import uuid4, UUID

import pytest
from pydantic import ValidationError

from app.models.person import Person


ord_id: UUID
type: str
info: str


def test_person_creation():

    ord_id = uuid4()
    type = 'test_per_type_1'
    info = 'test_per_info_1'

    person = Person(ord_id=ord_id, type=type, info=info)

    assert dict(person) == {'ord_id': ord_id, 'type': type, 'info': info}


def test_person_date_required():
    with pytest.raises(ValidationError):
        Person(ord_id=uuid4(),
               type='test_per_type_1',
               info='test_per_info_1')


def test_person_ord_id_required():
    with pytest.raises(ValidationError):
        Person(per_id=uuid4(),
               type='test_per_type_1',
               info='test_per_info_1')

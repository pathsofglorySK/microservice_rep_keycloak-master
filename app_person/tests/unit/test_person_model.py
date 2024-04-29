# /tests/unit/test_printing_model.py

from datetime import datetime
from uuid import uuid4, UUID

import pytest
from pydantic import ValidationError

from app.models.person import Person

per_id: UUID
ord_id: UUID
type: str


def test_person_creation():
    per_id = uuid4()
    ord_id = uuid4()
    type = 'test_per_type_1'

    person = Person(per_id=per_id, ord_id=ord_id, type=type)

    assert dict(person) == {'per_id': per_id, 'ord_id': ord_id, 'type': type}


def test_person_date_required():
    with pytest.raises(ValidationError):
        Person(per_id=uuid4(),
               ord_id=uuid4(),
               type='test_per_type_1')


def test_person_ord_id_required():
    with pytest.raises(ValidationError):
        Person(per_id=uuid4(),
               type='test_per_type_1')

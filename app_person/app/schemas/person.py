from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.schemas.base_schema import Base


class Person(Base):
    __tablename__ = 'person'

    per_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    ord_id = Column(UUID(as_uuid=True), nullable=False)
    type = Column(String, nullable=False)



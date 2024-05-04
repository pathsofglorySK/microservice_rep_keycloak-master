from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Header

from app.models.person import Person, CreatePersonRequest
from app.services.person_service import PersonService
import prometheus_client
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from fastapi import Request

person_router = APIRouter(prefix='/person', tags=['Person'])


provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(
  TracerProvider(
    resource=Resource.create({SERVICE_NAME: "delivery-service"})
  )
)
jaeger_exporter = JaegerExporter(
  agent_host_name="localhost",
  agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
  BatchSpanProcessor(jaeger_exporter)
)

name='Delivery Service'
tracer = trace.get_tracer(name)


delivery_router = APIRouter(prefix='/delivery', tags=['Delivery'])
metrics_router = APIRouter(tags=['Metrics'])

get_deliveries_count = prometheus_client.Counter(
    "get_deliveries_count",
    "Total got all deliveries"
)

created_delivery_count = prometheus_client.Counter(
    "created_delivery_count",
    "Total created deliveries"
)

started_delivery_count = prometheus_client.Counter(
    "started_printing_count",
    "Total started deliveries"
)

completed_delivery_count = prometheus_client.Counter(
    "completed_printing_count",
    "Total completed deliveries"
)

cancelled_delivery_count = prometheus_client.Counter(
    "cancelled_printing_count",
    "Total canceled deliveries"
)

def user_admin(role):
    if role == "service_user" or role == "service_admin":
        return True
    return False

def admin(role):
    if role == "service_admin":
        return True
    return False




@person_router.get('/')
def get_person(person_service: PersonService = Depends(PersonService)) -> list[Person]:
    return person_service.get_person()


@person_router.post('/')
def add_order(
        person_info: CreatePersonRequest,
        order_service: PersonService = Depends(PersonService)
) -> Person:
    try:
        person = order_service.create_person(person_info.ord_id, person_info.type)
        return person.dict()
    except KeyError:
        raise HTTPException(400, f'Order with id={person_info.per_id} already exists')


@person_router.post('/{id}/delete')
def delete_order(id: UUID, person_service: PersonService = Depends(PersonService)) -> Person:
    try:
        person = person_service.delete_person(id)
        return person.dict()
    except KeyError:
        raise HTTPException(404, f'Person with id={id} not found')
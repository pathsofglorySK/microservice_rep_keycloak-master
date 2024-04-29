import json
import traceback
from asyncio import AbstractEventLoop

import aio_pika
from aio_pika import IncomingMessage
from aio_pika.abc import AbstractRobustConnection

from app.settings import settings
from app.services.person_service import PersonService
from app.repositories.db_person_repo import PersonRepo


# async def send_to_person_queue(data: dict):
#     try:
#         # Установка соединения с RabbitMQ
#         connection = await aio_pika.connect_robust(settings.amqp_url)
#
#         async with connection:
#             # Создание канала
#             channel = await connection.channel()
#
#             # Объявление очереди, если её нет
#             queue = await channel.declare_queue('person_created_queue', durable=True)
#
#             for key, value in data.items():
#                 if isinstance(value, UUID):
#                     data[key] = str(value)
#                 elif isinstance(value, datetime):
#                     data[key] = value.isoformat()
#
#             # Отправка данных в очередь
#             await channel.default_exchange.publish(
#                 aio_pika.Message(body=json.dumps(data).encode()),
#                 routing_key='person_created_queue'
#             )
#             print(" [x] Sent %r" % data)
#
#     except aio_pika.exceptions.AMQPError as e:
#         print(f"Error occurred while sending data to queue: {e}")
#
#     finally:
#         # Закрытие соединения после отправки данных в очередь
#         await connection.close()


async def process_created_person(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        print("\n/// process_created_person ///\n ")
        PersonService(PersonRepo()).create_person(
            data['ord_id'], data['type'], data['info'])
        await msg.ack()
    except:
        traceback.print_exc()
        await msg.ack()


async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
    connection = await aio_pika.connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    person_created_queue = await channel.declare_queue('person_created_queue', durable=True)

    await person_created_queue.consume(process_created_person)

    print('Started RabbitMQ consuming...')

    return connection


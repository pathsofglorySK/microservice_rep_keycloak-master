# uvicorn app.main:app --reload

import asyncio

from fastapi import FastAPI

from app import rabbitmq
# from app.endpoints.order_router import order_router
from app.endpoints.person_router import person_router

app = FastAPI(title='Service')

#app.include_router(order_router, prefix='/api')
app.include_router(person_router, prefix='/api')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.consume(loop))

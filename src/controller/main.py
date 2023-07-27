import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, FastAPI
from .database import get_session
from .manipulator import ManipulatorClient
from .schemas import ManipulatorSchema, ControllerSchema
from .service import StatusService

app = FastAPI()


@app.post('/history')
async def send_data(
        start: datetime.datetime,
        end: datetime.datetime,
        session: AsyncSession = Depends(get_session),
):

    result = await StatusService(session).get(start, end)
    period_obj = [ManipulatorSchema(**obj) for obj in result]
    return period_obj


@app.post('/')
async def send_data(
        data: ControllerSchema,
        session: AsyncSession = Depends(get_session),
):
    result = ManipulatorSchema(
        created_at=data.created_at,
        status='up' if data.payload < 100 else 'down'
    )
    await StatusService(session).post(result)
    await ManipulatorClient().send(result)
    return {'status': 'Ok'}

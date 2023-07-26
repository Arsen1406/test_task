import datetime
from controller.database import get_session
from controller.manipulator import Manipulator
from controller.schemas import ControllerSchema, ManipulatorSchema
from controller.service import StatusService

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, FastAPI


app = FastAPI()


@app.post('/history')
async def send_data(
        start: datetime,
        end: datetime,
        session: AsyncSession = Depends(get_session),
):

    result = await StatusService(session).get(start, end)
    period_obj = [ControllerSchema(**obj.dict()) for obj in result]
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
    await Manipulator().send(result)
    return {'status': True}

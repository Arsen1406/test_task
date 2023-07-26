from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from models import Status


class StatusService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, time_start, time_end):
        stmt = select(Status).where(
            Status.created_at.between(time_start, time_end))
        result = await self.session.scalars(stmt)
        return result.all()

    async def post(self, obj):
        query = insert(Status).values(
            status=obj.status,
            created_at=obj.created_at
        )

        result = await self.session.execute(query)
        return result

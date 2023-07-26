from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from settings import settings


async_engine = create_async_engine(settings.DB_DSN, echo=False, future=True)
async_session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

BaseModel = declarative_base()

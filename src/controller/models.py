from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Status(Base):

    __tablename__ = 'status'

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    status = Column(String, comment='Статус')
    created_at = Column(DateTime, comment='Дата создания')

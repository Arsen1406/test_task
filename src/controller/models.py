from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Status(DeclarativeBase):

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

from typing import Self

from sqlalchemy import Column, UUID, String, select
from sqlalchemy.ext.asyncio import AsyncSession

from quickflow.models.base import Base


class User(Base):
    __tablename__ = "users"

    uuid = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    @staticmethod
    def encrypt_password(password: str) -> str:
        ...

    @classmethod
    async def get_by_email(cls, db: AsyncSession, email: str) -> Self | None:
        data = await db.execute(select(cls))
        result = [*data.scalars()]
        return None

    @classmethod
    def get_by_email_and_password_hash(cls, email: str, password: str) -> Self | None:
        ...

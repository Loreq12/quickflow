# SYNC
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     except:
#         db.rollback()
#     finally:
#         db.close()


# ASYNC
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine

from quickflow.config import get_settings


async def get_async_db():
    settings = get_settings()
    async_engine = create_async_engine(settings.database.async_connector(), echo=True)
    async_session = async_sessionmaker(async_engine, expire_on_commit=False)

    async with async_session() as session:
        yield session


async def get_async_engine() -> AsyncEngine:
    settings = get_settings()
    return create_async_engine(settings.database.async_connector(), echo=True)


def get_engine() -> Engine:
    settings = get_settings()
    return create_engine(settings.database.sync_connector(), echo=True)

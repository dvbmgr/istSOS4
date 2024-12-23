from app import (
    PG_MAX_OVERFLOW,
    PG_POOL_SIZE,
    PG_POOL_TIMEOUT,
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

dsn = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(
    dsn,
    pool_size=PG_POOL_SIZE,
    max_overflow=PG_MAX_OVERFLOW,
    pool_timeout=PG_POOL_TIMEOUT,
    pool_recycle=3600,
    pool_pre_ping=True,
)

Base = declarative_base()

SCHEMA_NAME = "sensorthings"

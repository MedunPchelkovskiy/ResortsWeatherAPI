from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Shared declarative base for ORM models.

    IMPORTANT: this API is READ-ONLY against an existing schema owned by the
    Prefect pipeline. Do not run Base.metadata.create_all() or Alembic
    migrations from this project — the gold tables already exist and are
    managed elsewhere.
    """

    pass

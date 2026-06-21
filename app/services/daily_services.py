from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.gold import GoldDaily


async def get_daily(
    db: AsyncSession,
    resort_name: str,
    start_date: date,
    end_date: date,
) -> list[GoldDaily]:
    """
    Returns daily rows for one resort between start_date and end_date
    (inclusive), ordered oldest -> newest.

    resort_name is plain str here, not the ResortName enum — the enum is a
    FastAPI/route-layer validation concept; the service layer just needs
    the raw value to put in a SQL WHERE clause.
    """
    stmt = (
        select(GoldDaily)
        .where(GoldDaily.place_name == resort_name)
        .where(GoldDaily.forecast_date_utc >= start_date)
        .where(GoldDaily.forecast_date_utc <= end_date)
        .order_by(GoldDaily.forecast_date_utc.asc())
    )
    result = await db.execute(stmt)
    return list(result.scalars().all())
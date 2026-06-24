from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.gold import GoldDaily, GoldFiveDayForecast


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


async def get_five_day(
    db: AsyncSession,
    resort_name: str,
    start_date: date,
) -> list[GoldDaily]:
    """
    Returns five days rows for one resort after start_date
    (inclusive), ordered oldest -> newest.

    resort_name is plain str here, not the ResortName enum — the enum is a
    FastAPI/route-layer validation concept; the service layer just needs
    the raw value to put in a SQL WHERE clause.
    """
    stmt = (
        select(GoldFiveDayForecast)
        .where(GoldFiveDayForecast.place_name == resort_name)
        .where(GoldFiveDayForecast.forecast_date_utc >= start_date)
        .order_by(
            GoldFiveDayForecast.forecast_date_utc.asc(),
            GoldFiveDayForecast.ingest_date.desc(),
            GoldFiveDayForecast.ingest_hour.desc(),
        )
        .distinct(GoldFiveDayForecast.forecast_date_utc)
        .limit(5)
    )
    result = await db.execute(stmt)
    return list(result.scalars().all())
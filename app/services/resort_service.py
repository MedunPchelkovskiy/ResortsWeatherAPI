from sqlalchemy import distinct, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.gold import GoldYearly


async def list_resorts(db: AsyncSession) -> list[str]:
    """
    Returns distinct resort names ever seen in gold_yearly, sorted alphabetically.

    Querying DISTINCT over an aggregated table works fine at 3 resorts. If
    this grows past a handful of resorts, or you need resort metadata
    (coordinates, slugs, display names for the widget), extract a dedicated
    `resorts` dimension table at that point — not before.
    """
    result = await db.execute(
        select(distinct(GoldYearly.place_name)).order_by(GoldYearly.place_name)
    )
    return list(result.scalars().all())

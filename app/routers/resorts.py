from datetime import date, timedelta

from app.schemas.daily import DailyOut
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.enums import ResortName
from app.db.session import get_db
from app.schemas.resort import ResortOut
from app.services import daily_services, resort_service

router = APIRouter(prefix="/resorts", tags=["resorts"])


@router.get("", response_model=list[ResortOut])
async def get_resorts() -> list[ResortOut]:
    """
    List all resorts the system supports (for dropdowns/widgets).

    Reads from the ResortName enum — the same fixed source of truth used to
    validate place_name in the detail endpoints below — instead of querying
    the DB. No `db` parameter needed here at all anymore, since there's
    nothing to query: this is just "loop over a Python enum and build a
    response object for each member".

    `ResortName` is iterable because it's an Enum class — iterating over it
    gives you each member (ResortName.bansko, ResortName.pamporovo, ...) in
    declaration order. `.value` on a member gives you the plain string
    ("bansko"), which is what ResortOut expects.
    """
    return [ResortOut(resort_name=resort.value) for resort in ResortName]


@router.get("/{place_name}/daily", response_model=list[DailyOut])
async def get_daily(
        place_name: ResortName,
        start_date: date | None = Query(
            default=None,
            description="Defaults to 7 days before end_date if omitted.",
        ),
        end_date: date | None = Query(
            default=None,
            description="Defaults to today if omitted.",
        ),
        db: AsyncSession = Depends(get_db),
) -> list[DailyOut]:
    """
    Daily weather data for one resort over a date range.

    place_name: validated against the ResortName enum BEFORE this function
    runs — an unknown resort never reaches this code, FastAPI returns 422
    automatically.

    start_date / end_date: plain query params (?start_date=2026-06-01).
    FastAPI parses ISO date strings into real `date` objects for you.

    Deliberately NOT done as `end_date: date = Query(default=date.today())` —
    that default would be computed ONCE, when this module is imported (i.e.
    when the app starts), and then reused for every request forever. Using
    `None` as the default and computing "today" inside the function body
    (below) means it's evaluated fresh on every request.
    """
    if end_date is None:
        end_date = date.today()
    if start_date is None:
        start_date = end_date - timedelta(days=7)

    # Per-field constraints (e.g. ge=/le= in Query()) only validate one
    # field at a time. Relationships BETWEEN fields — like "start must not
    # be after end" — have to be checked by hand, here in the route.
    if start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="start_date must not be after end_date",
        )

    rows = await daily_services.get_daily(
        db, resort_name=place_name.value, start_date=start_date, end_date=end_date
    )
    return rows  # response_model + from_attributes handles ORM -> DailyOut conversion

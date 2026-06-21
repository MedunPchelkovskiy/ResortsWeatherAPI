from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.resort import ResortOut
from app.services import resort_service

router = APIRouter(prefix="/resorts", tags=["resorts"])


@router.get("", response_model=list[ResortOut])
async def get_resorts(db: AsyncSession = Depends(get_db)) -> list[ResortOut]:
    """List all resorts known to the system (for dropdowns/widgets)."""
    names = await resort_service.list_resorts(db)
    return [ResortOut(resort_name=name) for name in names]

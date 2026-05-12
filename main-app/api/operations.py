from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from models.deribit import DeribitRead
from services.operations import get_all_deribit

router = APIRouter(
    prefix="/operations",
)


@router.get("", response_model=List[DeribitRead])
async def get_all_deribits(session: AsyncSession = Depends(db_helper.session_getter)):
    deribits = await get_all_deribit(session=session)
    return deribits

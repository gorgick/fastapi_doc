from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tables import Deribit


async def get_all_deribit(session: AsyncSession) -> Sequence[Deribit]:
    stmt = select(Deribit).order_by(Deribit.id)
    result = await session.scalars(stmt)
    return result.all()

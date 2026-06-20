from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.deribit import DeribitCreate
from services.send_email import send_email, send_welcome_email
from tables import Deribit


async def get_all_deribit(session: AsyncSession) -> Sequence[Deribit]:
    stmt = select(Deribit).order_by(Deribit.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_deribit(session: AsyncSession, deribit_create: DeribitCreate)->Deribit:
    deribit = Deribit(**deribit_create.model_dump())
    session.add(deribit)
    await session.commit()
    # await session.refresh(deribit)
    # await send_email(recipient=deribit.email, subject="Welcome", body=f"Hello {deribit.name}")
    await send_welcome_email(deribit)
    return deribit

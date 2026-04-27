from sqlalchemy import Numeric
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Deribit(Base):
    __tablename__ = "deribites"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

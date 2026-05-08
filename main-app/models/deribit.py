from pydantic import BaseModel


class Deribit(BaseModel):
    name: str
    price: float
    created_at: int


class DeribitCreate(Deribit):
    pass


class DeribitRead(Deribit):
    id: int

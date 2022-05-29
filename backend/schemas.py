# PYDANTIC (FASTAPI) Schemas
from pydantic import BaseModel


class Item(BaseModel):
    name: str = None
    model: str
    quantity: int

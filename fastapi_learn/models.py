from pydantic import BaseModel


class Produto(BaseModel):
    name: str
    price: float

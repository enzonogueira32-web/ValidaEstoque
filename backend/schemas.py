from datetime import date
from pydantic import BaseModel


class ProdutoCreate(BaseModel):
    nome: str
    categoria: str
    quantidade: int
    quantidade_minima: int
    data_validade: date
    preco: float
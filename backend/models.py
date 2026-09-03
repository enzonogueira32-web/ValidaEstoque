from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base


class Produto(Base):

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False)

    categoria = Column(String, nullable=False)

    quantidade = Column(Integer, nullable=False)

    quantidade_minima = Column(Integer, nullable=False)

    data_validade = Column(Date, nullable=False)

    preco = Column(Float, nullable=False)
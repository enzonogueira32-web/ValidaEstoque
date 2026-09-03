from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, Base
from . import models
from .schemas import ProdutoCreate
from .regras import verificar_status

app = FastAPI(title="ValidaEstoque")


Base.metadata.create_all(bind=engine)


def get_db():
    db = Session(bind=engine)

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def inicio():
    return {
        "mensagem": "API da validação do estoque funcionando!"
    }


@app.post("/produtos")
def criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):
    novo_produto = models.Produto(
        nome=produto.nome,
        categoria=produto.categoria,
        quantidade=produto.quantidade,
        quantidade_minima=produto.quantidade_minima,
        data_validade=produto.data_validade,
        preco=produto.preco
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto

@app.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(models.Produto).all()

    resultado = []

    for produto in produtos:
        resultado.append({
            "id": produto.id,
            "nome": produto.nome,
            "categoria": produto.categoria,
            "quantidade": produto.quantidade,
            "quantidade_minima": produto.quantidade_minima,
            "data_validade": produto.data_validade,
            "preco": produto.preco,
            "status": verificar_status(produto.data_validade)
        })

    return resultado

@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    return produto

@app.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto_existente = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if produto_existente is None:
        return {"erro": "Produto não encontrado"}

    produto_existente.nome = produto.nome
    produto_existente.categoria = produto.categoria
    produto_existente.quantidade = produto.quantidade
    produto_existente.quantidade_minima = produto.quantidade_minima
    produto_existente.data_validade = produto.data_validade
    produto_existente.preco = produto.preco

    db.commit()
    db.refresh(produto_existente)

    return produto_existente

@app.delete("/produtos/{produto_id}")
def deletar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    produto = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if produto is None:
        return {"erro": "Produto não encontrado"}

    db.delete(produto)
    db.commit()

    return {
        "mensagem": "Produto deletado com sucesso"
    }
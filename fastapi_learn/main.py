from fastapi import FastAPI
from models import Produto


app = FastAPI(title="Lerning FastAPI")


@app.get("/quadrado/{valor}")
def quadrado(valor: int):
    result = valor * valor
    return {"quadrado": result}


@app.get("/dobro")
def dobro(valor: int):
    result = valor * 2
    return {"dobro": result}


@app.get("/area-retangulo")
def retangulo(altura: int, largura: int):
    result = altura * largura
    return {"area retangulo": result}


@app.post("/produtos", status_code=201)
def produtos(produto: Produto):
    return {"Produto"["nome" : produto.name, "preco" : produto.price]}

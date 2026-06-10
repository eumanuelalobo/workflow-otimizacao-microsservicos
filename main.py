# main.py - Microsserviço de Catálogo de Produtos
import sys
sys.path.insert(0, '.')

import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI(title="Bounded Context: Catálogo de Produtos")

class Produto(BaseModel):
    nome: str
    descricao: str
    preco: float
    estoque: int

@app.get("/produtos")
def listar_produtos():
    # Representa o serviço "Listar produtos" do Bounded Context
    return [{"id": 1, "nome": "Placa Eletrônica Ty-1", "preco": 150.0}]

@app.post("/produtos", status_code=201)
def inserir_produto(produto: Produto):
    # Representa o serviço "Inserir um novo produto"
    return {"status": "Produto inserido com sucesso", "dados": produto}
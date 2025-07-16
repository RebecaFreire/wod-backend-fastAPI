from fastapi import FastAPI
from app.routes import atleta
from app.routes import categoria

app = FastAPI(
    title="API CrossFit DIO",
    version="1.0.0",
    description="Uma API assíncrona para gerenciamento de atletas, categorias e centros de treinamento"
)

app.include_router(atleta.router, prefix="/atletas", tags=["Atletas"])
app.include_router(categoria.router, prefix="/categorias", tags=["Categorias"])

@app.get("/")
def root():
    return {"mensagem": "API de Crossfit ativa com SQLite!"}

# 🚧 Passo temporário para criar as tabelas no SQLite
from app.database import Base, engine
from app.models.atleta import Atleta

Base.metadata.create_all(bind=engine)

from pydantic import BaseModel
from app.schemas.categoria import Categoria  # ← certifique-se de importar
from typing import Optional
from app.schemas.categoria import Categoria

class AtletaBase(BaseModel):
    nome: str
    idade: int
    categoria_id: int

class AtletaCreate(AtletaBase):
    pass

class Atleta(AtletaBase):
    id: int
    categoria: Optional[Categoria]

    class Config:
        from_attributes = True

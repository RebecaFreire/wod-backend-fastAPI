from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.categoria import Categoria as CategoriaModel
from app.schemas.categoria import CategoriaCreate, Categoria

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Categoria)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    nova = CategoriaModel(**categoria.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/", response_model=list[Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(CategoriaModel).all()

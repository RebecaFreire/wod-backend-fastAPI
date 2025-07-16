from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.atleta import AtletaCreate, Atleta
from app.models.atleta import Atleta as AtletaModel
from app.schemas.atleta import AtletaCreate, Atleta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import HTTPException

@router.post("/", response_model=Atleta)
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    try:
        novo_atleta = AtletaModel(**atleta.dict())  # ← modelo do banco, id é gerado
        db.add(novo_atleta)
        db.commit()
        db.refresh(novo_atleta)
        return novo_atleta
    except Exception as e:
        print("🔥 Erro ao criar atleta:", e)
        raise HTTPException(status_code=500, detail="Erro interno ao criar atleta")

@router.get("/", response_model=list[Atleta])
def listar_atletas(db: Session = Depends(get_db)):
    return db.query(AtletaModel).all()


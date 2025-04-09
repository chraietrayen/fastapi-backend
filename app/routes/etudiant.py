from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.etudiant import Etudiant
from app.schemas.etudiant import EtudiantCreate, EtudiantOut

router = APIRouter(prefix="/etudiants", tags=["Etudiants"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EtudiantOut)
def create_etudiant(etudiant: EtudiantCreate, db: Session = Depends(get_db)):
    db_etudiant = Etudiant(**etudiant.dict())
    db.add(db_etudiant)
    db.commit()
    db.refresh(db_etudiant)
    return db_etudiant

@router.get("/", response_model=list[EtudiantOut])
def get_etudiants(db: Session = Depends(get_db)):
    return db.query(Etudiant).all()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.formation import Formation
from app.schemas.formation import FormationCreate, FormationOut

router = APIRouter(prefix="/formations", tags=["Formations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FormationOut)
def create_formation(formation: FormationCreate, db: Session = Depends(get_db)):
    db_formation = Formation(**formation.dict())
    db.add(db_formation)
    db.commit()
    db.refresh(db_formation)
    return db_formation

@router.get("/", response_model=list[FormationOut])
def get_formations(db: Session = Depends(get_db)):
    return db.query(Formation).all()

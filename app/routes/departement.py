from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.departement import Departement
from app.schemas.departement import DepartementCreate, DepartementOut

router = APIRouter(prefix="/departements", tags=["Départements"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DepartementOut)
def create_departement(dep: DepartementCreate, db: Session = Depends(get_db)):
    db_dep = Departement(**dep.dict())
    db.add(db_dep)
    db.commit()
    db.refresh(db_dep)
    return db_dep

@router.get("/", response_model=list[DepartementOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(Departement).all()

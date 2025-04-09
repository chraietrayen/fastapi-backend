from pydantic import BaseModel

class EtudiantBase(BaseModel):
    nom: str
    email: str
    password: str
    departement_id: int

class EtudiantCreate(EtudiantBase):
    pass

class EtudiantOut(BaseModel):
    id: int
    nom: str
    email: str
    departement_id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel

class DepartementBase(BaseModel):
    nom: str

class DepartementCreate(DepartementBase):
    pass

class DepartementOut(BaseModel):
    id: int
    nom: str

    class Config:
        orm_mode = True

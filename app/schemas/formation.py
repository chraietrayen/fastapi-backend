from pydantic import BaseModel

class FormationBase(BaseModel):
    titre: str
    description: str

class FormationCreate(FormationBase):
    pass

class FormationOut(BaseModel):
    id: int
    titre: str
    description: str

    class Config:
        orm_mode = True

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Etudiant(Base):
    __tablename__ = "etudiants"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    departement_id = Column(Integer, ForeignKey("departements.id"))

    departement = relationship("Departement", back_populates="etudiants")

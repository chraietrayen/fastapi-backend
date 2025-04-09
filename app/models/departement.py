from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Departement(Base):
    __tablename__ = "departements"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True)

    etudiants = relationship("Etudiant", back_populates="departement")

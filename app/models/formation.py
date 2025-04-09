from sqlalchemy import Column, Integer, String
from app.database import Base

class Formation(Base):
    __tablename__ = "formations"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, unique=True)
    description = Column(String)

from fastapi import FastAPI
from app.routes import etudiants, formations, departements

app = FastAPI()

app.include_router(etudiants.router, prefix="/etudiants", tags=["Etudiants"])
app.include_router(formations.router, prefix="/formations", tags=["Formations"])
app.include_router(departements.router, prefix="/departements", tags=["Departements"])

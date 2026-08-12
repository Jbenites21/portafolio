from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api import product_router
from app.infraestructure.database import engine, Base
import app.infraestructure.models  # Importar los modelos para que se registren con SQLAlchemy

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Electro Cables API", version="1.0.0")

Instrumentator().instrument(app).expose(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://98.84.142.13:4321", 
                   "http://alb-proyecto-1459454180.us-east-1.elb.amazonaws.com"],  # Permitir todas las fuentes para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router.router)

@app.get("/")
def read_root():
    return {"message": "¡API de Electro Cables funcionando al 100% desde docker con docker compose!"}
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#CAMBIOS DE CONFIGURACION PARA CONEXION DE ORACLE CLOUD
#DB_HOST = os.getenv("DB_HOST")
#DB_PORT = os.getenv("DB_PORT")
#DB_SERVICE = os.getenv("DB_SERVICE")
TSN_NAME = os.getenv("TSN_NAME")
WALLET_PATH = os.getenv("WALLET_PATH")
WALLET_PASSWORD = os.getenv("WALLET_PASSWORD")

#CAMBIO DE URL DE CONEXION PARA ORACLE CLOUD
#DATABASE_URL = f"oracle+oracledb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?service_name={DB_SERVICE}"
DATABASE_URL = f"oracle+oracledb://{DB_USER}:{DB_PASSWORD}@{TSN_NAME}"

#SE PASA EL WALLET A TRAVES DE CONNECT_ARGS PARA LA CONEXION A ORACLE CLOUD
engine = create_engine(
    DATABASE_URL, 
    echo=True,
    connect_args={
        "config_dir": WALLET_PATH,
        "wallet_password": WALLET_PASSWORD,
        "wallet_location": WALLET_PATH
        }
    )

#creación de la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base declarativa para los modelos de SQLAlchemy
Base = declarative_base()

#dependencia para obtener la sesión de la base de datos en las rutas de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import Column, Integer, String, Float, Boolean, Identity
from app.infraestructure.database import Base

class ProductModel(Base):
    __tablename__ = "products"
    
    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(100), index=True)
    description = Column(String(500))
    price = Column(Float)
    stock = Column(Integer)
    category = Column(String(50), index=True)
    image_url = Column(String(255))
    is_active = Column(Boolean, default=True)  # True para activo, False para inactivo
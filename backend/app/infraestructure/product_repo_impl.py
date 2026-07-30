from sqlalchemy.orm import Session
from typing import List, Optional

from app.application.product_repo import ProductRepository
from app.domain.product import Product
from app.infraestructure.models import ProductModel

class ProductRepositoryImpl(ProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all_products(self) -> List[Product]:
        product_models = self.db.query(ProductModel).filter(ProductModel.is_active == True).all()
        domain_products = [Product(**product_model.__dict__) for product_model in product_models]
        return domain_products

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        product_model = self.db.query(ProductModel).filter(ProductModel.id == product_id, ProductModel.is_active == True).first()
        domain_product = Product(**product_model.__dict__) if product_model else None
        return domain_product

    def create_product(self, product: Product) -> Product:
        product_model = ProductModel(**product.__dict__)
        self.db.add(product_model)
        self.db.commit()
        self.db.refresh(product_model)
        domain_product = Product(**product_model.__dict__)
        return domain_product

    def update_product(self, product_id: int, product: Product) -> Optional[Product]:
        product_model = self.db.query(ProductModel).filter(ProductModel.id == product_id, ProductModel.is_active == True).first()
        if not product_model:
            return None
        for key, value in product.__dict__.items():
            setattr(product_model, key, value)
        self.db.commit()
        self.db.refresh(product_model)
        domain_product = Product(**product_model.__dict__)
        return domain_product

    def delete_product(self, product_id: int) -> bool:
        product_model = self.db.query(ProductModel).filter(ProductModel.id == product_id, ProductModel.is_active == True).first()
        if not product_model:
            return False
        product_model.is_active = False  # Marcar como inactivo en lugar de eliminar
        self.db.commit()
        return True
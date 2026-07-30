from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def create_product(self, product: Product) -> Product:
        pass

    @abstractmethod
    def update_product(self, product_id: int, product: Product) -> Optional[Product]:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        pass
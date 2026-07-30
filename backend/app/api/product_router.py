from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.infraestructure.database import get_db
from app.infraestructure.product_repo_impl import ProductRepositoryImpl

from app.domain.product import Product
from app.api.schemas import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["products"])

#== INYECCIÓN DE DEPENDENCIAS ==#
def get_product_repository(db: Session = Depends(get_db)) -> ProductRepositoryImpl:
    return ProductRepositoryImpl(db)

@router.get("/", response_model=List[ProductResponse])
def get_all_products(product_repo: ProductRepositoryImpl = Depends(get_product_repository)):
    products = product_repo.get_all_products()
    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, product_repo: ProductRepositoryImpl = Depends(get_product_repository)):
    product = product_repo.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return product

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_create: ProductCreate, product_repo: ProductRepositoryImpl = Depends(get_product_repository)):
    product = Product(**product_create.model_dump())
    created_product = product_repo.create_product(product)
    return created_product

@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product_update: ProductCreate, product_repo: ProductRepositoryImpl = Depends(get_product_repository)):
    product = Product(**product_update.model_dump())
    updated_product = product_repo.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, product_repo: ProductRepositoryImpl = Depends(get_product_repository)):
    success = product_repo.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return None
from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., example="Cable HDMI 2.0")
    description: Optional[str] = None
    price: float = Field(..., gt=0, description="Precio del producto, debe ser mayor que 0", example=19.99)
    stock: int = Field(..., gt=0, description="Cantidad en stock, debe ser mayor que 0", example=10)
    category: str = Field(..., example="Cables")
    image_url: str = Field(..., example="https://example.com/image.jpg")
    is_active: bool = Field(default=True, description="Indica si el producto está activo o no", example=True)

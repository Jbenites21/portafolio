// La "forma" de los datos, idéntica a tu schema de FastAPI
export interface Product {
  id: number;
  name: string;
  description?: string | null;
  price: number;
  stock: number;
  category: string;
  image_url: string;
  is_active: boolean;
}

// El componente en sí
export default function ProductCard({ product }: { product: Product }) {
  return (
    <div className="border border-gray-200 rounded-lg shadow-md p-4 max-w-sm bg-white hover:shadow-lg transition-shadow">
      <img 
        src={product.image_url} 
        alt={product.name} 
        className="w-full h-48 object-cover rounded-md mb-4"
      />
      <div className="flex justify-between items-center mb-2">
        <h2 className="text-xl font-bold text-gray-800">{product.name}</h2>
        <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded">
          {product.category}
        </span>
      </div>
      <p className="text-gray-600 text-sm mb-4 line-clamp-2">
        {product.description || "Sin descripción"}
      </p>
      <div className="flex justify-between items-center">
        <span className="text-2xl font-extrabold text-green-600">
          ${product.price.toFixed(2)}
        </span>
        <span className="text-sm text-gray-500">
          Stock: {product.stock}
        </span>
      </div>
    </div>
  );
}
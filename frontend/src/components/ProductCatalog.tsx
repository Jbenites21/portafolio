import { useState, useEffect } from 'react';
import ProductCard, { type Product } from './ProductCard'; // Importamos tu tarjeta
import ProductForm from './ProductForm'; // Importamos tu formulario

export default function ProductCatalog() {
  // 1. LA MEMORIA: Creamos un estado para guardar los productos (inicia como un arreglo vacío)
  const [products, setProducts] = useState<Product[]>([]);
  // También es buena práctica tener un estado para saber si está cargando
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const fetchProducts = async () => {
        try {
            const response = await fetch('http://alb-proyecto-1459454180.us-east-1.elb.amazonaws.com:8088') // 1. Hacer el fetch al backend
            const data = await response.json()// 2. Convertir la respuesta a JSON
            setProducts(data) // 3. Usar setProducts(data) para guardar los datos en la memoria
        } catch (error) {
            console.error('Error fetching products:', error);
        }finally {
            setIsLoading(false) // 4. Usar setIsLoading(false) para apagar el estado de carga independientemente si falla o no
        }
    }

  // 2. EL EJECUTOR: Se corre una sola vez al cargar el componente
  useEffect(() => {
    fetchProducts() // 5. Llamar a la función para que se ejecute
    
  }, []); // Los corchetes vacíos significan "ejecuta esto solo una vez al inicio"

  // 3. LO QUE VE EL USUARIO
  if (isLoading) {
    return <div className="text-center text-xl text-gray-500">Cargando catálogo desde Oracle...</div>;
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* Colocamos el formulario aquí. 
        Le pasamos la función fetchProducts como PROP. 
        Así, cuando el formulario termine de hacer el POST, ejecutará fetchProducts y la pantalla se actualizará sola.
      */}
      <ProductForm onProductAdded={fetchProducts} />

      <h2 className="text-2xl font-bold text-gray-800 mb-6 border-b pb-2">Inventario Actual</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}
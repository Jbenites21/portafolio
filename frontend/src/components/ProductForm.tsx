import React, { useState } from 'react';

// Le decimos al formulario que va a recibir una función como "prop"
// para avisarle al catálogo que debe recargarse cuando guardemos algo.
export default function ProductForm({ onProductAdded }: { onProductAdded: () => void }) {
  
  // 1. LA MEMORIA DEL FORMULARIO
  // Usamos un solo estado que guarda un objeto con todos los campos.
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    stock: '',
    category: 'Redes',
    image_url: 'https://via.placeholder.com/300', // Una imagen por defecto temporal
    is_active: true
  });

  // 2. EL ESCUCHADOR DE CAMBIOS
  // Cada vez que tecleas algo, esta función actualiza la memoria.
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      // Si el campo es precio o stock, lo convertimos a número para que FastAPI no se queje
      [name]: name === 'price' || name === 'stock' ? Number(value) : value
    });
  };

  // 3. EL EJECUTOR DEL ENVÍO (POST)
  const handleSubmit = async (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault(); // ¡Vital! Evita que la página web se recargue (el comportamiento por defecto de HTML)

    try {
      const response = await fetch('http://alb-proyecto-1459454180.us-east-1.elb.amazonaws.com:8088', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json' // Le decimos a FastAPI que le enviamos un JSON
        },
        body: JSON.stringify(formData) // Convertimos nuestro objeto de memoria a texto JSON
      });

      if (response.ok) {
        alert("¡Cable guardado en Oracle con éxito!");
        // Limpiamos el formulario devolviendo la memoria a cero
        setFormData({ name: '', description: '', price: '', stock: '', category: 'Redes', image_url: 'https://via.placeholder.com/300', is_active: true });
        
        // ¡Magia! Llamamos a la función que nos pasó el padre para recargar la lista
        onProductAdded(); 
      } else {
        alert("Error al guardar. Revisa la consola.");
      }
    } catch (error) {
      console.error("Fallo la conexión con FastAPI:", error);
    }
  };

  // 4. LA INTERFAZ VISUAL (Puro Tailwind)
  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md mb-8 border border-gray-200">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">Agregar Nuevo Cable</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">Nombre del Cable</label>
          <input required type="text" name="name" value={formData.name} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2" />
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700">Categoría</label>
          <select name="category" value={formData.category} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2">
            <option value="Redes">Redes</option>
            <option value="Video">Video</option>
            <option value="Energía">Energía</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Precio ($)</label>
          <input required type="number" step="0.01" name="price" value={formData.price} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2" />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Stock Inicial</label>
          <input required type="number" name="stock" value={formData.stock} onChange={handleChange} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2" />
        </div>
        
        <div className="md:col-span-2">
          <label className="block text-sm font-medium text-gray-700">Descripción</label>
          <textarea name="description" value={formData.description} onChange={handleChange} rows={2} className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2"></textarea>
        </div>
      </div>

      <button type="submit" className="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors">
        Guardar en Base de Datos
      </button>
    </form>
  );
}
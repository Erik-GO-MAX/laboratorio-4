class CarritoDeCompras:
    def _init_(self):
        """Inicializa el carrito de compras con una lista vacía de productos."""
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto a la lista de productos."""
        self.productos.append(producto)
        print(f"Producto '{producto}' agregado al carrito.")

    def eliminar_producto(self, producto):
        """Elimina un producto de la lista si está presente."""
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Producto '{producto}' eliminado del carrito.")
        else:
            print(f"El producto '{producto}' no está en el carrito.")

    def mostrar_productos(self):
        """Muestra los productos en el carrito o indica que está vacío."""
        if self.productos:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(f"- {producto}")
        else:
            print("El carrito está vacío.")

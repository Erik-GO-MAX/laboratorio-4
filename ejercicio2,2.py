class Biblioteca:
    def _init_(self):
        """Inicializa la biblioteca con una lista vacía de libros."""
        self.libros = []

    def agregar_libro(self, libro):
        """Agrega un libro a la lista de libros y muestra un mensaje de confirmación."""
        self.libros.append(libro)
        print(f"El libro '{libro}' ha sido agregado a la biblioteca.")

    def eliminar_libro(self, libro):
        """Elimina un libro de la lista si está presente, y muestra un mensaje de confirmación o error."""
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"El libro '{libro}' ha sido eliminado de la biblioteca.")
        else:
            print(f"El libro '{libro}' no se encuentra en la biblioteca.")

    def mostrar_libros(self):
        """Muestra todos los libros disponibles en la biblioteca o indica que está vacía."""
        if self.libros:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro}")
        else:
            print("La biblioteca está vacía.")

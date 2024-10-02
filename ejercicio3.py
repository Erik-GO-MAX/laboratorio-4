class Libro:
    def _init_(self, titulo, autor):
        # Constructor que inicializa el título, autor y el estado de disponibilidad
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Por defecto el libro está disponible

    def prestar(self):
        # Método para prestar el libro, si está disponible
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        # Método para devolver el libro y marcarlo como disponible
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

    def mostrar_estado(self):
        # Método para mostrar el estado actual del libro
        estado = "disponible" if self.disponible else "prestado"
        print(f"El libro '{self.titulo}' de {self.autor} está {estado}.")

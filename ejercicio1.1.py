class Cafetera:
    def _init_(self, capacidad):
        """Inicializa la cafetera con una capacidad máxima y un nivel actual de café de 0."""
        self.capacidad = capacidad  # Capacidad máxima en tazas
        self.nivel_actual = 0  # Nivel inicial de café

    def llenar_cafetera(self):
        """Llena la cafetera al máximo estableciendo el nivel actual igual a la capacidad máxima."""
        self.nivel_actual = self.capacidad
        print(f"La cafetera ha sido llenada. Capacidad actual: {self.nivel_actual} tazas.")

    def servir_cafe(self):
        """Disminuye el nivel de café en 1 taza si hay café disponible."""
        if self.nivel_actual > 0:
            self.nivel_actual -= 1
            print(f"Se ha servido una taza de café. Tazas restantes: {self.nivel_actual}.")
        else:
            print("No hay café disponible para servir.")

    def mostrar_nivel(self):
        """Muestra cuántas tazas de café quedan disponibles en la cafetera."""
        print(f"Nivel actual de café: {self.nivel_actual} tazas.")

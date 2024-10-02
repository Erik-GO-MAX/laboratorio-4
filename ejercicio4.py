class Termostato:
    def _init_(self, temperatura_inicial):
        """Inicializa el termostato con una temperatura dada."""
        self.temperatura = temperatura_inicial

    def incrementar_temperatura(self, grados):
        """Incrementa la temperatura en la cantidad de grados especificada."""
        self.temperatura += grados

    def decrementar_temperatura(self, grados):
        """Decrementa la temperatura en la cantidad de grados especificada."""
        self.temperatura -= grados

    def mostrar_temperatura(self):
        """Muestra la temperatura actual del termostato."""
        print(f"La temperatura actual es: {self.temperatura}°C")

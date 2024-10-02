class Temporizador:
    def _init_(self, tiempo_inicial):
        """Inicializa el temporizador con el tiempo restante dado en segundos."""
        self.tiempo_restante = tiempo_inicial
        self.en_progreso = False

    def iniciar_temporizador(self):
        """Inicia el temporizador y muestra el tiempo restante."""
        if self.tiempo_restante > 0:
            self.en_progreso = True
            print(f"El temporizador ha sido iniciado. Tiempo restante: {self.tiempo_restante} segundos.")
        else:
            print("No se puede iniciar el temporizador porque el tiempo restante es 0 o negativo.")

    def pausar_temporizador(self):
        """Pausa el temporizador y muestra el tiempo restante."""
        if self.en_progreso:
            self.en_progreso = False
            print(f"El temporizador ha sido pausado. Tiempo restante: {self.tiempo_restante} segundos.")
        else:
            print("El temporizador no está en progreso.")

    def mostrar_tiempo_restante(self):
        """Muestra el tiempo restante actual del temporizador."""
        print(f"Tiempo restante: {self.tiempo_restante} segundos.")

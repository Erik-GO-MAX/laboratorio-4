class Persona:
    def _init_(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad
        self.esta_despierto = True  
    def dormir(self):
       
        self.esta_despierto = False

    def despertar(self):
        
        self.esta_despierto = True

    def mostrar_estado(self):
        
        estado = "despierto/a" if self.esta_despierto else "durmiendo/a"
        print(f"{self.nombre} (edad: {self.edad}) está {estado}.")
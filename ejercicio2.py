class CuentaBancaria:
    def _init_(self, titular, saldo=0):
        # Constructor que inicializa el titular y el saldo
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        # Método para incrementar el saldo
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        # Método para disminuir el saldo, si hay suficiente disponible
        if cantidad > self.saldo:
            print(f"Saldo insuficiente. No se puede retirar {cantidad}.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que 0.")
        else:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")

    def mostrar_saldo(self):
        # Método para mostrar el saldo actual
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo}")
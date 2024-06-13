# Programación Orientada a Objetos (POO)

class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def ingresar_temperaturas_diarias(self):
        for dia in range(7):
            temperatura = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
            self.ingresar_temperatura(temperatura)

    def calcular_promedio_semanal(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

def main():
    clima = ClimaDiario()
    print("Ingrese las temperaturas diarias para determinar el promedio semanal:")
    clima.ingresar_temperaturas_diarias()
    promedio = clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados Celsius")

if __name__ == "__main__":
    main()

# Programación Tradicional

def ingresar_temperaturas_diarias():
    temperaturas = [18]
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

def main():
    print("Ingrese las temperaturas diarias para determinar el promedio semanal:")
    temperaturas = ingresar_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados Celsius")

if __name__ == "__main__":
    main()

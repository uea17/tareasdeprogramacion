# Este programa calcula el área de un círculo y convierte unidades de medida de centímetros a pulgadas.

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: El radio del círculo (float)
    :return: El área del círculo (float)
    """
    area = math.pi * radio ** 2
    return area


def convertir_cm_a_pulgadas(centimetros):
    """
    Convierte una medida de centímetros a pulgadas.

    :param centimetros: La medida en centímetros (float)
    :return: La medida en pulgadas (float)
    """
    pulgadas = centimetros / 2.54
    return pulgadas


# Variables y resultados
radio_circulo = 5.0  # Radio del círculo en centímetros (float)
area_circulo = calcular_area_circulo(radio_circulo)

medida_cm = 10.0  # Medida en centímetros (float)
medida_pulgadas = convertir_cm_a_pulgadas(medida_cm)

# Resultados
print(f"El área de un círculo con radio {radio_circulo} cm es {area_circulo:.2f} cm².")
print(f"{medida_cm} cm equivalen a {medida_pulgadas:.2f} pulgadas.")

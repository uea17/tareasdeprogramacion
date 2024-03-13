def calcular_descuento(monto_total, porcentaje_descuento=10):

    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

def mostrar_resultados(monto_total, descuento):

    monto_final = monto_total - descuento
    print("Monto total de la compra:", monto_total)
    print("Monto del descuento aplicado:", descuento)
    print("Monto final a pagar después del descuento:", monto_final)

# Llamadas a la función desde el programa principal
monto_compra_1 = 150
descuento_1 = calcular_descuento(monto_compra_1)
print("Resultado de la primera llamada:")
mostrar_resultados(monto_compra_1, descuento_1)

monto_compra_2 = 200
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
print("\nResultado de la segunda llamada:")
mostrar_resultados(monto_compra_2, descuento_2)


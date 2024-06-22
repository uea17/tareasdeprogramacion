# tienda.py

class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False


class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.reducir_stock(cantidad):
            self.productos.append((producto, cantidad))
            return True
        return False

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)
        return total


class Orden:
    def __init__(self, carrito, cliente):
        self.carrito = carrito
        self.cliente = cliente
        self.total = carrito.calcular_total()

    def confirmar_orden(self):
        # Aquí se podría implementar la lógica para confirmar la orden
        return True

# Ejemplo de uso
if __name__ == "__main__":
    producto1 = Producto(1, "Laptop", 1500, 10)
    producto2 = Producto(2, "Mouse", 50, 100)

    carrito = CarritoDeCompras()
    carrito.agregar_producto(producto1, 1)
    carrito.agregar_producto(producto2, 2)

    print(f"Total del carrito: ${carrito.calcular_total()}")

    orden = Orden(carrito, "Maria Gomez")
    if orden.confirmar_orden():
        print(f"Orden confirmada para {orden.cliente} con un total de ${orden.total}")

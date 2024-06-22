# hotel.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = True

    def reservar(self):
        if self.esta_disponible:
            self.esta_disponible = False
            return True
        return False

    def liberar(self):
        self.esta_disponible = True


class Reserva:
    def __init__(self, habitacion, cliente, fecha_inicio, fecha_fin):
        self.habitacion = habitacion
        self.cliente = cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def reservar_habitacion(self, numero, cliente, fecha_inicio, fecha_fin):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero and habitacion.esta_disponible:
                if habitacion.reservar():
                    reserva = Reserva(habitacion, cliente, fecha_inicio, fecha_fin)
                    return reserva
        return None

# Ejemplo de uso
if __name__ == "__main__":
    hotel = Hotel("Hotel Python")
    habitacion1 = Habitacion(101, "Simple", 50)
    habitacion2 = Habitacion(102, "Doble", 80)

    hotel.agregar_habitacion(habitacion1)
    hotel.agregar_habitacion(habitacion2)

    reserva = hotel.reservar_habitacion(101, "Juan Perez", "2024-07-01", "2024-07-10")
    if reserva:
        print(f"Habitación {reserva.habitacion.numero} reservada para {reserva.cliente}")
    else:
        print("No se pudo realizar la reserva")

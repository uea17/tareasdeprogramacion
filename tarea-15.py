# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Myrian",
    "edad": 24,
    "ciudad": "Riobamba",
}

# Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "riobamba"

# Agregar una nueva clave-valor para la profesión
informacion_personal["profecion"] = "Ingeniera"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print("Diccionario final:", informacion_personal)

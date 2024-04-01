# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt y escribir notas personales en él
with open("my_notes.txt", "w") as file:
    file.write("Mis notas personales:\n")  # Escribir la primera línea
    file.write("- Este es mi primer recordatorio.\n")  # Escribir la segunda línea
    file.write("- No olvidar hacer la tarea.\n")  # Escribir la tercera línea
    file.write("- Comprar leche en el supermercado.\n")  # Escribir la cuarta línea

# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt para lectura
with open("my_notes.txt", "r") as file:
    print("Contenido del archivo my_notes.txt:")
    # Leer el contenido del archivo línea por línea
    for line in file:
        print(line.strip())  # Mostrar cada línea leída




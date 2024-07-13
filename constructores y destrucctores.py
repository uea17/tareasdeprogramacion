# Clase que representa un archivo de texto
class ArchivoTexto:
    def __init__(self, nombre_archivo):
        """Constructor que inicializa el nombre del archivo y abre el archivo."""
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')
        print(f"Archivo {nombre_archivo} ha sido abierto para escritura.")

    def escribir_linea(self, linea):
        """Método para escribir una línea en el archivo."""
        self.archivo.write(linea + '\n')
        print(f"Escribiendo línea en {self.nombre_archivo}: {linea}")

    def __del__(self):
        """Destructor que cierra el archivo."""
        self.archivo.close()
        print(f"Archivo {self.nombre_archivo} ha sido cerrado.")

# Ejemplo de uso de la clase ArchivoTexto
def main():
    archivo = ArchivoTexto("mi_archivo.txt")
    archivo.escribir_linea("Primera línea de texto.")
    archivo.escribir_linea("Segunda línea de texto.")
    # El destructor será llamado automáticamente cuando el objeto archivo salga del alcance y sea eliminado

if __name__ == "__main__":
    main()

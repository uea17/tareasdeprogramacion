# Definición de una clase base
class Animal:
    def __init__(self, name, age):
        self.__name = name  # Atributo privado para encapsulación
        self.__age = age

    def speak(self):
        pass  # Método abstracto

    def get_info(self):
        return f'Name: {self.__name}, Age: {self.__age}'

    # Método para obtener el nombre (encapsulación)
    def get_name(self):
        return self.__name

    # Método para establecer el nombre (encapsulación)
    def set_name(self, name):
        self.__name = name


# Definición de una clase derivada
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Llamada al constructor de la clase base
        self.breed = breed

    # Sobrescribir el método speak (polimorfismo)
    def speak(self):
        return "Woof!"

    # Método adicional para la clase derivada
    def get_breed(self):
        return f'Breed: {self.breed}'


# Definición de otra clase derivada
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Llamada al constructor de la clase base
        self.color = color

    # Sobrescribir el método speak (polimorfismo)
    def speak(self):
        return "Meow!"

    # Método adicional para la clase derivada
    def get_color(self):
        return f'Color: {self.color}'


# Creación de instancias y demostración de funcionalidad
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Tabby")

print(dog.get_info())
print(dog.get_breed())
print(dog.speak())

print(cat.get_info())
print(cat.get_color())
print(cat.speak())

# Encapsulación: uso de métodos getter y setter
print(dog.get_name())
dog.set_name("Max")
print(dog.get_name())

# Comentarios explicativos:
# La clase 'Animal' es una clase base con atributos privados 'name' y 'age', y un método abstracto 'speak'.
# La clase 'Dog' hereda de 'Animal', añade un atributo 'breed' y sobrescribe el método 'speak'.
# La clase 'Cat' hereda de 'Animal', añade un atributo 'color' y sobrescribe el método 'speak'.
# Se utiliza encapsulación para proteger los atributos 'name' y 'age'.
# Polimorfismo se demuestra mediante la sobrescritura del método 'speak' en las clases derivadas 'Dog' y 'Cat'.

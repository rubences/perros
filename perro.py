class Perro:
    def __init__(self, nombre, raza, color):
        self.__nombre = nombre
        self.__raza = raza
        self.__color = color

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    def get_color(self):
        return self.__color

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_raza(self, raza):
        self.__raza = raza

    def set_color(self, color):
        self.__color = color

    # Comportamientos
    def menear(self):
        return f"{self.__nombre} está moviendo la cola."

    def ladrar(self):
        return f"{self.__nombre} dice: ¡Guau! ¡Guau!"

    def comer(self, comida):
        return f"{self.__nombre} está comiendo {comida}."

    # Representación en cadena
    def __str__(self):
        return f"Perro(nombre={self.__nombre}, raza={self.__raza}, color={self.__color})"



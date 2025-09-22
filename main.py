from perro import Perro
from gato import Gato
from ejercicio1.circulo import Circulo

if __name__ == "__main__":
    # Ejemplo de uso
    mi_perro = Perro("Max", "Labrador", "Marrón")
    print(mi_perro)
    print(mi_perro.ladrar())
    print(mi_perro.menear())
    print(mi_perro.comer("croquetas"))

    mi_gato = Gato("Pelusa")
    print(mi_gato.maullar())
    print(mi_gato.sentarse())
    print(mi_gato.rodar())

    mi_circulo = Circulo(5)
    print(mi_circulo)
    print("Área del círculo:", mi_circulo.area())
    print("Perímetro del círculo:", mi_circulo.perimetro()) 

    # Otros tipos de perros
    perro1 = Perro("Bella", "Golden Retriever", "Dorado")
    perro2 = Perro("Rocky", "Pastor Alemán", "Negro y Marrón")
    perro3 = Perro("Luna", "Husky Siberiano", "Blanco y Gris")
    perro4 = Perro("Charlie", "Bulldog Francés", "Blanco y Negro")

    print(perro1)
    print(perro2)
    print(perro3)
    print(perro4)


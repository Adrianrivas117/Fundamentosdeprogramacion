from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


class helicoptero(Vehiculo):
    pass
    

# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
helicoptero1 = helicoptero("apache", "boeing", 2021, "verde")
auto2 = Auto("chevrolet", "honda", 2022, "Rojo")
moto2 = Moto("italika", "honda", 2021, "Negra")

# Visualización
print(auto1)
print(moto1)
print(camion1)
print(helicoptero1)
print(auto2)
print(moto2)
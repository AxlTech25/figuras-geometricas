"""Figura Geometrica script"""
from abc import ABC, abstractmethod


class FiguraG(ABC):
    """
    Clase abstracta que representa una figura geométrica.
    """

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""



class Rectangulo(FiguraG):
    """Calcula el área del rectángulo."""
    def __init__(self, base, altura):
        """área del rectángulo."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        area = self.base*self.altura
        return area

    def obtener_base(self):
        """Devuelve la base del rectángulo."""
        return self.base

    def obtener_altura(self):
        """Devuelve la altura del rectángulo."""
        return self.altura

    def imprimir_info(self):
        """Imprime la base, la altura y el área del rectángulo."""
        print(f"Base: {self.base}, Altura: {self.altura}, Área: {self.calcular_area()}")


class Triangulo(FiguraG):
    """Calcula el área del triángulo."""
    def __init__(self, base, altura):
        """área del triángulo."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        area = (self.base*self.altura)/2
        return area
    def obtener_base(self):
        """Devuelve la base del triángulo."""
        return self.base

    def obtener_altura(self):
        """Devuelve la altura del triángulo."""
        return self.altura

    def imprimir_info(self):
        """Imprime la base, altura y área del triángulo."""
        print(f"Base: {self.base}, Altura: {self.altura}, Área: {self.calcular_area()}")

class Circulo(FiguraG):
    """Calcula el área del círculo."""
    def __init__(self, radio):
        """área del círculo."""
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        area = self.pi*(self.radio**2)
        return area

    def calcular_perimetro(self):
        """Calcula el perímetro del círculo."""
        perimetro = 2 * self.pi * self.radio
        return perimetro

    def obtener_radio(self):
        """Devuelve el radio del círculo."""
        return self.radio

    def imprimir_info(self):
        """Imprime el radio, área y perímetro del círculo."""
        print(f"Radio: {self.radio}, Área: {self.calcular_area()}, "
              f"Perímetro: {self.calcular_perimetro()}")

# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")

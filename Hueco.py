import random
from Pieza import *


class Hueco:
    def __init__(self, entradas=None):
        if entradas is None:
            entradas = [random.randint(0, 1), random.randint(0, 1)]
        self.a = a
        self.b = b
        self.salida = None
        self.Pieza = None

    def hay_pieza(self):
        """

        :return:
        """
        return self.Pieza is not None

    def meter(self, Pieza):
        """
        Importante, antes comprobar que esta vacio
        :return:
        """
        self.Pieza = Pieza

    def sacar(self, Pieza):
        self.Pieza = None


if __name__ == '__main__':
    n = Hueco()
    print(n.a)
    print(n.b)
    print(n.salida)

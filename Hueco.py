import random
from Pieza import *

# (WIDTH, HEIGHT)
cordenadas1 = 210, 75
cordenadas2 = 90, 240
cordenadas3 = 330, 240
tamanyo = 58, 120


class Hueco:
    def __init__(self, cordenadas, tamanyo, entradas=None):
        if entradas is None:
            entradas = [random.randint(0, 1), random.randint(0, 1)]

        self.a = entradas[0]
        self.b = entradas[1]
        self.cordenadas = cordenadas
        self.tamanyo = tamanyo
        self.salida = None
        self.Pieza = None
        # H1 = Hueco(cordenadas1, tamanyo, [1, 0])
        # H2 = Hueco(cordenadas2, tamanyo, [0, 1])
        # H3 = Hueco(cordenadas3, tamanyo, [H1.salida, H2.salida])

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
    H1 = Hueco(cordenadas1, tamanyo, [1, 0])
    H2 = Hueco(cordenadas2, tamanyo, [0, 1])
    H3 = Hueco(cordenadas3, tamanyo, [H1.salida, H2.salida])


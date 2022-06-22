import random
from Pieza import *

# (WIDTH, HEIGHT)
cordenadas1 = 210, 75
cordenadas2 = 90, 240
cordenadas3 = 330, 240
tamanyo = 58, 120


class Hueco:
    def __init__(self, cordenadas, tamanyo):
        self.cordenadas = cordenadas
        self.tamanyo = tamanyo
        self.salida = None
        self.Pieza = None

    def hay_pieza(self):
        """
        :return:
        """
        return self.Pieza is not None

    def meter(self, Pieza):
        """
        Importante, antes comprobar que esta vacio.
        :return:
        """
        self.Pieza = Pieza

    def sacar(self, Pieza):
        self.Pieza = None

    def comp(self, inputs):
        return self.Pieza.comp(inputs)

if __name__ == '__main__':
    from AND import *

    H1 = Hueco([], [])
    H1.meter(AND())
    print(H1.comp([0, 1]))


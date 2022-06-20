import random


class Pieza:
    # Definicion del comportamiento de las piezas en general
    def __init__(self,tamanyo, cordenadas=None, entradas=None):

        if entradas is None:
            entradas = [random.randint(0, 1), random.randint(0, 1)]

        self.a = entradas[0]
        self.b = entradas[1]

        self.cordenadas = [40, 90, 75, 210, 240, 330, 475, 576]
        self.tamanyo = (58, 120)
        self.salida = None


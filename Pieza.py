import random

tamanyo = 58, 120


class Pieza:
    # Definicion del comportamiento de las piezas en general
    def __init__(self, cordenadas, tamanyo,  entradas=None):

        if entradas is None:
            entradas = [random.randint(0, 1), random.randint(0, 1)]

        self.a = entradas[0]
        self.b = entradas[1]
        self.cordenadas = cordenadas
        self.tamanyo = tamanyo
        self.salida = None


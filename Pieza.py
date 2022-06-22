import random


class Pieza:
    # Definicion del comportamiento de las piezas en general
    def __init__(self, tamanyo=None, cordenadas=None):

        self.cordenadas = [40, 90, 75, 210, 240, 330, 475, 576]
        self.tamanyo = (58, 120)
        self.salida = None
        self.entradas = None

    def comp(self, inputs):
        pass


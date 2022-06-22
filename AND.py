from Pieza import *
import pygame
from pygame.locals import *


class AND(Pieza):

    def __init__(self, tamanyo=None, cordenadas=None):
        super().__init__(tamanyo, cordenadas)

        self.image = pygame.image.load('FOTOS/AND.png')
        self.pos = (self.cordenadas[1], self.cordenadas[6])
        self.tamanyo = self.tamanyo
        self.entradas = 2

    def comp(self, inputs):
        # Comportamineto de la Puerta logica
        if len(inputs) != self.entradas:
            raise LoQueSea
        self.salida = inputs[0] and inputs[1]
        return self.salida


if __name__ == '__main__':
    n = AND()
    print(n.pos)
    print(n.tamanyo)

    n.comp([0, 1])
    print(n.salida)
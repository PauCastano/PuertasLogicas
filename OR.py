from Pieza import *
import pygame
from pygame.locals import *


class OR(Pieza):
    pygame.init()

    def __init__(self, tamanyo=None, cordenadas=None):
        super().__init__(tamanyo, cordenadas)

        self.image = pygame.image.load('FOTOS/OR.png')
        self.rect = self.image.get_rect()
        self.pos = (self.cordenadas[1], self.cordenadas[6])
        self.tamanyo = self.tamanyo
        self.entradas = 2

    def comp(self, inputs):
        # Comportamineto de la Puerta logica
        if len(inputs) != self.entradas:
            raise LoQueSea
        self.salida = inputs[0] or inputs[1]
        return self.salida


if __name__ == '__main__':
    n = OR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
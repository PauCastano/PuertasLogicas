from Pieza import *
import pygame
from pygame.locals import *


class OR(Pieza):
    pygame.init()

    def __init__(self, tamanyo=None, cordenadas=None, entradas=None):
        super().__init__(tamanyo, cordenadas, entradas)

        self.image = pygame.image.load('FOTOS/OR.png')
        self.pos = (self.cordenadas[3], self.cordenadas[6])
        self.tamanyo = self.tamanyo

    def comp(self, input):
        # Comportamineto de la Puerta logica
        self.salida = self.a or self.b
        return self.salida


if __name__ == '__main__':
    n = OR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
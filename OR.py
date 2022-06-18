from Pieza import *
import pygame
from pygame.locals import *


class OR(Pieza):
    def __init__(self, entradas=None, cordenadas=None):
        super().__init__(cordenadas, tamanyo,  entradas)
        self.image = pygame.image.load('FOTOS/OR.png')

    def comp(self, entradas):
        # Comportamineto de la Puerta logica
        self.salida = self.a or self.b
        return self.salida


if __name__ == '__main__':
    n = OR()
    n.comp()
    print(n.a)
    print(n.b)
    print(n.salida)
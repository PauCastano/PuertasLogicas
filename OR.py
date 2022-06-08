from Pieza import *
import pygame
from pygame.locals import *


class OR(Pieza):
    pygame.init()

    def __init__(self, entradas=None, cordenadas=None):
        super().__init__(cordenadas, tamanyo,  entradas=None)
        self.image = pygame.image.load('FOTOS/OR.png')

        if entradas is None:
            entradas = [random.randint(0, 1), random.randint(0, 1)]
        self.entrada1 = entradas[0]
        self.entrada2 = entradas[1]

    def comp(self, entradas):
        # Comportamineto de la Puerta logica
        self.salida = self.entrada1 or self.entrada2
        return self.salida


if __name__ == '__main__':
    n = OR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
from Pieza import *
import pygame
from pygame.locals import *


class NAND(Pieza):

    def __init__(self, entradas=None, cordenadas=None):
        super().__init__(cordenadas, tamanyo, entradas)
        self.image = pygame.image.load('FOTOS/NAND.png')


    def comp(self, entradas):
        # Comportamineto de la Puerta logica
        self.salida = int(not (self.a and self.b))
        return self.salida


if __name__ == '__main__':
    n = NAND()
    n.comp()
    print(n.a)
    print(n.b)
    print(n.salida)
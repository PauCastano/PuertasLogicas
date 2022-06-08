from Pieza import *
import pygame
from pygame.locals import *


class NAND(Pieza):
    pygame.init()

    def __init__(self, entradas=None):
        super().__init__(entradas)
        self.image = pygame.image.load('FOTOS/NAND.png')

        if entradas is None:
           entradas = [random.randint(0, 1), random.randint(0, 1)]

        self.entrada1 = entradas[0]
        self.entrada2 = entradas[1]

    def comp(self, entradas):
        # Comportamineto de la Puerta logica
        self.salida = int(not (self.entrada1 and self.entrada2))
        return self.salida


if __name__ == '__main__':
    n = NAND()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
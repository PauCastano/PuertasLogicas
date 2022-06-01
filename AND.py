from Pieza import *
import pygame
from pygame.locals import *


class AND(Pieza):
    pygame.init()

    def __init__(self, entradas=None):
       # super().__init__(entrada1, entrada2)
        self.image = pygame.image.load('FOTOS/AND.png')

        if entradas is None:
            entradas = [random.randint(0, 1), random.randint(0, 1)]
        self.entrada1 = entradas[0]
        self.entrada2 = entradas[1]


    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = self.entrada1 and self.entrada2


if __name__ == '__main__':
    n = AND()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
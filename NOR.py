from Hueco import *
import pygame
from pygame.locals import *


class NOR(Pieza):
    pygame.init()

    def __init__(self, entradas=None):
        #super().__init__(entrada1, entrada2)
        self.image = pygame.image.load('FOTOS/NOR.png')
        if entradas is None:
            entradas = [random.randint(0, 1), random.randint(0, 1)]
        self.entrada1 = entradas[0]
        self.entrada2 = entradas[1]

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = int(not (self.entrada1 or self.entrada2))

if __name__ == '__main__':
    n = NOR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
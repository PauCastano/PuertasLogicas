from Pieza import *
import pygame
from pygame.locals import *


class AND(Pieza):
    pygame.init()

    def __init__(self, entrada1=0, entrada2=0):
        super().__init__(entrada1, entrada2)
        self.image = pygame.image.load('FOTOS/AND.png')

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = self.entrada1 and self.entrada2


if __name__ == '__main__':
    n = AND()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
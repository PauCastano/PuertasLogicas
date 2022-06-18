from Pieza import *
import pygame
from pygame.locals import *


class AND(Pieza):

    def __init__(self, entradas=None, cordenadas=None):
        super().__init__(cordenadas, tamanyo,  entradas)
        self.image = pygame.image.load('FOTOS/AND.png')

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = self.a and self.b
        return self.salida


if __name__ == '__main__':
    n = AND()
    n.comp()

    print(n.a)
    print(n.b)
    print(n.salida)
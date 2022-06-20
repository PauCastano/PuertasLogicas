from Pieza import *
import pygame
from pygame.locals import *


class AND(Pieza):

    def __init__(self,tamanyo=None, cordenadas=None, entradas=None):
        super().__init__(tamanyo, cordenadas, entradas)

        self.image = pygame.image.load('FOTOS/AND.png')
        self.pos = (self.cordenadas[1], self.cordenadas[6])
        self.tamanyo = self.tamanyo

    def comp(self, input):
        # Comportamineto de la Puerta logica
        self.salida = self.a and self.b
        return self.salida


if __name__ == '__main__':
    n = AND()
    print(n.pos)
    print(n.tamanyo)

    n.comp()
    print(n.a)
    print(n.b)
    print(n.salida)
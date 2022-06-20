from Pieza import *
import pygame
from pygame.locals import *


class AND(Pieza):

    def __init__(self, cordenadas, tamanyo, entradas=None):
        super().__init__(cordenadas, tamanyo, entradas)

        self.image = pygame.image.load('FOTOS/AND.png')
        self.pos = (cordenadas[1], cordenadas[6])
        self.tamanyo = tamanyo

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = self.a and self.b
        return self.salida


if __name__ == '__main__':
    n = AND([40, 90, 100, 210, 260, 330, 400, 576], (58, 120))
    print(n.pos)
    print(n.tamanyo)

    n.comp()
    print(n.a)
    print(n.b)
    print(n.salida)
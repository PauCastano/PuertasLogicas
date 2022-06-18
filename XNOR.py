from Pieza import *
import pygame
from pygame.locals import *


class XNOR(Pieza):
    def __init__(self, entradas=None, cordenadas=None):
        super().__init__(cordenadas, tamanyo,  entradas)
        self.image = pygame.image.load('FOTOS/XNOR.png')

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = int(not (self.a ^ self.b))


if __name__ == '__main__':
    n = XNOR()
    n.comp()
    print(n.a)
    print(n.b)
    print(n.salida)
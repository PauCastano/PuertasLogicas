from Pieza import *
import pygame
from pygame.locals import *


class XOR(Pieza):
    def __init__(self, entradas=None, cordenadas=None):
        super().__init__(cordenadas, tamanyo,  entradas)
        self.image = pygame.image.load('FOTOS/XOR.png')

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = self.a^self.b


if __name__ == '__main__':
    n = XOR()
    n.comp()
    print(n.a)
    print(n.b)
    print(n.salida)
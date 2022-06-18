from Hueco import *
import pygame
from pygame.locals import *


class NOR(Pieza):

    def __init__(self, entradas=None, cordenadas=None):
        super().__init__(cordenadas, tamanyo, entradas)
        self.image = pygame.image.load('FOTOS/NOR.png')

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = int(not (self.a or self.b))

if __name__ == '__main__':
    n = NOR()
    n.comp()
    print(n.a)
    print(n.b)
    print(n.salida)
from Pieza import *
import pygame
from pygame.locals import *


class NOR(Pieza):
    pygame.init()

    def __init__(self, entrada1=0, entrada2=0):
        super().__init__(entrada1, entrada2)
        self.image = pygame.image.load('FOTOS/NOR.png')

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = int(not (self.entrada1 or self.entrada2))
if __name__ == '__main__':
    n = NOR()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
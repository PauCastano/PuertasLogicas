from Pieza import *
import pygame
from pygame.locals import *


class NAND(Pieza):
    pygame.init()

    def __init__(self, entrada1=0, entrada2=0):
        super().__init__(entrada1, entrada2)
        self.image = pygame.image.load('FOTOS/NAND.png')

    def comp(self):
        # Comportamineto de la Puerta logica
        self.salida = int( not (self.entrada1 and self.entrada2))

# COMPROVAR QUE FUNCIONA BIEN


if __name__ == '__main__':
    n = NAND()
    n.comp()
    print(n.entrada1)
    print(n.entrada2)
    print(n.salida)
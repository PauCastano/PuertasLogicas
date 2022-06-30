from Pieza import *
import pygame


class NOR(Pieza):
    pygame.init()

    def __init__(self, tamanyo=None, cordenadas=None):
        super().__init__(tamanyo, cordenadas)

        self.image = pygame.image.load('FOTOS/NOR.png')
        self.rect = self.image.get_rect()
        self.pos = (self.cordenadas[3], self.cordenadas[7])
        self.tamanyo = self.tamanyo
        self.entradas = 2

    def comp(self, inputs):
        # Comportamineto de la Puerta logica
        if len(inputs) != self.entradas:
            raise Exception("Faltan entradas")
        self.salida = not (inputs[0] or inputs[1])
        self.salida = int(self.salida)
        return self.salida


if __name__ == '__main__':
    n = NOR()
    print(n.pos)
    print(n.tamanyo)

    n.comp([0, 1])
    print(n.salida)
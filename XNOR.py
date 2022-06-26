from Pieza import *
import pygame


class XNOR(Pieza):
    pygame.init()

    def __init__(self, tamanyo=None, cordenadas=None):
        super().__init__(tamanyo, cordenadas)

        self.image = pygame.image.load('FOTOS/XNOR.png')
        self.rect = self.image.get_rect()
        self.pos = (self.cordenadas[5], self.cordenadas[7])
        self.tamanyo = self.tamanyo
        self.entradas = 2

    def comp(self,inputs):
        # Comportamineto de la Puerta logica
        if len(inputs) != self.entradas:
            raise Exception("Faltan entradas")
        self.salida = not (inputs[0] ^ inputs[1])
        return self.salida


if __name__ == '__main__':
    n = XNOR()
    n.comp()
    print(n.a)
    print(n.b)
    print(n.salida)
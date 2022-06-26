from Pieza import *
import pygame


class AND(Pieza):
    pygame.init()

    def __init__(self, tamanyo=None, cordenadas=None):
        super().__init__(tamanyo, cordenadas)

        self.image = pygame.image.load('FOTOS/AND.png')
        self.rect = self.image.get_rect()
        self.pos = (self.cordenadas[1], self.cordenadas[6])
        self.tamanyo = self.tamanyo
        self.entradas = 2

    def comp(self, inputs):
        # Comportamineto de la Puerta logica
        if len(inputs) != self.entradas:
            raise Exception("Faltan entradas")
        self.salida = inputs[0] and inputs[1]
        return self.salida

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]



if __name__ == '__main__':
    n = AND()
    print(n.pos)
    print(n.tamanyo)

    n.comp([0, 1])
    print(n.salida)
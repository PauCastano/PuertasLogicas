import random
import pygame


class Pieza(pygame.sprite.Sprite):
    # Definicion del comportamiento de las piezas en general
    def __init__(self, tamanyo=None, cordenadas=None):
        super().__init__()

        self.cordenadas = [40, 90, 75, 210, 240, 330, 425, 525]
        self.tamanyo = (58, 120)
        self.salida = None
        self.entradas = None

    def comp(self, inputs):
        pass

    def update(self):
        pass

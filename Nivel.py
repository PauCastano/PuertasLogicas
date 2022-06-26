import random
import pygame
from pygame.locals import *
import os
import sys
from AND import *
from OR import *


class Nivel:
    pygame.init()

    def __init__(self, n_input, piezas = []):

        self.caracteristcas = [random.randint(0, 1) for i in
                               range(n_input + 1)]  # devuelve una lista de 5 valores entre 0 y 1,
        self.input = self.caracteristcas[:2]  # en esta lista estan los inputs y los outputs
        self.output = self.caracteristcas[-1]
        self.n_hueco = n_input - 1
        self.piezas = [OR()]  # listado de piezas utilizado en el nivel
        self.posible_solucion = []

    def rellenar_huecos(self):
#Poner piezas aleatorias para cada hueco
        if self.piezas[0].comp(self.input) == self.output:
            self.posible_solucion.append(self.piezas[0])

    def comp(self, inputs):
        pass


if __name__ == '__main__':
    n = Nivel(2)

    print('Entradas:', n.input)
    print('Salida querida:', n.output)
    print('Resultado:', n.piezas[0].comp(n.input))
    print(n.posible_solucion)



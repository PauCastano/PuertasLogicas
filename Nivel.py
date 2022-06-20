import random
import pygame
from pygame.locals import *
import os
import sys
from AND import *


class Nivel:
    pygame.init()

    def __init__(self, n_input, pieza = []):

        self.caracteristcas = [random.randint(0, 1) for i in
                               range(n_input + 1)]  # devuelve una lista de 5 valores entre 0 y 1,
        self.input = self.caracteristcas[:2]  # en esta lista estan los inputs y los outputs
        self.output = self.caracteristcas[-1]
        self.n_hueco = n_input - 1
        self.pieza = [AND()]  # listado de piezas utilizado en el nivel
        self.posible_solucion = []

    def rellenar_huecos(self):

        if self.pieza[0].comp(self.input) == self.output:
            self.posible_solucion.append(self.pieza[0])


if __name__ == '__main__':
    n = Nivel(2)

    print('Entradas:', n.input)
    print('Salida querida:', n.output)
    print('Resultado:', n.pieza[0].comp(n.input))
    print(n.posible_solucion)



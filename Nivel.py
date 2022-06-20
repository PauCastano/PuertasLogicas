import random
import pygame
from pygame.locals import *
import os
import sys
from AND import *
from NAND import *
from OR import *


class Nivel:
    pygame.init()

    def __init__(self, n_input, pieza = []):

        self.caracteristcas = [random.randint(0, 1) for x in range(n_input)]    # devuelve una lista de 5 valores entre 0 y 1,
        self.input = self.caracteristcas[:4]                                   # en esta lista estan los inputs y los outputs
        self.output = 1
        self.n_hueco = n_input - 1
        self.pieza = pieza  # listado de piezas utilizado en el nivel
        self.posible_solucion = []

    def rellenar_huecos(self):

        for x in range(len(self.pieza)):

            random.shuffle(self.pieza)

            for i in self.pieza:

                if (self.pieza[0].comp([(self.pieza[1].comp(self.input[:2])),
                                       (self.pieza[2].comp(self.input[2:4]))])) == self.output:

                    self.posible_solucion.append(self.pieza[0], self.pieza[1], self.pieza[2])


if __name__ == '__main__':
    n = Nivel(2, [AND()])

    print(n.input)
    print('AND', n.pieza[0].comp(n.input[:2]))
    # print('OR', n.pieza[1].comp(n.input[:2]))
    # print(n.pieza[2].comp([(n.pieza[0].comp(n.input[:2])),
    #                                  (n.pieza[1].comp(n.input[2:4]))]))
    print(n.posible_solucion)



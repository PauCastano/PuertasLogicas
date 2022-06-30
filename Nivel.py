import random
import pygame
from pygame.locals import *
import os
import sys
from NAND import *
from OR import *
from NOR import *
from XOR import *
from XNOR import *
from Hueco import *
from AND import *
import itertools


class Nivel:
    pygame.init()

    def __init__(self, n_input, piezas = []):

        self.input = [random.randint(0, 1) for i in
                               range(n_input)]  # devuelve una lista de 5 valores entre 0 y 1,
        self.output = 1
        self.n_hueco = n_input - 1
        self.piezas = [OR(), AND(), NOR(), NAND(), XOR(), XNOR()]  # listado de piezas utilizado en el nivel
        self.posible_solucion = []

    def comp(self):
#Poner piezas aleatorias para cada hueco
        H1 = Hueco()
        H1.rect.x = 210
        H1.rect.y = 75

        H2 = Hueco()
        H2.rect.x = 90
        H2.rect.y = 240

        H3 = Hueco()
        H3.rect.x = 330
        H3.rect.y = 240
        perm_puertas = list(itertools.product(self.piezas, repeat = 3)) #tupla
        comb_puertas = [] #lista con todas las permutaciones posibles

        for q in range(len(perm_puertas)):
            comb_puertas.append(perm_puertas[q][0])
            comb_puertas.append(perm_puertas[q][1])
            comb_puertas.append(perm_puertas[q][2])

        k = 0
        for count, puertax in enumerate(comb_puertas):
            if k < len(comb_puertas):

                pieza1 = comb_puertas[k]
                pieza2 = comb_puertas[k+1]
                pieza3 = comb_puertas[k+2]

                H1.meter(pieza1)
                H2.meter(pieza2)
                H3.meter(pieza3)

                resultado_intermedio = []
                resultado_intermedio.append(H2.comp(self.input[:2]))
                resultado_intermedio.append(H3.comp(self.input[2:4]))

                if H1.comp(resultado_intermedio) == 1:
                    self.posible_solucion.extend((pieza2, pieza3, pieza1))

                H1.sacar(pieza1)
                H2.sacar(pieza2)
                H3.sacar(pieza3)
                k += 3


if __name__ == '__main__':
    n = Nivel(4)
    n.comp()
    print('Entradas:', n.input)
    print('Salida querida:', n.output)
    print('Resultado:', n.posible_solucion)



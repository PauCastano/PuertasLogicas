import random
import pygame
from pygame.locals import *
import os
import sys
from OR import *
from AND import *
from Hueco import *

class Nivel:
    pygame.init()

    def __init__(self, n_input, piezas = []):

        self.input = [random.randint(0, 1) for i in
                               range(n_input)]  # devuelve una lista de 5 valores entre 0 y 1,
        self.output = 1
        self.n_hueco = n_input - 1
        self.piezas = [OR(), AND()]  # listado de piezas utilizado en el nivel
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

        pieza1 = random.choice(self.piezas)
        pieza2 = random.choice(self.piezas)
        pieza3 = random.choice(self.piezas)

        H1.meter(pieza1)
        H2.meter(pieza2)
        H3.meter(pieza3)

        resultado_intermedio = []
        resultado_intermedio.append(H2.comp(self.input[:2]))
        resultado_intermedio.append(H3.comp(self.input[2:4]))
        print('RESULTADO FINAL:', H1.comp(resultado_intermedio) )
        if H1.comp(resultado_intermedio) == 1:
            self.posible_solucion.extend((pieza2, pieza3, pieza1))
        print('soluciones', self.posible_solucion)

    def comp123(self, inputs):
        pass


if __name__ == '__main__':
    n = Nivel(4)
    n.comp()
    print('Entradas:', n.input)
    print('Salida querida:', n.output)
    print('Resultado:')
    print(n.posible_solucion)



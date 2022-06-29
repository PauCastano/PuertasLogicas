import random
import pygame
from pygame.locals import *
import os
import sys
from Button import *
from AND import *
from NAND import *
from OR import *
from NOR import *
from XOR import *
from XNOR import *
from Hueco import *
from Nivel import *


def main():

    running = True
    moving = False

    lista_huecos = pygame.sprite.Group()
    lista_puertas = pygame.sprite.Group()
    lista_todos_sprites = pygame.sprite.Group()

    H1 = Hueco()
    H1.rect.x = 210
    H1.rect.y = 75

    H2 = Hueco()
    H2.rect.x = 90
    H2.rect.y = 240

    H3 = Hueco()
    H3.rect.x = 330
    H3.rect.y = 240

    P_AND = AND()
    P_AND.rect.x = AND().pos[0]
    P_AND.rect.y = AND().pos[1]

    P_NAND = NAND()
    P_NAND.rect.x = NAND().pos[0]
    P_NAND.rect.y = NAND().pos[1]

    P_OR = OR()
    P_OR.rect.x = OR().pos[0]
    P_OR.rect.y = OR().pos[1]

    P_NOR = NOR()
    P_NOR.rect.x = NOR().pos[0]
    P_NOR.rect.y = NOR().pos[1]

    P_XOR = XOR()
    P_XOR.rect.x = XOR().pos[0]
    P_XOR.rect.y = XOR().pos[1]

    P_XNOR = XNOR()
    P_XNOR.rect.x = XNOR().pos[0]
    P_XNOR.rect.y = XNOR().pos[1]

    lista_huecos.add(H1, H2, H3)
    lista_puertas.add(P_NAND, P_AND, P_OR, P_NOR, P_XOR, P_XNOR)
    lista_todos_sprites.add(H1, H2, H3, P_AND, P_NAND, P_OR, P_XOR, P_XNOR, P_NOR)

    nivel = Nivel(4)

    in1 = str(nivel.input[0])
    in2 = str(nivel.input[1])
    in3 = str(nivel.input[2])
    in4 = str(nivel.input[3])
    print(in1, in2, in3, in4)

    solucion_propuesta = []
    posibles_soluciones = []
    resultado_inetrmedio = []

    listado_puertas = [P_NAND, P_AND, P_OR, P_NOR, P_XOR, P_XNOR]

    for r in listado_puertas:
        # nivel.r.comp(nivel.input[:2])
        H1.meter(r)
        resultado_inetrmedio.append(int(H1.comp(nivel.input[:2])))
        solucion_propuesta.append(r)
        H1.sacar(r)
        listado_puertas.remove(r)
        print(listado_puertas)

        for x in listado_puertas:
            H2.meter(x)
            resultado_inetrmedio.append(int(H2.comp(nivel.input[2:4])))
            solucion_propuesta.append(x)
            H2.sacar(x)
            listado_puertas.remove(x)

            for z in listado_puertas:
                H3.meter(z)
                print(r, x, z)
                print(resultado_inetrmedio)
                resultado_final = int(H3.comp(resultado_inetrmedio))
                solucion_propuesta.append(z)
                print(resultado_final)
                H3.sacar(z)
                listado_puertas.remove(z)

                if resultado_final == 1:
                    posibles_soluciones.append(solucion_propuesta)
                    print('soluciones:', posibles_soluciones)
                    solucion_propuesta = []

                else:
                    solucion_propuesta = []


if __name__ == "__main__":
    main()





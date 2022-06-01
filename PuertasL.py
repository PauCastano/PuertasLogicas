# ***********************************************************
# Programa Puertas logicas PRE (PROGRAMACIÓ PER A ENGINYERS)
# Curso Primavera 2021-2022
# Nombres:
#           Ariadna Delriu Carulla
#           Pau Castaño i Ferré
#           Guillem Rovira Herrero
# ***********************************************************


# ***************************
# Importacion de los modulos
# ***************************


import pygame
from pygame.locals import *
import os
import sys

import Hueco
from AND import *
from NAND import *
from NOR import *
from OR import *
from XNOR import *
from XOR import *
from Hueco import *

# ***********
# Constantes
# ***********

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
IMG_DIR = "FOTOS"
Amarillo = (255, 255, 0)
Blanco = (255, 255, 255)
# (WIDTH, HEIGHT)
cordenadas1 = 211, 100
cordenadas2 = 91, 260
cordenadas3 = 331, 260
tamanyo = 90, 90
resultado = 0

# ******************************
# Clases y Funciones utilizadas
# ******************************

class nivel:
    def __init__(self,):
def load_image(nombre, IMG_DIR, alpha=False):
    ruta = os.path.join(IMG_DIR, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


# Todas las puertas logicas heredan de la clase Pieza

def main():
    pygame.init()

    H1 = Hueco(cordenadas1, tamanyo, [1, 0])
    H2 = Hueco(cordenadas2, tamanyo, [0, 1])
    H3 = Hueco(cordenadas3, tamanyo, [H1.salida, H2.salida])

    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fondo = pygame.image.load('FOTOS/FONDO.jpg')

    # image = NOR().image
    # image.convert()
    #
    # rect = image.get_rect()
    # rect.center = SCREEN_WIDTH*1.5//3, SCREEN_HEIGHT*3.5//5 # En cada porta

    # P_NOR = NOR().image.get_rect()
    # P_NOR.center = SCREEN_WIDTH * 1.5 // 3, SCREEN_HEIGHT * 3.5 // 5

    P_AND = AND().image.get_rect()
    P_AND.center = SCREEN_WIDTH * 1.5 // 3, SCREEN_HEIGHT * 4.5 // 5

    # P_OR = OR().image.get_rect()
    # P_OR.center = SCREEN_WIDTH*0.5//3, SCREEN_HEIGHT*4.5//5
    #
    # P_XOR = XOR().image.get_rect()
    # P_XOR.center = SCREEN_WIDTH * 0.5 // 3, SCREEN_HEIGHT * 3.5 // 5

    #Hueco1 = pygame.Rect(((SCREEN_WIDTH*1.5 // 3)-29, (SCREEN_WIDTH*1.5 // 5)-60), (58, 120))
    Hueco1 = pygame.Rect(H1.cordenadas, H1.tamanyo)
    Hueco2 = pygame.Rect(H2.cordenadas, H2.tamanyo)
    Hueco3 = pygame.Rect(H3.cordenadas, H3.tamanyo)

# collide = pygame.Rect.colliderect(object,rect2)

    running = True
    moving = False

    portes = [P_AND]
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                for r in portes:
                    if r.collidepoint(event.pos):
                        moving = True

            elif event.type == MOUSEMOTION and moving:
                for r in portes:
                    if r.collidepoint(event.pos):
                        r.move_ip(event.rel)

                    # if Hueco1.top == r.top:
                    #     Hueco.H1.hay_pieza()
                    #
                    # elif Hueco2.top == r.top:
                    #     Hueco.H2.hay_pieza()
                    #
                    # elif Hueco3.top == r.top:
                    #     Hueco.H3.hay_pieza()

            elif event.type == MOUSEBUTTONUP:
                moving = False

            # elif Hueco.H1.hay_pieza() and Hueco.H2.hay_pieza() and Hueco.H3.hay_pieza():
            #     if Hueco.H3.salida == 1:
            #         resultado = 1
            #     else:
            #         resultado = 0


        # L'ordre en que fem les figures importa en quines estan en primera fila
        screen.blit(fondo,(0,0))
        pygame.draw.rect(screen, Amarillo, Hueco1)
        pygame.draw.rect(screen, Amarillo, Hueco2)
        pygame.draw.rect(screen, Amarillo, Hueco3)
        # screen.blit(NOR().image, P_NOR)
        screen.blit(AND().image, P_AND)
        # screen.blit(OR().image, P_OR)
        # screen.blit(XOR().image, P_XOR)

        pygame.display.update()


if __name__ == "__main__":
    main()
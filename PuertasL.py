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
from Pieza import *

import pygame
from pygame.locals import *
import os
import sys

# ***********
# Constantes
# ***********

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
IMG_DIR = "FOTOS"

# ******************************
# Clases y Funciones utilizadas
# ******************************


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




YELLOW = (255, 255, 0)


# Todas las puertas logicas heredan de la clase Pieza

def main():
    pygame.init()


    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    image = pygame.image.load('FOTOS/BE.png')
    image.convert()

    rect = image.get_rect()
    rect.center= SCREEN_WIDTH//2, SCREEN_WIDTH//2

    image2 = pygame.image.load('FOTOS/BE.png')
    image2.convert()

    rect2 = image.get_rect()
    rect2.center = SCREEN_WIDTH // 4, SCREEN_WIDTH // 4

    running = True
    moving = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    moving = True
            elif event.type == MOUSEBUTTONUP:
                moving = False
            elif event.type == MOUSEMOTION  and moving:
                rect.move_ip(event.rel)

        screen.fill(YELLOW)
        screen.blit(image, rect)

        pygame.display.update()


if __name__ == "__main__":
    main()
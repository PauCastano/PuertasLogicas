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

# ***********
# Constantes
# ***********

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
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




Amarillo = (255, 255, 0)
Blanco = (255, 255, 255)


# Todas las puertas logicas heredan de la clase Pieza

def main():
    pygame.init()


    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    image = pygame.image.load('FOTOS/AND.png')
    image.convert()

    rect = image.get_rect()
    rect.center= SCREEN_WIDTH//2, SCREEN_WIDTH//2

    image2 = pygame.image.load('FOTOS/BE.png')
    image2.convert()

    rect2 = image2.get_rect()
    rect2.center = 500, 200

    object = pygame.Rect((SCREEN_WIDTH // 4, SCREEN_WIDTH // 4), (200, 200))


   # collide = pygame.Rect.colliderect(object,rect2)

    running = True
    moving = False

    portes = [rect, rect2]
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

                if object.top == rect2.top:
                    rect2.top = object.top
                    rect2.left = object.left


            elif event.type == MOUSEBUTTONUP:
                moving = False


        # L'ordre de les en que fem les figures importa en quines estan en primera fila
        screen.fill(Amarillo)
        pygame.draw.rect(screen, Blanco, object)
        screen.blit(image, rect)
        screen.blit(image2, rect2)


        pygame.display.update()


if __name__ == "__main__":
    main()
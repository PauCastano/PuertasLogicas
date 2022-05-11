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

https://www.youtube.com/watch?v=ZFI4vExV2F0

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






# Todas las puertas logicas heredan de la clase Pieza

def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = load_image("FONDO.jpg", IMG_DIR, alpha=False)
    # Ajustem l'escala del fons
    fondo = pygame.transform.scale(fondo,(640, 480))
    # Girem el fons 90º
    fondo = pygame.transform.rotate(fondo, 90)


    screen.blit(fondo, (0, 0))
    screen.blit(tux, (300, 300))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()
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

https://programmerclick.com/article/70961779601/




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

    ventana = pygame.display.set_mode((600,300))
    pygame.display.set_caption("Tutorial")
    posX=200
    posY = 100
    velocidad = 2
    Blanco=(255, 255, 255)
    derecha = True
    rectangulo = pygame.Rect(0,0,100,150)
    rectangulo_dos = pygame.Rect(300, 300, 100, 150)
    # el bucle principal del juego
    while True:

        ventana.fill(Blanco)
        pygame.draw.rect(ventana, (180, 70, 70), rectangulo_dos)
        pygame.draw.rect(ventana, (180, 70, 70), rectangulo)
        rectangulo.left, rectangulo.top = pygame.mouse.get_pos()

        if rectangulo.colliderect(rectangulo_dos):
            velocidad = 0
            print("Colisiono")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if derecha == True:
            if posX < 400:
                posX += velocidad
                rectangulo_dos.left = posX
            else:
                derecha = False
        else:
            if posX > 1:
                posX -= velocidad
                rectangulo_dos.left = posX
            else:
                derecha = True

if __name__ == "__main__":
    main()
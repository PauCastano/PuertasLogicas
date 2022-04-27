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

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
IMG_DIR = "imagenes"

# ******************************
# Clases y Funciones utilizadas
# ******************************


def load_image(nombre, dir_imagen, alpha=False):
    ruta = os.path.join(dir_imagen, nombre)
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



class Pieza:
    # Definicion del comportamiento de las piezas en general
    def __init__(self, entrada1 = 0, entrada2 = 0):
        self.entrada1 = entrada1
        self.entrada2 = entrada2

    def mov(self):
        self.speed = [4, 4]


# Todas las puertas logicas heredan de la clase Pieza
class AND(Pieza):

    def __init__(self):
        super(AND, self).__init__()
        self.image = load_image("AND.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1 and self.entrada2 == 1:
            salida = 1
        else:
            salida = 0
        return salida

class OR(Pieza):

    def __init__(self):
        super(OR, self).__init__()
        self.image = load_image("OR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1:
            salida = 1
        elif self.entrada2 == 1:
           salida = 1
        else:
            salida = 0
        return salida

class XOR(Pieza):
    def __init__(self):
        super(XOR, self).__init__()
        self.image = load_image("XOR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 != self.entrada2:
            salida = 1
        else:
            salida = 0
        return salida

class NAND(Pieza):
    def __init__(self):
        super(NAND, self).__init__()
        self.image = load_image("NAND.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == 1 and self.entrada2 == 1:
            salida = 0
        else:
            salida = 1
        return salida

class NOR(Pieza):
    def __init__(self):
        super(NOR, self).__init__()
        self.image = load_image("NOR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if (self.entrada1 == 0) and (self.entrada2 == 0):
            salida = 1
        else:
            salida = 0
        return salida

class XNOR(Pieza):
    def __init__(self):
        super(XNOR, self).__init__()
        self.image = load_image("XNOR.png", IMG_DIR, alpha=True)

    def comp(self):
        # Comportamineto de la Puerta logica
        if self.entrada1 == self.entrada2:
            salida = 1
        else:
            salida = 0
        return salida

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Juego puertas logicas")
    fondo = load_image("fondo.jpg", IMG_DIR, alpha=False)

if __name__ == "__main__":
    main()
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

import random
import pygame
from pygame.locals import *
import os
import sys
from AND import *
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

class Nivel:
    pygame.init()
    #input, output, hueco, pieza, conector,
    def __init__(self, n_input):
        """
        :param inputs:
        :param outputs:
        :param huecos:
        :param puertas:
        """
        self.caracteristcas = [random.randint(0, 1) for i in range(n_input+1)]  # devuelve una lista de 5 valores entre 0 y 1,
        self.input = self.caracteristcas[:2]    # en esta lista estan los inputs y los outputs
        self.output = self.caracteristcas[-1]
        self.n_hueco = n_input - 1
        self.pieza = [AND()]                         # listado de piezas utilizado en el nivel
        self.posible_solucion = []

    def rellenar_huecos(self):
        '''
        random.shuffle(self.pieza)

        for x in range(len(self.pieza)):

            for i in self.pieza:

                if (self.pieza[0].comp((self.pieza[1].comp(self.input[0:1])), (self.pieza[2].comp(self.input[2:3])))) == self.output:

                    self.posible_solucion= [self.pieza[0], self.pieza[1], self.pieza[2]].
        '''

        if self.pieza[0].comp(self.input) == self.output:
            return print(self.posible_solucion.append(self.pieza))

        # creamos la ventana:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        fondo = pygame.image.load('FOTOS/FONDO.jpg')
        # image = NOR().image
        # image.convert()
        # rect = image.get_rect()
        # rect.center = SCREEN_WIDTH*1.5//3, SCREEN_HEIGHT*3.5//5 # En cada porta

        P_AND = AND().image.get_rect()
        P_AND.center = SCREEN_WIDTH * 1.5 // 3, SCREEN_HEIGHT * 4.5 // 5

       # P_OR = OR().image.get_rect()
       # P_OR.center = SCREEN_WIDTH * 0.5 // 3, SCREEN_HEIGHT * 4.5 // 5

        # Hueco1 = pygame.Rect(((SCREEN_WIDTH*1.5 // 3)-29, (SCREEN_WIDTH*1.5 // 5)-60), (58, 120))
        #Hueco1 = pygame.Rect(huecos)
        # Hueco2 = pygame.Rect(H2.cordenadas, H2.tamanyo)
        # Hueco3 = pygame.Rect(H3.cordenadas, H3.tamanyo)

    # collide = pygame.Rect.colliderect(object,rect2)

    def mov(self):

        running = True
        moving = False
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
            #screen.blit(fondo, (0, 0))
           # pygame.draw.rect(screen, Amarillo, Hueco1)
            # pygame.draw.rect(screen, Amarillo, Hueco2)
            # pygame.draw.rect(screen, Amarillo, Hueco3)
           # screen.blit(NOR().image, P_NOR)
           # screen.blit(AND().image, P_AND)
            # screen.blit(OR().image, P_OR)
            # screen.blit(XOR().image, P_XOR)

            pygame.display.update()


if __name__ == "__main__":
    N = Nivel(2)
    N.rellenar_huecos()

    print(N.posible_solucion.append(N.pieza))
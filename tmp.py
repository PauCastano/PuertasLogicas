import random
import pygame
from pygame.locals import *
import os
import sys
from AND import *
from OR import *
from Hueco import *



SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
IMG_DIR = "FOTOS"
Amarillo = (255, 255, 0)
Rojo = (255, 0, 0)
Blanco = (255, 255, 255)
# (WIDTH, HEIGHT)
cordenadas1 = 211, 100
cordenadas2 = 91, 260
cordenadas3 = 331, 260

P_AND = AND().image.get_rect()
P_AND.center = AND().pos

P_OR = OR().image.get_rect()
P_OR.center = OR().pos

# Hueco1 = pygame.Rect((210, 75), (58, 120))
# Hueco2 = pygame.Rect((90, 240), (58, 120))
# Hueco3 = pygame.Rect((330, 240), (58, 120))
H1 = Hueco((210, 75), (58, 120))
Hueco1 = pygame.Rect(H1.cordenadas, H1.tamanyo)
H2 = Hueco((90, 240), (58, 120))
Hueco2 = pygame.Rect(H2.cordenadas, H2.tamanyo)
H3 = Hueco((330, 240), (58, 120))
Hueco3 = pygame.Rect(H3.cordenadas, H3.tamanyo)

# P_OR = OR().image.get_rect()
# P_OR.center = SCREEN_WIDTH * 0.5 // 3, SCREEN_HEIGHT * 4.5 // 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fondo = pygame.image.load('FOTOS/FONDO1.jpg')


portes=[P_AND, P_OR]


def main():

    running = True
    moving = False
    respuesta =[]

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

                    if Hueco1.top == r.top:
                        r.center = Hueco1.center
                        H1.hay_pieza()
                        respuesta.append(r)

                    if Hueco2.center == r.center:
                        r.center = Hueco2.center
                        H2.hay_pieza()

                    if Hueco3.center == r.center:
                        r.center = Hueco3.center
                        H3.hay_pieza()

            elif event.type == MOUSEBUTTONUP:
                moving = False

            # elif Hueco.H1.hay_pieza() and Hueco.H2.hay_pieza() and Hueco.H3.hay_pieza():
            #     if Hueco.H3.salida == 1:
            #         resultado = 1
            #     else:
            #         resultado = 0

        # L'ordre en que fem les figures importa en quines estan en primera fila
        screen.blit(fondo, (0, 0))
        pygame.draw.rect(screen, Amarillo, Hueco1)
        pygame.draw.rect(screen, Rojo, Hueco2)
        pygame.draw.rect(screen, Amarillo, Hueco3)

        screen.blit(AND().image, P_AND)
        screen.blit(OR().image, P_OR)

        # screen.blit(NOR().image, P_NOR)
        # screen.blit(XOR().image, P_XOR)

        pygame.display.update()


if __name__ == "__main__":

    main()

import random
import pygame
from pygame.locals import *
import os
import sys
from AND import *
from OR import *
from Hueco import *

pygame.init()


SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
IMG_DIR = "FOTOS"
Amarillo = (255, 255, 0)
Rojo = (255, 0, 0)
Blanco = (255, 255, 255)

# P_AND = AND().image.get_rect()
# P_AND.center = AND().pos

# P_OR = OR().image.get_rect()
# P_OR.center = OR().pos

# Hueco1 = pygame.Rect((210, 75), (58, 120))
# Hueco2 = pygame.Rect((90, 240), (58, 120))
# Hueco3 = pygame.Rect((330, 240), (58, 120))
# H1 = Hueco((210, 75), (58, 120))
# Hueco1 = pygame.Rect(H1.cordenadas, H1.tamanyo)
# H2 = Hueco((90, 240), (58, 120))
# Hueco2 = pygame.Rect(H2.cordenadas, H2.tamanyo)
# H3 = Hueco((330, 240), (58, 120))
# Hueco3 = pygame.Rect(H3.cordenadas, H3.tamanyo)

# P_OR = OR().image.get_rect()
# P_OR.center = SCREEN_WIDTH * 0.5 // 3, SCREEN_HEIGHT * 4.5 // 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fondo = pygame.image.load('FOTOS/FONDO1.jpg')


def main():

    running = True
    moving = False
    respuesta =[]

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
    P_AND.rect.x = 90
    P_AND.rect.y = 475

    lista_huecos.add(H1, H2, H3)
    lista_puertas.add(P_AND)
    lista_todos_sprites.add(H1, H2, H3, P_AND)


    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:

                for r in lista_puertas:
                    if r.rect.collidepoint(event.pos):
                        moving = True

            elif event.type == MOUSEMOTION and moving:
                for r in lista_puertas:

                    mouse_pos = pygame.mouse.get_pos()
                    r.rect.x = mouse_pos[0]
                    r.rect.y = mouse_pos[1]

                    lista_huecos_llenos = pygame.sprite.groupcollide(lista_puertas, lista_huecos, False, True)

                    for lista_huecos in lista_huecos_llenos:
                        r.rect.center = H1.rect.center

                # for r in portes:
                    # if r.collidepoint(event.pos):
                    #     r.move_ip(event.rel)

                    # if Hueco1.top == r.top:
                    #     r.center = Hueco1.center
                    #     H1.hay_pieza()

                    # if Hueco2.center == r.center:
                    #     r.center = Hueco2.center
                    #     H2.hay_pieza()
                    #
                    # if Hueco3.center == r.center:
                    #     r.center = Hueco3.center
                    #     H3.hay_pieza()

            elif event.type == MOUSEBUTTONUP:
                moving = False

            # elif Hueco.H1.hay_pieza() and Hueco.H2.hay_pieza() and Hueco.H3.hay_pieza():
            #     if Hueco.H3.salida == 1:
            #         resultado = 1
            #     else:
            #         resultado = 0

        # L'ordre en que fem les figures importa en quines estan en primera fila
        screen.blit(fondo, (0, 0))
        lista_todos_sprites.draw(screen)
        # pygame.draw.rect(screen, Amarillo, Hueco1)
        # pygame.draw.rect(screen, Rojo, Hueco2)
        # pygame.draw.rect(screen, Amarillo, Hueco3)
        #
        # screen.blit(AND().image, P_AND)

        # screen.blit(OR().image, P_OR)
        # screen.blit(NOR().image, P_NOR)
        # screen.blit(XOR().image, P_XOR)

        pygame.display.update()


if __name__ == "__main__":
    main()

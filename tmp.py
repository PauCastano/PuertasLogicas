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

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fondo = pygame.image.load('FOTOS/FONDO1.jpg')


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("FOTOS/font.ttf", size)


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
    lista_puertas.add(P_AND, P_NAND, P_OR, P_NOR, P_XOR, P_XNOR)
    lista_todos_sprites.add(H1, H2, H3, P_AND, P_NAND, P_OR, P_NOR, P_XOR, P_XNOR)

    in1 = str(Nivel(4).input[0])
    in2 = str(Nivel(4).input[1])
    in3 = str(Nivel(4).input[2])
    in4 = str(Nivel(4).input[3])
    print(in1)

    while running:

        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(fondo, (0, 0))

        R_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON4.png"), pos=(375, 135),
                         text_input="R", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        lista_solucion = []

        for button in [R_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:

                if R_BUTTON.checkForInput(MOUSE_POS):

                    P_AND.rect.x = AND().pos[0]
                    P_AND.rect.y = AND().pos[1]

                    P_NAND.rect.x = NAND().pos[0]
                    P_NAND.rect.y = NAND().pos[1]

                    P_OR.rect.x = OR().pos[0]
                    P_OR.rect.y = OR().pos[1]

                    P_NOR.rect.x = NOR().pos[0]
                    P_NOR.rect.y = NOR().pos[1]

                    P_XOR.rect.x = XOR().pos[0]
                    P_XOR.rect.y = XOR().pos[1]

                    P_XNOR.rect.x = XNOR().pos[0]
                    P_XNOR.rect.y = XNOR().pos[1]

                    lista_solucion = []

                    print(lista_solucion)

                for r in lista_puertas:
                    if r.rect.collidepoint(event.pos):
                        moving = True

            elif event.type == MOUSEMOTION and moving:

                for r in lista_puertas:

                    if r.rect.collidepoint(event.pos):
                        r.rect.move_ip(event.rel)

                    choque = pygame.sprite.spritecollideany(r, lista_huecos)
                    if choque:
                        r.rect.center = choque.rect.center
                        lista_solucion.append(r)
                        print(lista_solucion)

            elif event.type == MOUSEBUTTONUP:
                moving = False

        # L'ordre en que fem les figures importa en quines estan en primera fila

        lista_todos_sprites.draw(SCREEN)

        input1 = get_font(15).render(in1, True, "#b68f40")
        input1_RECT = input1.get_rect(center=(100, 380))
        SCREEN.blit(input1, input1_RECT)

        input2 = get_font(15).render(in2, True, "#b68f40")
        input2_RECT = input2.get_rect(center=(130, 380))
        SCREEN.blit(input2, input2_RECT)

        input3 = get_font(15).render(in3, True, "#b68f40")
        input3_RECT = input3.get_rect(center=(350, 380))
        SCREEN.blit(input3, input3_RECT)

        input4 = get_font(15).render(in4, True, "#b68f40")
        input4_RECT = input4.get_rect(center=(375, 380))
        SCREEN.blit(input4, input4_RECT)


        # pygame.draw.rect(SCREEN, Amarillo, Hueco1)
        # pygame.draw.rect(SCREEN, Rojo, Hueco2)
        # pygame.draw.rect(SCREEN, Amarillo, Hueco3)
        # SCREEN.blit(AND().image, P_AND)
        # SCREEN.blit(OR().image, P_OR)
        # SCREEN.blit(NOR().image, P_NOR)
        # SCREEN.blit(XOR().image, P_XOR)

        pygame.display.update()


if __name__ == "__main__":
    main()


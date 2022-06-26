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
import pygame, sys, random
from Button import *
from Pieza import *

pygame.init()

SCREEN = pygame.display.set_mode((480, 640))
pygame.display.set_caption("Menu")

BG = pygame.image.load('FOTOS/FONDO.jpg')
TAND = pygame.image.load('FOTOS/T.AND.png')
TNAND = pygame.image.load('FOTOS/T.NAND.png')
TOR = pygame.image.load('FOTOS/T.OR.PNG')
TNOR = pygame.image.load('FOTOS/T.NOR.png')
TXOR = pygame.image.load('FOTOS/T.XOR.PNG')
TXNOR = pygame.image.load('FOTOS/T.XNOR.png')


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("FOTOS/font.ttf", size)


def TUTORIAL():
    while True:
        TUTORIAL_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        TUTORIAL_TEXT = get_font(40).render("TUTORIAL", True, "#b68f40")
        TUTORIAL_RECT = TUTORIAL_TEXT.get_rect(center=(240, 100))
        SCREEN.blit(TUTORIAL_TEXT, TUTORIAL_RECT)

        AND_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON2.png"), pos=(150, 250),
                                 text_input="AND", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        NAND_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON2.png"), pos=(350, 250),
                             text_input="NAND", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        OR_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON2.png"), pos=(150, 320),
                             text_input="OR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        NOR_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON2.png"), pos=(350, 320),
                             text_input="NOR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        XOR_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON2.png"), pos=(150, 390),
                             text_input="XOR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        XNOR_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON2.png"), pos=(350, 390),
                             text_input="XNOR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        for button in [AND_BUTTON, NAND_BUTTON, OR_BUTTON, NOR_BUTTON, XOR_BUTTON, XNOR_BUTTON, QUIT_BUTTON]:
            button.changeColor(TUTORIAL_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AND_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    AND()
                if NAND_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    NAND()
                if OR_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    OR()
                if NOR_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    NOR()
                if XOR_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    XOR()
                if XNOR_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    XNOR()
                if QUIT_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    main_menu()

        pygame.display.update()
def AND():
    while True:
        AND_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(TAND, (50, 200))
        AND_TEXT = get_font(40).render("AND", True, "#b68f40")
        AND_RECT = AND_TEXT.get_rect(center=(240, 100))
        SCREEN.blit(AND_TEXT, AND_RECT)

        BACK_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                         text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON.changeColor(AND_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(AND_MOUSE_POS):
                    TUTORIAL()

        pygame.display.update()
def NAND():
    while True:
        NAND_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(TNAND, (50, 200))
        NAND_TEXT = get_font(40).render("NAND", True, "#b68f40")
        NAND_RECT = NAND_TEXT.get_rect(center=(240, 100))
        SCREEN.blit(NAND_TEXT, NAND_RECT)

        BACK_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON.changeColor(NAND_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(NAND_MOUSE_POS):
                    TUTORIAL()

        pygame.display.update()
def OR():
    while True:
        OR_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(TOR, (50, 200))
        OR_TEXT = get_font(40).render("OR", True, "#b68f40")
        OR_RECT = OR_TEXT.get_rect(center=(240, 100))
        SCREEN.blit(OR_TEXT, OR_RECT)

        BACK_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON.changeColor(OR_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OR_MOUSE_POS):
                    TUTORIAL()

        pygame.display.update()
def NOR():
    while True:
        NOR_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(TNOR, (50, 200))
        NOR_TEXT = get_font(40).render("NOR", True, "#b68f40")
        NOR_RECT = NOR_TEXT.get_rect(center=(240, 100))
        SCREEN.blit(NOR_TEXT, NOR_RECT)

        BACK_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON.changeColor(NOR_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(NOR_MOUSE_POS):
                    TUTORIAL()

        pygame.display.update()
def XOR():
    while True:
        XOR_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(TXOR, (50, 200))
        XOR_TEXT = get_font(40).render("XOR", True, "#b68f40")
        XOR_RECT = XOR_TEXT.get_rect(center=(240, 100))
        SCREEN.blit(XOR_TEXT, XOR_RECT)

        BACK_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON.changeColor(XOR_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(XOR_MOUSE_POS):
                    TUTORIAL()

        pygame.display.update()
def XNOR():
    while True:
        XNOR_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(TXNOR, (50, 200))
        XNOR_TEXT = get_font(40).render("XNOR", True, "#b68f40")
        XNOR_RECT = XNOR_TEXT.get_rect(center=(240, 100))
        SCREEN.blit(XNOR_TEXT, XNOR_RECT)

        BACK_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON.changeColor(XNOR_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(XNOR_MOUSE_POS):
                    TUTORIAL()

        pygame.display.update()
def PLAY():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(40).render("PLAY", True, "#b68f40")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(240, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        NIVEL1_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON3.png"), pos=(240, 250),
                                 text_input="NIVEL 1", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        NIVEL2_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON3.png"), pos=(240, 320),
                             text_input="NIVEL 2", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        NIVEL3_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON3.png"), pos=(240, 390),
                             text_input="NIVEL 3", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")


        for button in [NIVEL1_BUTTON,NIVEL2_BUTTON,NIVEL3_BUTTON, QUIT_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pass
                if NIVEL2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pass
                if NIVEL3_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pass
                if QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(240, 100))

        TUTORIAL_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 250),
                             text_input="TUTORIAL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        PLAY_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 400),
                                text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="SALIDA", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [TUTORIAL_BUTTON, PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    TUTORIAL()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    PLAY()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
import pygame, sys
from Button import *

pygame.init()

SCREEN = pygame.display.set_mode((480, 640))
pygame.display.set_caption("Menu")

BG = pygame.image.load('FOTOS/FONDO.jpg')


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("FOTOS/font.ttf", size)


def TUTORIAL():
    while True:
        TUTORIAL_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        TUTORIAL_TEXT = get_font(40).render("TUTORIAL", True, "#b68f40")
        TUTORIAL_RECT = TUTORIAL_TEXT.get_rect(center=(240, 100))
        SCREEN.blit( TUTORIAL_TEXT, TUTORIAL_RECT)

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
                             text_input="SALIDA", font=get_font(40), base_color="#d7fcd4", hovering_color="White")


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
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def AND():
    pass
def NAND():
    pass
def OR():
    pass
def NOR():
    pass
def XOR():
    pass
def XNOR():
    pass
def JUEGO():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
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
                    JUEGO()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
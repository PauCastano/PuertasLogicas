#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
import pygame_menu

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
IMG_DIR = "FOTOS"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fondo = pygame.image.load('FOTOS/FONDO.jpg')

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        screen.blit(fondo,(0,0))
        draw_text('MENU PRINCIPAL', font, (0, 0, 0), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(120, 200, 250, 50)
        button_2 = pygame.Rect(120, 300, 250, 50)
        button_3 = pygame.Rect(120,400,250,50)
        if button_1.collidepoint((mx, my)):
            if click:
                TUTORIAL()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        draw_text('TUTORIAL', font, (255,255,255), screen, 190, 215)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def TUTORIAL():
    running = True
    while running:
        screen.blit(fondo, (0, 0))
        draw_text('TUTORIAL', font, (0, 0, 0), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(120, 150, 100, 50)
        button_2 = pygame.Rect(120, 250, 100, 50)
        button_3 = pygame.Rect(270, 150, 100, 50)
        button_4 = pygame.Rect(270, 250, 100, 50)
        button_5 = pygame.Rect(120, 350, 100, 50)
        button_6 = pygame.Rect(270, 350, 100, 50)
        button_7 = pygame.Rect(120, 450, 250, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                pass
        if button_2.collidepoint((mx, my)):
            if click:
                pass
        if button_3.collidepoint((mx, my)):
            if click:
                pass
        if button_4.collidepoint((mx, my)):
            if click:
                pass
        if button_5.collidepoint((mx, my)):
            if click:
                pass
        if button_6.collidepoint((mx, my)):
            if click:
                pass
        if button_3.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        pygame.draw.rect(screen, (0, 0, 0), button_5)
        pygame.draw.rect(screen, (0, 0, 0), button_6)
        pygame.draw.rect(screen, (255, 0, 0), button_7)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

if __name__ == "__main__":
    main_menu()

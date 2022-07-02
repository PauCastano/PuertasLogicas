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
from pygame.locals import *
from Button import *
from Nivel import *
pygame.init()

SCREEN = pygame.display.set_mode((480, 640))
pygame.display.set_caption("Menu")
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
IMG_DIR = "FOTOS"
fondo = pygame.image.load('FOTOS/FONDO1.jpg')

BG = pygame.image.load('FOTOS/FONDO.jpg')
TAND = pygame.image.load('FOTOS/T.AND.png')
TNAND = pygame.image.load('FOTOS/T.NAND.png')
TOR = pygame.image.load('FOTOS/T.OR.PNG')
TNOR = pygame.image.load('FOTOS/T.NOR.png')
TXOR = pygame.image.load('FOTOS/T.XOR.PNG')
TXNOR = pygame.image.load('FOTOS/T.XNOR.png')


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("FOTOS/font.ttf", size)

def PLAY():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("PLAY", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(240, 100))

        N2_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON3.png"), pos=(240, 320),
                                text_input="NORMAL", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        N1_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON3.png"), pos=(240, 390),
                           text_input="DIFICIL", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 550),
                             text_input="ATRAS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")


        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [N1_BUTTON, N2_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if N1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    N1()
                if N2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    N2()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def N2():

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

    P_AND2 = AND()
    P_AND2.rect.x = AND().pos[0]
    P_AND2.rect.y = AND().pos[1]

    P_NAND = NAND()
    P_NAND.rect.x = NAND().pos[0]
    P_NAND.rect.y = NAND().pos[1]

    P_NAND2 = NAND()
    P_NAND2.rect.x = NAND().pos[0]
    P_NAND2.rect.y = NAND().pos[1]

    P_OR = OR()
    P_OR.rect.x = OR().pos[0]
    P_OR.rect.y = OR().pos[1]

    P_OR2 = OR()
    P_OR2.rect.x = OR().pos[0]
    P_OR2.rect.y = OR().pos[1]

    P_NOR = NOR()
    P_NOR.rect.x = NOR().pos[0]
    P_NOR.rect.y = NOR().pos[1]

    P_NOR2 = NOR()
    P_NOR2.rect.x = NOR().pos[0]
    P_NOR2.rect.y = NOR().pos[1]

    P_XOR = XOR()
    P_XOR.rect.x = XOR().pos[0]
    P_XOR.rect.y = XOR().pos[1]

    P_XOR2 = XOR()
    P_XOR2.rect.x = XOR().pos[0]
    P_XOR2.rect.y = XOR().pos[1]

    P_XNOR = XNOR()
    P_XNOR.rect.x = XNOR().pos[0]
    P_XNOR.rect.y = XNOR().pos[1]

    P_XNOR2 = XNOR()
    P_XNOR2.rect.x = XNOR().pos[0]
    P_XNOR2.rect.y = XNOR().pos[1]

    lista_huecos.add(H1, H2, H3)
    lista_puertas.add(P_AND, P_NAND, P_OR, P_NOR, P_XOR, P_XNOR)
    lista_todos_sprites.add(H1, H2, H3, P_AND, P_NAND, P_OR, P_XOR, P_XNOR, P_NOR)

    nivel = Nivel(4)
    nivel.comp()
    list_soluciones = nivel.posible_solucion
    print('solciones_nievl:', list_soluciones)

    in1 = str(nivel.input[0])
    in2 = str(nivel.input[1])
    in3 = str(nivel.input[2])
    in4 = str(nivel.input[3])
    res = 0
    todas_puertas = [AND(), NAND(), OR(), NOR(), XOR(), XNOR(), AND(), NAND(), OR(), NOR(), XOR(), XNOR(), AND(),
                     NAND(), OR(), NOR(), XOR(), XNOR()]
    while running:

        SCREEN.fill("black")
        SCREEN.blit(fondo, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        lista_solucion = [0, 0, 0]


        R_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON4.png"), pos=(375, 135),
                          text_input="R", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON4.png"), pos=(375, 90),
                             text_input="A", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        F_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON3.png"), pos=(240, 410),
                          text_input="FELICIDADES", font=get_font(30), base_color="#d7fcd4",
                          hovering_color="White")
        T_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON3.png"), pos=(240, 410),
                          text_input="TRY AGAIN", font=get_font(30), base_color="#d7fcd4",
                          hovering_color="White")


        for button in [R_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        if res == 1:
            F_BUTTON.changeColor(MOUSE_POS)
            F_BUTTON.update(SCREEN)

        if res == 2:
            T_BUTTON.changeColor(MOUSE_POS)
            T_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running = False

            if event.type == MOUSEBUTTONDOWN:

                if F_BUTTON.checkForInput(MOUSE_POS) and res ==1:
                    PLAY()
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    PLAY()
                if R_BUTTON.checkForInput(MOUSE_POS) or (T_BUTTON.checkForInput(MOUSE_POS) and res==2):
                    res = 0
                    lista_puertas.remove(P_AND2, P_NAND2, P_OR2, P_NOR2, P_XOR2, P_XNOR2)
                    lista_todos_sprites.remove(P_AND2, P_NAND2, P_OR2, P_NOR2, P_XOR2, P_XNOR2)

                    for bup, bbb in enumerate(lista_puertas):
                        bbb.rect.x = todas_puertas[bup].pos[0]
                        bbb.rect.y = todas_puertas[bup].pos[1]

                    lista_solucion = [0, 0, 0]
                    print(lista_puertas)

                for r in lista_puertas:
                    if r.rect.collidepoint(event.pos):
                        moving = True

            elif event.type == MOUSEMOTION and moving:

                for r in lista_puertas:
                    if r.rect.collidepoint(event.pos):
                        r.rect.move_ip(event.rel)

            elif event.type == MOUSEBUTTONUP:

                for r in lista_puertas:
                    choque = pygame.sprite.spritecollideany(r, lista_huecos)
                    if choque:
                        r.rect.center = choque.rect.center
                        if choque == H1:
                            lista_solucion[0] = r

                        elif choque == H2:
                            lista_solucion[1] = r

                        else:
                            lista_solucion[2] = r

                        if r == P_AND:
                            lista_puertas.add(P_AND2)
                            lista_todos_sprites.add(P_AND2)
                        elif r == P_NAND:
                            lista_puertas.add(P_NAND2)
                            lista_todos_sprites.add(P_NAND2)
                        elif r == P_OR:
                            lista_puertas.add(P_OR2)
                            lista_todos_sprites.add(P_OR2)
                        elif r == P_NOR:
                            lista_puertas.add(P_NOR2)
                            lista_todos_sprites.add(P_NOR2)
                        elif r == P_XOR:
                            lista_puertas.add(P_XOR2)
                            lista_todos_sprites.add(P_XOR2)
                        elif r == P_XNOR:
                            lista_puertas.add(P_XNOR2)
                            lista_todos_sprites.add(P_XNOR2)

                moving = False

        if lista_solucion[0] != 0 and lista_solucion[1] != 0 and lista_solucion[2] != 0:
            count = 0

            for contar, puertasz in enumerate(list_soluciones):
                if count < len(list_soluciones):
                    print(list_soluciones[count:count + 3])
                    if list_soluciones[count:count + 3] == lista_solucion:
                        print('Felicidades')
                        res = 1
                        break
                    else:
                        count += 3
                else:
                    res = 2



        lista_todos_sprites.draw(SCREEN)

        input1 = get_font(15).render(in1, True, "#b68f40")
        input1_RECT = input1.get_rect(center=(105, 390))
        SCREEN.blit(input1, input1_RECT)

        input2 = get_font(15).render(in2, True, "#b68f40")
        input2_RECT = input2.get_rect(center=(130, 390))
        SCREEN.blit(input2, input2_RECT)

        input3 = get_font(15).render(in3, True, "#b68f40")
        input3_RECT = input3.get_rect(center=(348, 390))
        SCREEN.blit(input3, input3_RECT)

        input4 = get_font(15).render(in4, True, "#b68f40")
        input4_RECT = input4.get_rect(center=(370, 390))
        SCREEN.blit(input4, input4_RECT)

        out = get_font(15).render('1', True, "#b68f40")
        out_RECT = out.get_rect(center=(239, 45))
        SCREEN.blit(out, out_RECT)

        pygame.display.update()
def N1():

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
    lista_todos_sprites.add(H1, H2, H3, P_AND, P_NAND, P_OR, P_XOR, P_XNOR, P_NOR)

    nivel = Nivel(4)
    nivel.comp()
    list_soluciones = nivel.posible_solucion
    print('solciones_nievl:', list_soluciones)

    in1 = str(nivel.input[0])
    in2 = str(nivel.input[1])
    in3 = str(nivel.input[2])
    in4 = str(nivel.input[3])
    res = 0
    todas_puertas = [AND(), NAND(), OR(), NOR(), XOR(), XNOR()]
    while running:

        SCREEN.fill("black")
        SCREEN.blit(fondo, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        lista_solucion = [0, 0, 0]


        R_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON4.png"), pos=(375, 135),
                          text_input="R", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON4.png"), pos=(375, 90),
                             text_input="A", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        F_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON.png"), pos=(240, 410),
                          text_input="FELICIDADES", font=get_font(30), base_color="#d7fcd4",
                          hovering_color="White")
        T_BUTTON = Button(image=pygame.image.load("FOTOS/BUTTON3.png"), pos=(240, 410),
                          text_input="TRY AGAIN", font=get_font(30), base_color="#d7fcd4",
                          hovering_color="White")


        for button in [R_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        if res == 1:
            F_BUTTON.changeColor(MOUSE_POS)
            F_BUTTON.update(SCREEN)
        if res == 2:
            T_BUTTON.changeColor(MOUSE_POS)
            T_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running = False

            if event.type == MOUSEBUTTONDOWN:

                if F_BUTTON.checkForInput(MOUSE_POS) and res ==1:
                    PLAY()
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    PLAY()
                if R_BUTTON.checkForInput(MOUSE_POS) or (T_BUTTON.checkForInput(MOUSE_POS) and res == 2):
                    res = 0

                    for cuenta, ccc in enumerate(lista_puertas):
                        ccc.rect.x = todas_puertas[cuenta].pos[0]
                        ccc.rect.y = todas_puertas[cuenta].pos[1]

                    lista_solucion = [0, 0, 0]
                    print(lista_puertas)

                for r in lista_puertas:
                    if r.rect.collidepoint(event.pos):
                        moving = True

            elif event.type == MOUSEMOTION and moving:

                for r in lista_puertas:
                    if r.rect.collidepoint(event.pos):
                        r.rect.move_ip(event.rel)

            elif event.type == MOUSEBUTTONUP:

                for r in lista_puertas:
                    choque = pygame.sprite.spritecollideany(r, lista_huecos)
                    if choque:
                        r.rect.center = choque.rect.center
                        if choque == H1:
                            lista_solucion[0] = r

                        elif choque == H2:
                            lista_solucion[1] = r

                        else:
                            lista_solucion[2] = r


                moving = False

        if lista_solucion[0] != 0 and lista_solucion[1] != 0 and lista_solucion[2] != 0:
            count = 0

            for contar, puertasz in enumerate(list_soluciones):
                if count < len(list_soluciones):
                    print(list_soluciones[count:count + 3])
                    if list_soluciones[count:count + 3] == lista_solucion:
                        res = 1
                        print('Felicidades')
                        res = 1
                        break
                    else:
                        count += 3
                else:
                    res = 2


        lista_todos_sprites.draw(SCREEN)

        input1 = get_font(15).render(in1, True, "#b68f40")
        input1_RECT = input1.get_rect(center=(105, 390))
        SCREEN.blit(input1, input1_RECT)

        input2 = get_font(15).render(in2, True, "#b68f40")
        input2_RECT = input2.get_rect(center=(130, 390))
        SCREEN.blit(input2, input2_RECT)

        input3 = get_font(15).render(in3, True, "#b68f40")
        input3_RECT = input3.get_rect(center=(348, 390))
        SCREEN.blit(input3, input3_RECT)

        input4 = get_font(15).render(in4, True, "#b68f40")
        input4_RECT = input4.get_rect(center=(370, 390))
        SCREEN.blit(input4, input4_RECT)

        out = get_font(15).render('1', True, "#b68f40")
        out_RECT = out.get_rect(center=(239, 45))
        SCREEN.blit(out, out_RECT)

        pygame.display.update()
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
                    T_AND()
                if NAND_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    T_NAND()
                if OR_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    T_OR()
                if NOR_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    T_NOR()
                if XOR_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    T_XOR()
                if XNOR_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    T_XNOR()
                if QUIT_BUTTON.checkForInput(TUTORIAL_MOUSE_POS):
                    main_menu()

        pygame.display.update()
def T_AND():
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
def T_NAND():
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
def T_OR():
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
def T_NOR():
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
def T_XOR():
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
def T_XNOR():
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
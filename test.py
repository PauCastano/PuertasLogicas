import pygame
import sys
import math
from pygame.locals import *
from random import *


# La clase de pelota hereda de la clase Spirte
class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        self.rect = self.rect.move(self.speed)

        # Si el lado izquierdo de la pelota está fuera del límite, cambie el lado izquierdo de la pelota al límite derecho
        # Esto logra el efecto de entrar por la izquierda y salir por la derecha
        if self.rect.right < 0:
            self.rect.left = self.width

        elif self.rect.left > self.width:
            self.rect.right = 0

        elif self.rect.bottom < 0:
            self.rect.top = self.height

        elif self.rect.top > self.height:
            self.rect.bottom = 0


def collide_check(item, target):
    col_balls = []
    for each in target:
        distance = math.sqrt( \
            math.pow((item.rect.center[0] - each.rect.center[0]), 2) + \
            math.pow((item.rect.center[1] - each.rect.center[1]), 2))
        if distance <= (item.rect.width + each.rect.width) / 2:
            col_balls.append(each)
    return col_balls


def main():
    pygame.init()

    ball_image = "FOTOS/BE.png"
    bg_image = "FOTOS/BLANCO.png"

    running = True

    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball - Monster ZF")

    background = pygame.image.load(bg_image).convert_alpha()

    # Se usa para almacenar la lista de objetos de bola
    balls = []

    # Crea cinco bolas
    BALL_NUM = 2
    for i in range(BALL_NUM):
        # Posición aleatoria, velocidad aleatoria
        position = 200, 300
        speed = [randint(-1, 1), randint(-1, 1)]
        ball = Ball(ball_image, position, speed, bg_size)
        balls.append(ball)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)

        for i in range(BALL_NUM):
            item = balls.pop(i)

            if collide_check(item, balls):
                item.speed[0] = -item.speed[0]
                item.speed[1] = -item.speed[1]

            balls.insert(i, item)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()


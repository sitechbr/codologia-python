# -*- coding: utf-8 -*-
# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint


WIDTH = 800
HEIGHT = 600
FPS = 60
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

score = 0
font_name = pygame.font.match_font('arial')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50), flags=pygame.SRCALPHA)
        x = 24
        y = 24
        pygame.draw.circle(self.image, WHITE, (x, y), 20, 1)
        pygame.draw.circle(self.image, WHITE, (x, y), 1)
        pygame.draw.line(self.image, WHITE, (x - 24, y), (x - 16, y))
        pygame.draw.line(self.image, WHITE, (x + 24, y), (x + 16, y))
        pygame.draw.line(self.image, WHITE, (x, y - 24), (x, y - 16))
        pygame.draw.line(self.image, WHITE, (x, y + 24), (x, y + 16))

        self.rect = self.image.get_rect()

    def setPos(self, x, y):
        self.rect.center = (x, y)



# Timer
pygame.init()


# Создаем игру и окно
  # это команда, которая запускает pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание окна программы
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # таймер для работы с заданной частотой кадров
pygame.mouse.set_visible(False)  # Удаляем курсор

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    screen.fill(BLACK)
    # Управление курсором как мышью
    cursorPX, cursorPY = pygame.mouse.get_pos()
    player.setPos(cursorPX, cursorPY)

    all_sprites.draw(screen)
    pygame.display.update()

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        

pygame.quit()
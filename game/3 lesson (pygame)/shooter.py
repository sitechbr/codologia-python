# -*- coding: utf-8 -*-
# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint

MOVE_TIME = 5000
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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def setPos(self, x, y):
        self.rect.center = (x, y)


def show_score():
    font = pygame.font.Font(font_name, 18)
    text_surface = font.render(str(score), True, WHITE)
    screen.blit(text_surface, (WIDTH // 2, 10))


# Timer
pygame.init()
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, MOVE_TIME)

# Создаем игру и окно
  # это команда, которая запускает pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание окна программы
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # таймер для работы с заданной частотой кадров
pygame.mouse.set_visible(False)  # Удаляем курсор

all_sprites = pygame.sprite.Group()
enemy = Enemy(randint(0, WIDTH), randint(0, HEIGHT), RED)
player = Player()

all_sprites.add(enemy)

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
    show_score()
    pygame.display.update()

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == move_event:
            enemy.setPos(randint(0, WIDTH), randint(0, HEIGHT))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if player.rect.colliderect(enemy):
                    print("hit")
                    enemy.setPos(randint(0, WIDTH), randint(0, HEIGHT))
                    score+=1
                # else:
                # print("miss")

pygame.quit()
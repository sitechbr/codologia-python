# -*- coding: utf-8 -*-
# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

RELOAD_SPEED = 450
SPEED_PLAYER = 10
MOVE_DOWN = 500
WIDTH = 640
HEIGHT = 480
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
reloaded= True
score = 0
font_name = pygame.font.match_font('arial')
state = "stop"

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,20), flags=pygame.SRCALPHA)
        pygame.draw.rect(self.image, WHITE, (0,0, 30,20))
        self.rect = self.image.get_rect()
        self.x, self.y = self.rect.center
        self.rect.center = (x,y)
        self.speed = SPEED_PLAYER
    def move_left(self):
        if self.rect.left >5:
            self.rect.move_ip(-self.speed,0)
    def move_right(self):
        if self.rect.right < WIDTH:
            self.rect.move_ip(self.speed,0)
    def shoot(self):
        shot = Shots(self.rect.centerx, self.rect.top)
        all_sprites.add(shot)
        shots.add(shot)    

class Shots(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10), flags=pygame.SRCALPHA)
        pygame.draw.rect(self.image, BLUE, (0,0, 10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speedy = -10
        
    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

   
class Enemy(pygame.sprite.Sprite):  
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,20), flags=pygame.SRCALPHA)
        pygame.draw.rect(self.image, RED, (0,0, 30,20))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)   
    def update(self):
        self.rect.y += 10     

        
def show_score(score):
    font = pygame.font.Font(font_name,20)
    text_surface = font.render(str(score), True,WHITE)
    screen.blit(text_surface,(WIDTH/2,10))

def show_text(my_text):
    font = pygame.font.Font(font_name,40)
    text_surface = font.render(str(my_text), True,WHITE)
    screen.blit(text_surface,(WIDTH/2-text_surface.get_width()/2,HEIGHT/2-40))
# Создаем игру и окно
pygame.init()  # это команда, которая запускает pygame
move_down_event = pygame.USEREVENT + 1
reloaded_event  = pygame.USEREVENT + 2
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # создание окна программы
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # таймер для работы с заданной частотой кадров
pygame.mouse.set_visible(False)
all_sprites = pygame.sprite.Group()
shots = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player(WIDTH//2,HEIGHT-20)
all_sprites.add(player)
for x in range(15, WIDTH, 40):
    for y in range(10, HEIGHT//2, 40):
        enemy = Enemy(x,y)
        enemies.add(enemy)
        all_sprites.add(enemy)
pygame.time.set_timer(move_down_event, MOVE_DOWN)
        
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    screen.fill(BLACK)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False                  
        if event.type == move_down_event:
            enemies.update()               
        if event.type == reloaded_event:
            # when the reload timer runs out, reset it
            reloaded = True
            pygame.time.set_timer(reloaded_event, 0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                state = "stop"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                state = "left"
            if event.key == pygame.K_RIGHT:
                state = "right"
            if event.key == pygame.K_SPACE:
                if reloaded:
                    player.shoot()
                    reloaded = False
                    # when shooting, create a timeout of RELOAD_SPEED
                    pygame.time.set_timer(reloaded_event, RELOAD_SPEED)
    if state == "left":
        player.move_left()
    elif state == "right":
        player.move_right()
    else:
        pass
    shots.update()             
    hits = pygame.sprite.groupcollide(enemies, shots, True, True)
    for hit in hits:
        hit.kill()
        score+=1

    hits = pygame.sprite.spritecollide(player,enemies,False)
    if hits:
        show_text("Game Over")
        pygame.display.update()
        pygame.time.delay(5000)
        running = False
    if score > 20:
        show_text("YOU WIN")
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    player.rect.clamp_ip(screen.get_rect())
    all_sprites.draw(screen)
    shots.draw(screen)
    show_score(score)
    # после отрисовки всего, переворачиваем экран
    pygame.display.update()

pygame.quit()
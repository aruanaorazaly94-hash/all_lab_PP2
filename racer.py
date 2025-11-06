import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

fps = 60

width = 400
height = 600
speed = 5
score = 0
point = 0
i = 0

red = (255, 0, 0)
black = (0, 0, 0)
#Текст
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
#Фон
background = pygame.image.load("./images/street.webp")
#Экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Raser")
t = pygame.time.Clock()
#Враг
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./images/Enemy.webp")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0) 
#Запуск движения
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > height + 80):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
#Монеты
class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./images/money.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0) 
#Запуск движения
    def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > height + 80):
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0) 

    def lost(self):
        self.rect.center = (1000, 1000)
#Монеты
class Money2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./images/money2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0) 
#Запуск движения
    def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > height + 80):
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0) 

    def lost(self):
        self.rect.center = (1000, 1000)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height - 80)
#Движения
    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)

        if self.rect.bottom < height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < width:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                
P1 = Player()
E1 = Enemy()
M1 = Money()
M2 = Money2()

#Создание групп
enemies = pygame.sprite.Group()
enemies.add(E1)

cash = pygame.sprite.Group()
cash.add(M1)

cash2 = pygame.sprite.Group()
cash2.add(M2)

all_sprites = pygame.sprite.Group()
all_sprites.add(M1)
all_sprites.add(P1)
all_sprites.add(E1)

#Игровой цикл
while True: 
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))

    scores = font_small.render(str(score), True, black)
    screen.blit(scores, (10,10))

    points = font_small.render(str(point), True, black)
    screen.blit(points, (375,10))

    #Перемещает и перерисовывает все обьекты
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if point % 5 == 0 and i != 0:
        for entity in cash2:
            screen.blit(entity.image, entity.rect)
            entity.move()

    #Запускается, если происходит столкновение между игроком и врагом
    if pygame.sprite.spritecollideany(P1, enemies):
                    
        screen.fill(red)
        screen.blit(game_over, (30,250))

        pygame.display.update()
        for entity in all_sprites:
                entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
    #Соприкосновение обьектов
    if pygame.sprite.spritecollideany(P1, cash):
        point += 1
        if point % 3 == 0:
            i += 1
            speed += 0.5
        M1.lost()
        pygame.display.update()
    #Соприкосновение обьектов
    if pygame.sprite.spritecollideany(P1, cash2):
        point += 3
        speed += 0.5
        M2.lost()
        pygame.display.update()
        
    pygame.display.update()
    t.tick(fps)
import pygame
import datetime

width = 1440
height = 1080

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mickey Clock")

main = pygame.image.load('./images/base_micky.jpg')
rh = pygame.image.load('./images/minute.png')
lh = pygame.image.load('./images/second.png')

running = True

while running:
    pygame.display.update()
    screen.blit(main, (0, 0))
    time = datetime.datetime.now()
    rot1 = pygame.transform.rotate(lh, -time.second * 6)
    rot1_rect = rot1.get_rect(center = (width/2, height/2))
    screen.blit(rot1, rot1_rect)
    rot2 = pygame.transform.rotate(rh, (-time.minute - 8) * 6)
    rot2_rect = rot2.get_rect(center = (width/2, height/2))
    screen.blit(rot2, rot2_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
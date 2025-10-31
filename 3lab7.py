import pygame
x = 225
y = 225

pygame.init()
screen = pygame.display.set_mode((2*x, 2*y))
pygame.display.set_caption("Red Ball")

running = True

while running:
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y > 40:
                    y -= 20
        
            if event.key == pygame.K_DOWN:
                if y < 410:
                    y += 20

            elif event.key == pygame.K_RIGHT:
                if x < 410:
                    x += 20
                
            elif event.key == pygame.K_LEFT:
                if x > 40:
                    x -= 20
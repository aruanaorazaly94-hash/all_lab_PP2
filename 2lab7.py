import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("PyGame Player")

playlist = ['./music/Drake - Jumbotron Shit Poppin.mp3',
            './music/Drake, 21 Savage - Circo Loco (Audio).mp3',
            './music/Drake, 21 Savage - Broke Boys (Audio).mp3',
            './music/Drake, 21 Savage - Major Distribution (Audio).mp3']

i = 0
j = 0

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                i += 1
                if i == 1:
                    pygame.mixer.music.load(playlist[0])
                    pygame.mixer.music.play()
                elif i % 2 == 0:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                j += 1
                i = 1
                if j < len(playlist):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                else:
                    j = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                
            elif event.key == pygame.K_LEFT:
                j -= 1
                i = 1
                if j > -len(playlist):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                else:
                    j = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                
                
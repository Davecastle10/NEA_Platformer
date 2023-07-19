import sys
import pygame 

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("NEA Platformer")


clock = pygame.time.Clock()

game_running = True

while game_running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)

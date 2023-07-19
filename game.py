import sys

import pygame 

from scripts.utils import load_image
from scripts.entities import PhysicsEntity






class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("NEA Platformer")
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320, 240))


        

        self.clock = pygame.time.Clock()

        self.background_img_1 = pygame.image.load("assets/images/backgrounds/green_hills_1.png")

        self.player_movement = [False, False, False, False]

        self.assets = {
            'player': load_image('entities/player/player_v1.png')
        }

        self.player = PhysicsEntity(self, 'player', (310, 190), (80, 100))



    def run(self):
        while True:
            self.screen.blit(self.background_img_1, (0, 0))

            self.player.update((self.player_movement[1] - self.player_movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.player_movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player_movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.player_movement[1] = False

            #self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()
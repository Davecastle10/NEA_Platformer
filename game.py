# all of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 

import os
import sys
import pygame 

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds






class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("NEA Platformer")
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320, 240))


        self.clock = pygame.time.Clock()


        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player/idle/00.png'),
            'background': load_image('backgrounds/blue_sky_waves.png'),
            'clouds' : load_images('clouds')
        }
        
        self.clouds = Clouds(self.assets['clouds'], count = 16)

        self.player_movement = [False, False, False, False]
        self.player = PhysicsEntity(self, 'player', (130, 70), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))


            # scrolls camera to keep player in the center of the screen
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset = render_scroll)

            self.tilemap.render(self.display, offset = render_scroll)

            self.player.update(self.tilemap, (self.player_movement[1] - self.player_movement[0], 0))
            self.player.render(self.display, offset = render_scroll)

            #print(self.tilemap.tiles_around(self.player.pos)) # used for error checking on what tiles are within a 3x3 radius

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.player_movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                    if event.key == pygame.K_a:
                        self.player_movement[0] = True
                    if event.key == pygame.K_d:
                        self.player_movement[1] = True
                    if event.key == pygame.K_w:
                        self.player.velocity[1] = -3
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -3


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player_movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.player_movement[1] = False
                    if event.key == pygame.K_a:
                        self.player_movement[0] = False
                    if event.key == pygame.K_d:
                        self.player_movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()
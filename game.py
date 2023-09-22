# all of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 

import os
import sys
import pygame 
from pygame import freetype

import glob 

from scripts.utils import load_image, load_images, Animation
from scripts.entities_copy import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds





# dafluffypotatoes tutorial code
class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("NEA Platformer")
        self.screen = pygame.display.set_mode((1280,760))
        self.display = pygame.Surface((640, 380))


        self.clock = pygame.time.Clock()


        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player/idle/00.png'),
            'background': load_image('backgrounds/blue_sky_waves_big.png'),
            'clouds' : load_images('clouds'),
            'player/idle' : Animation(load_images('entities/player/idle'), img_dur=6),# currently dont have extra images of r the idle animation but this is for when i have made them
            'player/jump' : Animation(load_images('entities/player/jump'), img_dur=4),
            'player/run' : Animation(load_images('entities/player/run'), img_dur=5),
            'player/slide' : Animation(load_images('entities/player/slide'), img_dur=5),# no images yet
            'player/wall_slide' : Animation(load_images('entities/player/wall_slide'), img_dur=5),# no images yet
        }
        
        self.clouds = Clouds(self.assets['clouds'], count = 16)

        self.player_movement = [False, False, False, False]
        self.player = Player(self, (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]

        self.alt = False
        self.paused = False





# creating a list of the file locations of the maps
        self.maps_path = 'data/maps'
        self.maps_list = list()
        for filename in glob.iglob(f'{self.maps_path}/*'):
            self.maps_list.append(filename)

        #self.current_map = 'data/maps/map.json' # don't think i need this anymore
        self.current_map_index = 0
        self.tilemap.load(self.maps_list[self.current_map_index])

    # dafluffypotatoes tutorial code
    def run(self):
        while True:
            if self.paused == True:
                print("helo")
                self.display.blit((0,0,0))
                # attempt to display text
                #pygame.freetype.Font.render("Paused", fgcolor = (255,255,255,255), bgcolor = (0, 0, 0, 0), style = STYLE_DEFAULT )







            else:
                self.display.blit(self.assets['background'], (0, 0))


                # scrolls camera to keep player in the center of the screen
                self.scroll[0] += (self.player.frect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
                self.scroll[1] += (self.player.frect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
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

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.alt:# when pressing shift scroll thought tyle variants instead fo groups
                        if event.button == 4:
                            self.current_map_index = (self.current_map_index - 1) % len(self.maps_list)
                            self.tilemap.load(self.maps_list[self.current_map_index])
                            
                        if event.button == 5:
                            self.current_map_index = (self.current_map_index + 1) % len(self.maps_list)
                            self.tilemap.load(self.maps_list[self.current_map_index])
 




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
                    if event.key == pygame.K_LALT:
                        self.alt = True
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not(self.paused)


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player_movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.player_movement[1] = False
                    if event.key == pygame.K_a:
                        self.player_movement[0] = False
                    if event.key == pygame.K_d:
                        self.player_movement[1] = False
                    if event.key == pygame.K_LALT:
                        self.alt = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()
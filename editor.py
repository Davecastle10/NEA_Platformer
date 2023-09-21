# all of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 

import os
import sys
import pygame 

import glob

from scripts.utils import load_images
from scripts.tilemap import Tilemap
# dafluffypotatoes tutorial code
RENDER_SCALE = 2.0



# dafluffypotatoes tutorial code
class Editor:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Editor")
        self.screen = pygame.display.set_mode((1280,800))
        self.display = pygame.Surface((640, 400))


        self.clock = pygame.time.Clock()


        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
        }
        
        

        self.movement = [False, False, False, False]

        self.tilemap = Tilemap(self, tile_size=16)


        # creating a list of the file locations of the maps
        self.maps_path = 'data/maps'
        self.maps_list = list()
        for filename in glob.iglob(f'{self.maps_path}/*'):
            self.maps_list.append(filename)

        #self.current_map = 'data/maps/map.json' # don't think i need this anymore
        self.current_map_index = 0
        self.tilemap.load(self.maps_list[self.current_map_index])



        self.scroll = [0, 0]

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0

        self.clicking = False
        self.right_clicking = False
        self.shift = False
        self.alt = False

        self.ongrid = True

    # dafluffypotatoes tutorial code
    def run(self):
        while True:
            self.display.fill((0, 0, 0))


            self.scroll[0] += (self.movement[1] - self.movement[0]) * 2
            self.scroll[1] += (self.movement[3] - self.movement[2]) * 2
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.tilemap.render(self.display, offset=render_scroll)


            current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
            current_tile_img.set_alpha(100)

            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0] / RENDER_SCALE, mpos[1] / RENDER_SCALE)# scaling coords because the display/screen thing is scaled at bottom for pixel art look
            # coords of mouse in terms of tile pos
            tile_pos = (int((mpos[0] + self.scroll[0]) // self.tilemap.tile_size), int((mpos[1] + self.scroll[1]) // self.tilemap.tile_size))


            if self.ongrid:# snap the tile image to the grid
                self.display.blit(current_tile_img, (tile_pos[0] * self.tilemap.tile_size - self.scroll[0], tile_pos[1] * self.tilemap.tile_size - self.scroll[1]))
            else:
                self.display.blit(current_tile_img, mpos)


            if self.clicking and self.ongrid:
                self.tilemap.tilemap[str(tile_pos[0]) + ';' + str(tile_pos[1])] = {'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': tile_pos}

            if self.right_clicking:
                tile_loc = str(tile_pos[0]) + ';' + str(tile_pos[1])
                if tile_loc in self.tilemap.tilemap:
                    del self.tilemap.tilemap[tile_loc]
                for tile in self.tilemap.offgrid_tiles.copy():
                    tile_img = self.assets[tile['type']][tile['variant']]
                    tile_r = pygame.Rect(tile['pos'][0] - self.scroll[0], tile['pos'][1] - self.scroll[1], tile_img.get_width(), tile_img.get_height())
                    if tile_r.collidepoint(mpos):
                        self.tilemap.offgrid_tiles.remove(tile)



            self.display.blit(current_tile_img, (5, 5))




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                        if not self.ongrid:
                            self.tilemap.offgrid_tiles.append({'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': (mpos[0] + self.scroll[0], mpos[1] + self.scroll[1])})
                    if event.button == 3:
                        self.right_clicking = True
                    
                    if self.shift:# when pressing shift scroll thought tyle variants instead fo groups
                        if event.button == 4:
                            self.tile_variant = (self.tile_variant - 1) % len(self.assets[self.tile_list[self.tile_group]])
                        if event.button == 5:
                            self.tile_variant = (self.tile_variant + 1) % len(self.assets[self.tile_list[self.tile_group]])
                    
                    else:# scroll thorugh tile groups
                        if event.button == 4:
                            self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                            self.tile_variant = 0# so you look at the first variant in the group
                        if event.button == 5:
                            self.tile_group = (self.tile_group + 1) % len(self.tile_list)
                            self.tile_variant = 0
                    
                    if self.alt:# when pressing shift scroll thought tyle variants instead fo groups
                        if event.button == 4:
                            self.current_map_index = (self.current_map_index - 1) % len(self.maps_list)
                            self.tilemap.load(self.maps_list[self.current_map_index])
                            
                        if event.button == 5:
                            self.current_map_index = (self.current_map_index + 1) % len(self.maps_list)
                            self.tilemap.load(self.maps_list[self.current_map_index])


                if event.type == pygame.MOUSEBUTTONUP:
                                    if event.button == 1:
                                        self.clicking = False
                                    if event.button == 3:
                                        self.right_clicking = False
                    
                    
                    
                    

                if event.type == pygame.KEYDOWN:

                    if self.alt:
                        if event.key == pygame.K_o:
                            self.tilemap.save(f'data/maps/maps{len(self.maps_list)}.json')
                            #self.tilemap.save(self.maps_list[self.current_map_index])


                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                    if event.key == pygame.K_RSHIFT:
                        self.shift = True
                    if event.key == pygame.K_g:
                        self.ongrid = not self.ongrid
                    if event.key == pygame.K_o:
                        self.tilemap.save(self.maps_list[self.current_map_index])
                    if event.key == pygame.K_t:
                        self.tilemap.autotile()
                    if event.key == pygame.K_LALT:
                        self.alt = True



                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
                    if event.key == pygame.K_LSHIFT:
                        self.shift = False
                    if event.key == pygame.K_RSHIFT:
                        self.shift = False
                    if event.key == pygame.K_LALT:
                        self.alt = False



            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Editor().run()
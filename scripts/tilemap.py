# all of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 


import os
import json
import pygame

# dafluffypotatoes tutorial code
AUTOTILE_MAP = {
    tuple(sorted([(1, 0), (0, 1)])): 0,
    tuple(sorted([(1, 0), (0, 1), (-1, 0)])): 1,
    tuple(sorted([(-1, 0), (0, 1)])): 2,
    tuple(sorted([(-1, 0), (0, -1), (0, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1)])): 4,
    tuple(sorted([(-1, 0), (0, -1), (1, 0)])): 5,
    tuple(sorted([(1, 0), (0, -1)])): 6,
    tuple(sorted([(1, 0), (0, -1), (0, 1)])): 7,
    tuple(sorted([(1, 0), (-1, 0), (0, 1), (0, -1)])): 8,
}
# dafluffypotatoes tutorial code
#NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0,-1), (1, -1), (1,0), (0, 0), (-1, 1), (0, 1), (1, 1)] # list off all tiles in a 3x3 radius of the enitity and their offset in relation to the entiy measured in tiles
NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0,-1), (1, -1), (1,0), (0, 0), (-1, 1), (0, 1), (1, 1)] # list off all tiles in a 3x3 radius of the enitity and their offset in relation to the entiy measured in tiles
PHYSICS_TILES = {'grass', 'stone'}
AUTOTILE_TYPES = {'grass', 'stone'}

# dafluffypotatoes tutorial code
class Tilemap:
    def __init__(self, game, tile_size = 16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []


    # dafluffypotatoes tutorial code
    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size)) # converts pixel pos to grid pos
        for offset in NEIGHBOUR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])# the weird bit is the way that tile location is stroed as a strning so that they can be later stored in a .json file for the level editor
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    # dafluffypotatoes tutorial code
    def save(self, path):
        f = open(path, 'w')
        json.dump({'tilemap': self.tilemap, 'tile_size': self.tile_size, 'offgrid': self.offgrid_tiles}, f)
        f.close()

    # dafluffypotatoes tutorial code
    def load(self, path):
        f = open(path, 'r')
        map_data = json.load(f)
        f.close()

        self.tilemap = map_data['tilemap']
        self.tile_size = map_data['tile_size']
        self.offgrid_tiles = map_data['offgrid']

    # dafluffypotatoes tutorial code
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                #
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    # dafluffypotatoes tutorial code
    def autotile(self):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            neighbours = set()
            for shift in [(1,0), (-1, 0), (0, -1), (0, 1)]:
                check_loc = str(tile['pos'][0] + shift[0]) + ';' + str(tile['pos'][1] + shift[1])
                if check_loc in self.tilemap:
                    if self.tilemap[check_loc]['type'] == tile['type']:
                        neighbours.add(shift)
            neighbours = tuple(sorted(neighbours))
            if (tile['type'] in AUTOTILE_TYPES) and (neighbours in AUTOTILE_MAP):
                tile['variant'] = AUTOTILE_MAP[neighbours]


    # dafluffypotatoes tutorial code
    def render(self, surf, offset = (0, 0)):
        for tile in self.offgrid_tiles: #need to implement a more efficient version of this if i plan on implementig an infinte world that generates stuuf offscreen
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1])) 

        for x in range(offset[0] // self.tile_size, (offset[0] + surf.get_width()) // self.tile_size + 1):
            for y in range(offset[1] // self.tile_size, (offset[1] + surf.get_height()) // self.tile_size + 1):
                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))

            





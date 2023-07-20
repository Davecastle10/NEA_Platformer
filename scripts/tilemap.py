import os 
import pygame


BASE_IMG_PATH = 'assets/images/'

class Tilemap:
    def __init__(self, tile_size=16):
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []


        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap[';10' + str(i + 5)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
            return img


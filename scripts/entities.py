# all of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 

import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0] # x velociyt then y velocity
        self.collisons = {'up': False, 'down': False, 'right': False, 'left': False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    
    def update(self, tilemap, movement=(0, 0)):
        self.collisons = {'up': False, 'down': False, 'right': False, 'left': False}


        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # seperated collisions into x and y to make them easier
        self.pos[0] += frame_movement[0]# come back later and try to remove the pos parts by using fRects that are rects that support floats
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisons['right'] = True
                if frame_movement[0] <0:
                    entity_rect.left = rect.right
                    self.collisons['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]# come back later and try to remove the pos parts by using fRects that are rects that support floats
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisons['down'] = True
                if frame_movement[1] <0:
                    entity_rect.top = rect.bottom
                    self.collisons['up'] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1) # starts with with a down vel of 1 and increments by 0. until it reaches 5 which is terminal velocity

        if self.collisons['down'] or self.collisons['up']:
            self.velocity[1] = 0

    def render(self, surf, offset = (0, 0)):
        surf.blit(self.game.assets['player'], (self.pos[0] - offset[0], self.pos[1] - offset[1] ))


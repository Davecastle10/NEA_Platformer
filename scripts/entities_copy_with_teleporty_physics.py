# all of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 
# this file is not actually implemetned in the game, it is just a previous version that I kept around for comparison becaue it had some weird and interesting effects 

import pygame

# dafluffypotatoes tutorial code
class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0] # x velociyt then y velocity
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.e_frect = pygame.FRect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        self.action = ''
        self.anim_offset = (-3, 0) # so that the entitity img can overflow for the animations, can be set to (-3, -3) but then the player images need adjusting
        self.flip = False
        self.set_action('idle')

    # dafluffypotatoes tutorial code
    def frect(self):
        return pygame.FRect(self.pos[0], self.pos[1], self.size[0], self.size[1])# rect values: left, top, width, height - left and top are the x and y coords of the top left corner of the rect and the width and height are used to create the rect as they provide the dimensions that need to be drawn from the top left corner
    
    # dafluffypotatoes tutorial code
    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()

    # dafluffypotatoes tutorial code but is now over half mine
    
    def update(self, tilemap, movement_input=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        frame_movement = (movement_input[0] + self.velocity[0], movement_input[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
        self.e_frect.move_ip(frame_movement[0], frame_movement[1])
        frect_pos = self.e_frect.x, self.e_frect.y

        
        # seperated collisions into x and y to make them easier
        
        for rect in tilemap.physics_rects_around(frect_pos):
            if self.e_frect.colliderect(rect):
                if frame_movement[0] < 0:# if movong right
                    self.e_frect.right = rect.left# the problem wiyh the ovement is something to do with this
                    self.collisions['right'] = True
                if frame_movement[0] > 0:# if moving left
                    self.e_frect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = self.e_frect.x# the problem wiyh the ovement is something to do with this


        for rect in tilemap.physics_rects_around(self.pos):# the problem wiyh the ovement is something to do with this
            if self.e_frect.colliderect(rect):
                if frame_movement[1] > 0:# moving down
                    self.e_frect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] <0:# moving left
                    self.e_frect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = self.e_frect.y
        
        if movement_input[0] > 0:# if move right then face right
            self.flip = False
        if movement_input[0] < 0:# if move left the flip to face left
            self.flip = True

        self.velocity[1] = min(5, self.velocity[1] + 0.1) # starts with with a down vel of 1 and increments by 0. until it reaches 5 which is terminal velocity

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

        self.animation.update()

    # dafluffypotatoes tutorial code
    def render(self, surf, offset = (0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1])) # sel.flip is the x axis flip and Fasle is the y-axis flip option, but flipping in the y - axis is verry reare so most of the time it is not needed


# dafluffypotatoes tutorial code
class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0
    # dafluffypotatoes tutorial code
    def update(self, tilemap, movement_input):
        super().update(tilemap, movement_input = movement_input)
        

        self.air_time += 1
        if self.collisions['down']: # if not touching the ground
            self.air_time = 0
        
        if self.air_time > 4:
            self.set_action('jump')
        elif movement_input[0] != 0:
            self.set_action('run')
        else:
            self.set_action('idle')


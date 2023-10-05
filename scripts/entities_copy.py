# all of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 

import pygame

# dafluffy potato tutorial code unless otherwise stated
class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0] # x velociyt then y velocity
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.action = ''
        self.anim_offset = (-3, 0) # so that the entitity img can overflow for the animations, can be set to (-3, -3) but then the player images need adjusting
        self.flip = False
        self.set_action('idle')

# my code unless otherwise stated        
        self.e_frect = pygame.FRect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.jump = False
        self.double_jump = False


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

# my code unless otherwise stated
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
        self.e_frect.move_ip(frame_movement[0], frame_movement[1])
        frect_pos = self.e_frect.x, self.e_frect.y

        
        # seperated collisions into x and y to make them easier


        """ I belive i have figured out what the problem with the zooming physics is
        self.e_frect.right = rect.left
        self.e_frect.left = rect.right
        self.e_frect.bottom = rect.top
        self.e_frect.top = rect.bottom
        
        when thes lines are commented out the character no longer zooms about, and instead moves at the normal
        speed, howver the charchter does have a tendencie to phase thourgh objects"""


        
        for rect in tilemap.physics_rects_around(self.pos):
            if self.e_frect.colliderect(rect):
                if frame_movement[0] < 0:# if movong right was > but it was moving the wrong way liek that for some reason
                    #self.e_frect.right = rect.left# the problem wiyh the ovement is something to do with this
                    
                    if self.e_frect.right == rect.left:# add something that locks the players axis coordss if they collide with something no that axis
                        print('work in progress')


                    self.collisions['right'] = True
                elif frame_movement[0] > 0:# if moving left
                    #self.e_frect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = self.e_frect.x# the problem wiyh the ovement is something to do with this


        for rect in tilemap.physics_rects_around(self.pos):# the problem wiyh the ovement is something to do with this
            if self.e_frect.colliderect(rect):
                if frame_movement[1] > 0:# moving down
                    self.e_frect.bottom = rect.top
                    self.collisions['down'] = True
                elif frame_movement[1] < 0:# moving left
                    self.e_frect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = self.e_frect.y

# dafluffy potato tutorial code unless otherwise stated
#         
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


# dafluffypotatoes tutorial code unless otherwise stated
class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0

        self.jump = False# my code
        self.double_jump = False# my code

    # dafluffypotatoes tutorial code
    def update(self, tilemap, movement_input):
        super().update(tilemap, movement_input = movement_input)

        # my code
        if self.collisions['down'] == True:# resest the jump counters if the player lands
            self.jump = False# my code
            self.double_jump = False# my code
        

        self.air_time += 1
        if self.collisions['down']: # if not touching the ground
            self.air_time = 0
        
        if self.air_time > 4:
            self.set_action('jump')
        elif movement_input[0] != 0:
            self.set_action('run')
        else:
            self.set_action('idle')


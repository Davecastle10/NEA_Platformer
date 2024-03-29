# all of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 

import os
import pygame

# dafluffypotatoes tutorial code
BASE_IMG_PATH = 'data/images/'

# dafluffypotatoes tutorial code
def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

# dafluffypotatoes tutorial code
def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images

# dafluffypotatoes tutorial code
class Animation:# update thsi in the future to have frames ov varying lengths rather than them being stuck at a constant 5 unnit length
    def __init__(self, images, img_dur = 5, loop = True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0

    # dafluffypotatoes tutorial code
    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    # dafluffypotatoes tutorial code
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
    
    # dafluffypotatoes tutorial code
    def img(self):
        return self.images[int(self.frame / self.img_duration)]
    
    # make a simple text function aswell that is less complicated




    


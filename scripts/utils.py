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

def display_text_simple(surf, text_pos, text_input, font):
    """A simple procedure to display black text on a surface

    Args:
        surf (surface you want to display text on): the surface that you want to display text on
        text_pos (tuple(int)): the x,y coords for the top left position of the text 
        text_input (str): the strig you want to be displayed as text 
        font (pygame font object): the pygame font object that you wnat to use as a base for the text 
    """    
    display_text = font.render(text_input, False, (1, 1, 1))
    surf.blit(display_text, text_pos)

    
def display_text_complicated(surf, text_pos, text_input, font, text_colour, bg_colour = None, wrap_length = 0):
    """A more advanced procedure to display text of a chosen colour with a chosen background colour that can wrap lines to a surface

    Args:
        surf (surface you want to display text on): _description_
        text_pos (tuple with the text location): _description_
        text_input (str): the string of text you want to display 
        font (a pygame.font.Font object): the pygame.font.Font object that has the txt size and font
        text_colour (RGB code list/tuple thingy): The Rgb code .
    """        
    display_text = font.render(text_input, False, text_colour, bg_colour, wrap_length)
    surf.blit(display_text, text_pos)


    


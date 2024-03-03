import pygame

class Text:
    def __init__(self, size = 8, font_name = 'Comic Sans'):# finish this later
        self.font = pygame.font.SysFont(font_name, size)

    def display_text_simple(self, surf, text_pos, text_input):
        """A simple procedure to display black text on a surface

        Args:
            surf (surface you want to display text on): the surface that you want to display text on
            text_pos (tuple(int)): the x,y coords for the top left position of the text 
            text_input (str): the strig you want to be displayed as text  
        """    
        display_text = self.font.render(text_input, False, (1, 1, 1))
        surf.blit(display_text, text_pos)

    
    def display_text_complicated(self,surf, text_pos, text_input, text_colour, bg_colour = None, wrap_length = 0):
        """A more advanced procedure to display text of a chosen colour with a chosen background colour that can wrap lines to a surface

        Args:
            surf (surface you want to display text on): _description_
            text_pos (tuple(int)): the top left corner of the text box in as (x,y) coords
            text_input (str): the string of text you want to display 
            text_colour (RGB code list/tuple thingy): The Rgb code .
        """        
        display_text = self.font.render(text_input, False, text_colour, bg_colour, wrap_length)
        surf.blit(display_text, text_pos)

class Auto_Wrapping_Text: # I was going to start working on this, and then utilised the other code in this file instead.
    def __init__(self, text_pos, text_destination_size, text_input, text_colour = (1, 1, 1), bg_colour = None):
        """A ccomplicated text class that creates text thwat will automatically change size and wrap to best fit the desired location.

        Args:
            text_pos (tuple(int)): the top left corner of the text box as (x,y) coords
            text_destination_size (tuple(int)): the size of the x and y dimensions of the text box
            text_input (str): the text you wish to dispay
            text_colour (tuple(int from 1 to 255), optional): the colour of the text you wish to display, not that it cannot be all as true black is transparent in the game. Defaults to (1, 1, 1).
            bg_colour (tuple(int from 1 to 255), optional):  the colour of the text you wish to display, not that it cannot be all as true black is transparent in the game. Defaults to None.
        """        
        pass


import pygame

class Button:
    """A class for buttons, that will most likely be used as a parent class for other GUI componets that I create in the future
    """    
    def __init__(self, input_pos = (0,0), input_text = "", input_size = (100, 40), ):
        """The constructor method for a Button object

        Args:
            input_pos (tuple of integers, optional): The (x,y) position of the top left hand corner of the Button. Defaults to (0,0).
            input_text (str, optional): The text to be dispayed on the button -when I get round to adding this feature. Defaults to "".
            input_size (tuple of integers, optional): The (x,y) size of the rect created for the button. Defaults to (100, 40).
        """        
        self.text_to_display = input_text
        self.size = input_size
        self.pos = input_pos
        
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render('Hello, World!', True, (189, 100, 185), None, int(self.size[0] * 0.9))
        self.button_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]) 
    
    def clicked(self, events_input):
        """A method used to see if the button has been clicked

        Args:
            events_input (list): inout the pygame.event.get events list into the function so it cna see if the mouse has clicked whilst hovering over the button

        Returns:
            Bool: Tru if the button ha been clicked and False if it hasn't 
        """        
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            for event in events_input:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return True
        else:
            return False
        
    def render(self, surf, image):
        """The function to render an image for the button onto the screen

        Args:
            surf (pygame surface/screen): The surface/screen that you wan the image of the button to render to
            image (.png or other image file): The image you want to render 
        """        
        surf.blit(image, self.pos)
        pygame.Surface.blit(self.text_surface, self.button_rect)



        





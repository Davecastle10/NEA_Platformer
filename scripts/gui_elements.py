import pygame


# .clicked method is not working, wo it might be worth just using the mousbutton checking in the game file instead of a specific
# method for now, also add docuemtnation about the failures and work to the word doc
# also add a docstrings to the code below





class Button:
    def __init__(self, input_pos = (0,0), input_text = "", input_size = (100, 40), ):
        self.text_to_display = input_text
        self.size = input_size
        self.pos = input_pos
        self.button_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def get_frect(self):
        pass
    
    def clicked(self, events_input):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            for event in events_input:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return True
        else:
            return False
        
    def render(self, surf, image):
        surf.blit(image, self.pos)


        





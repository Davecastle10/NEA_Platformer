import pygame

class Button:
    def __init__(self,input_pos, input_text = "", input_size = (20, 50), ):
        self.text_to_display = input_text
        self.size = input_size
        self.pos = input_pos
        self.button_frect = pygame.FRect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def get_frect(self):
        pass
    
    def clicked(self, mouse_pos):
        if self.button_frect.collidepoint(mouse_pos):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        return True
        else:
            return False
        





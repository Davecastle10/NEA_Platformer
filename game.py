import sys
import pygame 

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600,480))
        pygame.display.set_caption("NEA Platformer")

        self.clock = pygame.time.Clock()

        self.background_img_1 = pygame.image.load("assets/images/backgrounds/green_hills_1.png")

    
    def run(self):
        while True:
            self.screen.blit(self.background_img_1, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)


Game().run()
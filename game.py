import sys

import pygame 

from scripts.entities import PhysicsEntity




class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600,480))
        pygame.display.set_caption("NEA Platformer")

        self.clock = pygame.time.Clock()

        self.background_img_1 = pygame.image.load("assets/images/backgrounds/green_hills_1.png")

        self.player_img = pygame.image.load("assets/images/entities/player/player_v1.png")
        self.player_img_pos = [270, 190]
        self.player_img_movement = [False, False, False, False]


    def run(self):
        while True:
            self.screen.blit(self.background_img_1, (0, 0))

            self.player_img_pos[0] += self.player_img_movement[1] - self.player_img_movement[0]
            self.player_img_pos[1] += self.player_img_movement[3] - self.player_img_movement[2]

            self.screen.blit(self.player_img, self.player_img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player_img_movement[0] = True
                if event.key == pygame.K_RIGHT:
                    self.player_img_movement[1] = True
                if event.key == pygame.K_UP:
                    self.player_img_movement[2] = True
                if event.key == pygame.K_DOWN:
                    self.player_img_movement[3] = True



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player_img_movement[0] = False
                if event.key == pygame.K_RIGHT:
                    self.player_img_movement[1] = False
                if event.key == pygame.K_UP:
                    self.player_img_movement[2] = False
                if event.key == pygame.K_DOWN:
                    self.player_img_movement[3] = False

Game().run()
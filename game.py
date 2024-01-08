# most of this is from dafluffypotatos tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&t=6923s unless otherwaise stated atm 

import os
import sys
import pygame 
from pygame import freetype
import pygame_gui

import glob 

from scripts.utils import load_image, load_images,  Animation
from scripts.entities_copy import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
from scripts.questions import Question, Question_set
from scripts.gui_elements import Button
from scripts.text_stuff import Text






# dafluffypotatoes tutorial code unless otherwise stated
class Game:
    def __init__(self):
        pygame.init()

        self.display_x_size = 640
        self.display_y_size = 380

        pygame.display.set_caption("NEA Platformer")
        self.screen = pygame.display.set_mode((self.display_x_size * 2, self.display_y_size * 2))
        self.display = pygame.Surface((self.display_x_size, self.display_y_size))

        self.manager = pygame_gui.UIManager((self.display_x_size * 2, self.display_y_size * 2))
        self.hello_button_pressed = False


        self.clock = pygame.time.Clock()


        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player/idle/00.png'),
            'background': load_image('backgrounds/blue_sky_waves_big.png'),#mine
            'clouds' : load_images('clouds'),
            'start_screen' : load_image('backgrounds/start_screen_v2.png'),#mine
            'pause_screen' : load_image('backgrounds/pause_screen.png'),#mine
            'player/idle' : Animation(load_images('entities/player/idle'), img_dur=6),# currently dont have extra images of r the idle animation but this is for when i have made them
            'player/jump' : Animation(load_images('entities/player/jump'), img_dur=4),
            'player/run' : Animation(load_images('entities/player/run'), img_dur=5),
            'player/slide' : Animation(load_images('entities/player/slide'), img_dur=5),# no images yet
            'player/wall_slide' : Animation(load_images('entities/player/wall_slide'), img_dur=5),# no images yet
            'question_screen' : load_image('backgrounds/question_format.png'),
            'button_1_image' : load_image('gui/button_1.png'),
            'question_blocks' : load_images('tiles/question_blocks'),
        }
        
        self.clouds = Clouds(self.assets['clouds'], count = 16)

        self.player_movement = [False, False, False, False]
        self.player = Player(self, (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]

# my code unless otherwise stated
        self.alt = False
        self.paused = False
        self.started = False
        self.showing_questions = True

        self.chosen_question_set = Question_set(0)


        self.pixel_font = pygame.font.SysFont('Comic Sans', 8)
        self.question_font = pygame.font.SysFont('Comic Sans', 72)

        self.question_text_obj = Text(20, 'Comic Sans')
        self.answer_text_obj = Text(10, 'Comic Sans')
        self.small_text_obj = Text(8, 'Comic Sans')

        self.question_number = 0





        # creating a list of the file locations of the maps
        self.maps_path = 'data/maps'
        self.maps_list = list()
        for filename in glob.iglob(f'{self.maps_path}/*'):
            self.maps_list.append(filename)

        #self.current_map = 'data/maps/map.json' # don't think i need this anymore
        self.current_map_index = 0
        self.tilemap.load(self.maps_list[self.current_map_index])


        #self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.display_x_size - 50, self.display_y_size - 25), (100, 50)),
        #                                     text='Say Hello',
        #                                     manager=self.manager)

        # Gui objects and other stuff

        self.button_1 = Button()
        
        
    
    def run(self):
        while True:
            events_list = pygame.event.get()

            time_delta = self.clock.tick(60)

            if self.started == False:
                self.display.blit(self.assets['start_screen'], (0,0))

                for event in events_list:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if True in pygame.key.get_pressed():# if any key is pressed, start the game
                        self.started = True

            elif self.showing_questions == True:
                self.display.blit(self.assets['question_screen'], (0,0))

                # displaying the question
                self.question_text_obj.display_text_complicated(self.display, (66,60), self.chosen_question_set.get_question(self.question_number), (1, 1, 1), None, 511)

                # displaying the answers
                #correct answer in red corner
                self.answer_text_obj.display_text_complicated(self.display, (50,180), self.chosen_question_set.question_list[self.question_number].give_correct_answer(), (1, 1, 1), None, 250)
                #blue corner incorrect answer
                self.answer_text_obj.display_text_complicated(self.display, (335,180), self.chosen_question_set.question_list[self.question_number].incorrect_answer_1, (1, 1, 1), None, 250)
                #yellow corner incorrect answer
                self.answer_text_obj.display_text_complicated(self.display, (50,270), self.chosen_question_set.question_list[self.question_number].incorrect_answer_2, (1, 1, 1), None, 250)
                #green corner incorrect answer
                self.answer_text_obj.display_text_complicated(self.display, (335,270), self.chosen_question_set.question_list[self.question_number].incorrect_answer_3, (1, 1, 1), None, 250)

                for event in events_list:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.showing_questions = not(self.showing_questions)


            elif self.paused == True:
                self.display.blit(self.assets['pause_screen'], (0,0))
                



                for event in events_list:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.paused = not(self.paused)
                    if self.button_1.clicked(events_list) == True:
                        self.paused = not(self.paused)
                    





# dafluffypotatoes tutorial code unless otherwise stated
            else:
                self.display.blit(self.assets['background'], (0, 0))


                # scrolls camera to keep player in the center of the screen
                self.scroll[0] += (self.player.frect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
                self.scroll[1] += (self.player.frect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
                render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

                self.clouds.update()
                self.clouds.render(self.display, offset = render_scroll)

                self.tilemap.render(self.display, offset = render_scroll)

                self.player.update(self.tilemap, (self.player_movement[1] - self.player_movement[0], 0))
                self.player.render(self.display, offset = render_scroll)


                self.button_1.render(self.display, self.assets['button_1_image'])

            #print(self.tilemap.tiles_around(self.player.pos)) # used for error checking on what tiles are within a 3x3 radius


                self.small_text_obj.display_text_complicated(self.display, (2, 5), "Hello World", (1, 1, 1))




# all code from here down is mine unless otherwise stated
                """
                if self.hello_button_pressed == False:
                    self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.display_x_size - 50, self.display_y_size - 25), (100, 50)),
                                                text='Say Hello',
                                                manager=self.manager)"""



                

                

                for event in events_list:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if self.alt:# when pressing shift scroll thought tyle variants instead fo groups
                            if event.button == 4:
                                self.current_map_index = (self.current_map_index - 1) % len(self.maps_list)
                                self.tilemap.load(self.maps_list[self.current_map_index])
                                
                            if event.button == 5:
                                self.current_map_index = (self.current_map_index + 1) % len(self.maps_list)
                                self.tilemap.load(self.maps_list[self.current_map_index])
    

                    if event.type == pygame.KEYDOWN:
                        # if player wants to go left
                        if self.player.collisions['left'] == False:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                self.player_movement[0] = True
                        
                        # if the player wants to go right
                        if self.player.collisions['right'] == False:
                            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                self.player_movement[1] = True
                        
                        # this handles the double jumping
                        if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                            #if self.player.collisions['down'] == True:# resest the jump counters if the player lands
                            #    self.player.jump = False
                            #    self.player.double_jump = False
                            
                            if self.player.jump == False:# if the player hasnt jumped
                                self.player.velocity[1] = -3# jump
                                self.player.jump = True# can't jump agin until they land

                            elif self.player.double_jump == False:# if the player hasnt double jumped
                                self.player.velocity[1] = -3# double jump
                                self.player.double_jump = True# cant jump again until the player touches the ground

                            elif self.player.wall_jump == True:
                                self.player.velocity[1] = -3

                        if event.key == pygame.K_LALT:
                            self.alt = True
                        if event.key == pygame.K_ESCAPE:
                            self.paused = not(self.paused)
                        if event.key == pygame.K_RETURN:
                            self.started = True


                    if event.type == pygame.KEYUP:
                        # player wants to stop going left
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.player_movement[0] = False
                        
                        # player wanst to stop going right
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.player_movement[1] = False
                        
                        if event.key == pygame.K_LALT:
                            self.alt = False


                if self.button_1.clicked(events_list) == True:
                    self.paused = not(self.paused)
                
                    """
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.hello_button:
                            print('Hello World!')
                            self.hello_button_pressed == True

                    self.manager.process_events(event)"""

            #self.manager.update(time_delta)
# dafluffy potato tutorial code unless otherwise stated
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            #display_text(self.screen, (6, 14), "Hello World", self.pixel_font, (1, 1, 1))
            #self.manager.draw_ui(self.screen)
            pygame.display.update()
            #self.clock.tick(60)

Game().run()
import pygame
import sys
from settings import *
import os

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
#        print('call init')
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
        self.clock  = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.run()


        self.load()
    def run(self):
 #       print('call run')
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state =='playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


###################SUPPORT DEFS#################

# CENTRE CALL IN GENERAL BY SUBTRACTING THE POS - SIZE 
# POSITION CANNOT BE A TUPLE BECAUSE YOU CANT ACCESS INDEX, TUPLES SUCC ASS
    def draw_text(self, text, screen, size, pos, color, font_name, centred = False): 
 #       print(font_name)
        font = pygame.font.Font(font_name, 16)
        printing= font.render(text, False, color)
        text_size = printing.get_size()
        if centred == True:
            pos[0] = pos[0] - text_size[0]//2
            pos[1] = pos[1] - text_size[1]//2
        
        screen.blit(printing, pos)

    def load(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
    
    def draw_grid(self):
        for x in range(WIDTH//cell_width):
            pygame.draw.line(self.screen,GREY,(x*cell_width,0),(x*cell_width, HEIGHT))
        for y in range(HEIGHT//cell_height):
            pygame.draw.line(self.screen, GREY,(0, y*cell_height), (WIDTH, y*cell_height))






###################INTRO DEFS #################


    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
#        print('draw call')
        self.draw_text('PRESS SPACE BAR',self.screen, 38,[WIDTH//2,HEIGHT//2-50], (243,58,106),START_FONT, centred= True)
        self.draw_text('1 PLAYER MODE ONLY', self.screen, 22, [WIDTH//2, HEIGHT//2 + 50], (44, 168, 198), START_FONT, centred=True)
        self.draw_text('© 2021 Kartikeya Srivastava', self.screen, 22, [WIDTH//2, HEIGHT//2 + 100], (255, 255, 0), START_FONT, centred = True)
        self.draw_text('HIGH SCORE', self.screen, 12, [5,0], (0, 255, 0), START_FONT)
        self.draw_text('1P', self.screen, 12, [410, 0], (0, 255, 0), START_FONT)

                       
        pygame.display.update()

###################PLAYING DEFS #################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def playing_update(self):
        pass

    def playing_draw(self):
        self.load()
        self.screen.blit(self.background,(0,0))
#        print('called')
        self.draw_grid()
        pygame.display.update()
 

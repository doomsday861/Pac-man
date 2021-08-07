#!/usr/bin/env python
#coding: utf8 
import pygame
import sys
from settings import *
import os
from pac_class import *
from wallreader import *
pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
#        print('call init')
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
        self.clock  = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.pac = Pac(self,P_START_POS)
        self.walls = []
        self.dancer = wallreader.walread(self)
        print('wall size is '+str(len(self.walls)))
        self.run()



 #       self.load()
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
        self.background = pygame.image.load(MAZE_PATH)
        self.background = pygame.transform.scale(self.background, (MAZE_W, MAZE_H))

        #WALLS ON THE GRID COORDINATES
 
    
    def draw_grid(self):
        for x in range(WIDTH//cell_width):
            pygame.draw.line(self.background,RED,(x*cell_width,0),(x*cell_width, HEIGHT))
        for y in range(HEIGHT//cell_height):
            pygame.draw.line(self.background,RED,(0, y*cell_height), (WIDTH, y*cell_height))






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
        self.draw_text('1P', self.screen, 12, [580, 0], (0, 255, 0), START_FONT)

                       
        pygame.display.update()

###################PLAYING DEFS #################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
#                print(pygame.key.name)
                if event.key == pygame.K_UP:
                    print('up press')
                    self.pac.move(vec(0,-1))
                if event.key == pygame.K_DOWN:
                    print('down press')
                    self.pac.move(vec(0, 1))
                if event.key == pygame.K_LEFT:
                    print('left press')
                    self.pac.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    print('right press')
                    self.pac.move(vec(1, 0))


    def playing_update(self):
        self.pac.update()

    def playing_draw(self):
        self.load()
        self.screen.fill(BLACK)
        self.screen.blit(self.background,(TOP_BOTTOM_MARGIN//2,TOP_BOTTOM_MARGIN//2))
#        print('called')
        self.draw_grid()
        self.draw_text('HIGH SCORE: 0',self.screen,18,[10,5],GREEN,START_FONT)
        self.draw_text('CURRENT SCORE: 0', self.screen,18, [WIDTH//2, 5], GREEN, START_FONT)
        self.pac.draw()
        pygame.display.update()
 

#!/usr/bin/env python
#coding: utf8 
import pygame
import sys
from pygame.constants import KEYDOWN
from settings import *
import os
from pac_class import *
from wallreader import *
from ghost_class import *
pygame.init()
pygame.mixer.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
#        print('call init')
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
        pygame.display.set_caption('Pac-man')
        self.clock  = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.pac = Pac(self,vec(P_START_POS))
        self.walls = []
        self.coins = []
        self.ghosts =[]
        self.g_pos =[]
        self.dancer = wallreader.walread(self)
#        print('wall size is '+str(len(self.walls)))
#        print(self.walls)
 #       print(self.g_pos)
        self.make_ghosts()
        pygame.mixer.music.load("sound_intro.mp3")
        pygame.mixer.music.play()
#######image addition lines ##########
        self.pacmanL = []
        self.pacmanR =[]
        self.pacmanU =[]
        self.pacmanD =[]
        self.pacmanL.append(pygame.image.load(
            'sprite_pacman_left1.png').convert_alpha())
        self.pacmanL.append(pygame.image.load(
            'sprite_pacman_left2.png').convert_alpha())
        self.pacmanL.append(pygame.image.load(
            'sprite_pacman_left3.png').convert_alpha())
        self.pacmanR.append(pygame.image.load(
            'sprite_pacman_right1.png').convert_alpha())
        self.pacmanR.append(pygame.image.load(
            'sprite_pacman_right2.png').convert_alpha())
        self.pacmanR.append(pygame.image.load(
            'sprite_pacman_right3.png').convert_alpha())
        self.pacmanU.append(pygame.image.load(
            'sprite_pacman_up1.png').convert_alpha())
        self.pacmanU.append(pygame.image.load(
            'sprite_pacman_up2.png').convert_alpha())
        self.pacmanU.append(pygame.image.load(
            'sprite_pacman_up3.png').convert_alpha())
        self.pacmanD.append(pygame.image.load(
            'sprite_pacman_down1.png').convert_alpha())
        self.pacmanD.append(pygame.image.load(
            'sprite_pacman_down2.png').convert_alpha())
        self.pacmanD.append(pygame.image.load(
            'sprite_pacman_down3.png').convert_alpha())
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
            elif self.state == 'game over':
                self.game_over_events()
                self.game_over_update()
                self.game_over_draw()
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
        with open("walls.txt", "r") as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == 'B':
                        pygame.draw.rect(self.background, BLACK, (xidx*cell_width, yidx*cell_height, cell_width, cell_height))


    def make_ghosts(self):
        for idx,pos in enumerate(self.g_pos):
            self.ghosts.append(Ghost(self,vec(pos),idx))
    
    def draw_grid(self):
        for x in range(WIDTH//cell_width):
            pygame.draw.line(self.background,RED,(x*cell_width,0),(x*cell_width, HEIGHT))
        for y in range(HEIGHT//cell_height):
            pygame.draw.line(self.background,RED,(0, y*cell_height), (WIDTH, y*cell_height))
        for coin in self.coins:
            pygame.draw.rect(self.background,(167,179,34),(coin.x * cell_width, coin.y * cell_height,cell_width,cell_height))

    def reset(self):
        self.pac.lives = 3
        self.pac.grid_pos = vec(P_START_POS)
        self.pac.pix_pos = self.pac.get_pix_pos()
        self.pac.direction *= 0
        self.pac.current_score = 0
        self.coins = []
        for ghost in self.ghosts:
            ghost.grid_pos = vec(ghost.starting_pos)
            ghost.pix_pos = ghost.get_pix_pos()
            ghost.direction *= 0
        with open("walls.txt", "r") as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == '1':
                        self.walls.append(vec(xidx, yidx))
                    if char == 'C':
                        self.coins.append(vec(xidx, yidx))
                    if char in ["2", "3", "4", "5"]:
                        self.g_pos.append([xidx, yidx])
        self.state = 'playing'


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
        self.draw_text('?? 2021 Kartikeya Srivastava', self.screen, 22, [WIDTH//2, HEIGHT//2 + 100], (255, 255, 0), START_FONT, centred = True)
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
                    # print('up press')
                    self.pac.move(vec(0,-1))
                if event.key == pygame.K_DOWN:
                    # print('down press')
                    self.pac.move(vec(0, 1))
                if event.key == pygame.K_LEFT:
                    # print('left press')
                    self.pac.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    # print('right press')
                    self.pac.move(vec(1, 0))


    def playing_update(self):
        self.pac.update()
        for ghost in self.ghosts:
            ghost.update()

        for ghost in self.ghosts:
            if ghost.grid_pos == self.pac.grid_pos:
                self.remove_life()
            

    def playing_draw(self):
        self.load()
        self.screen.fill(BLACK)
#        self.draw_grid()
        self.screen.blit(self.background,(TOP_BOTTOM_MARGIN//2,TOP_BOTTOM_MARGIN//2))
        self.draw_coins()
#        print('called')
        self.draw_text('HIGH SCORE: 0',self.screen,18,[10,5],GREEN,START_FONT)
        self.draw_text('CURRENT SCORE: {}'.format(self.pac.current_score), self.screen,18, [WIDTH//2, 5], GREEN, START_FONT)
        self.pac.draw()
        for ghost in self.ghosts:
            ghost.draw()
        pygame.display.update()
        # self.coins.pop()
    
    def remove_life(self):
        self.pac.lives -=1
        pygame.mixer.music.load("sound_death.mp3")
        pygame.mixer.music.play()
        if self.pac.lives == 0:
            self.state = 'game over'
        else:
            # print(self.pac.lives)
            self.pac.grid_pos = vec(self.pac.starting_pos)
            self.pac.pix_pos = self.pac.get_pix_pos()
            self.pac.direction *=0
            for ghost in self.ghosts:
                ghost.grid_pos = vec(ghost.starting_pos)
                ghost.pix_pos = ghost.get_pix_pos()
                ghost.direction *=0
###COIN STUFF###
    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (124, 123, 7),
                               (int(coin.x*cell_width)+cell_width//2+TOP_BOTTOM_MARGIN//2,
                                int(coin.y*cell_height)+cell_height//2+TOP_BOTTOM_MARGIN//2), 5)


###################GAME OVER DEFS #################

    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def game_over_update(self):
        pass

    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press ESCAPE to QUIT"
        again_text = "Press SPACE BAR TO PLAY AGAIN"
        self.draw_text('GAME OVER ', self.screen, 198, [WIDTH//2, HEIGHT//2], RED, START_FONT, centred=True)
        self.draw_text(quit_text, self.screen, 58, [
                       WIDTH//2, HEIGHT//2+100], (135,123,251), START_FONT, centred=True)
        self.draw_text(again_text, self.screen, 58, [
                       WIDTH//2, HEIGHT//2+50], (255, 255, 0), START_FONT, centred=True)


        pygame.display.update()

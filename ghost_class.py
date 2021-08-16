from settings import *
import pygame
import app_class
import random

vec = pygame.math.Vector2

class Ghost:
    def __init__(self , app , pos ,number):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.radius = int(cell_width//2.3)
        self.number = number
        self.colour = self.set_colour()
        self.direction = vec(0,0)
        self.personality = self.set_personality()
        print(self.personality)

    def update(self):
        self.pix_pos +=self.direction

        if self.time_to_move():
            self.move()

            #THE RECTANGLE GRID TRACKING
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_MARGIN +
                            cell_width//2)//cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_MARGIN +
                            cell_height//2)//cell_height+1

    def draw(self):
        pygame.draw.circle(self.app.screen,self.colour,(int(self.pix_pos.x), int(self.pix_pos.y)),self.radius)

    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_MARGIN//2) % cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_MARGIN//2) % cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True
    
    def move(self):
        if self.personality == 'random':
            self.direction = self.get_random_direction()


    def get_random_direction(self):
        while True:
            number = random.randint(-2,1)
            if number == -2:
                x_dir,y_dir = 1,0
            elif number == -1:
                x_dir, y_dir = 0, 1
            elif number ==0:
                x_dir, y_dir = -1, 0
            else:
                x_dir, y_dir = 0, -1
            cur = vec(x_dir, y_dir)

            if vec(cur.x + self.grid_pos.x, cur.y + self.grid_pos.y) not in self.app.walls:
                break
        return vec(x_dir,y_dir)



    def get_pix_pos(self):
        print(self.grid_pos)
        return vec((self.grid_pos[0]*cell_width)+TOP_BOTTOM_MARGIN//2+cell_width//2, (self.grid_pos[1]*cell_height)+TOP_BOTTOM_MARGIN//2+cell_height//2)

    def set_colour(self):
        print(self.number)
        if self.number == 0:
            return (0,0,255)
        if self.number == 1:
            return (197,200,27)
        if self.number == 2:
            return (189,29,29)
        if self.number == 3:
            return (215, 159, 33)

    def set_personality(self):
        if self.number == 0:
            return "speedy"
        if self.number == 1:
            return "slow"
        if self.number == 2:
            return "random"
        else:
            return "scared"

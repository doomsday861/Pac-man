from settings import *
import pygame
import app_class
import random
import math

vec = pygame.math.Vector2

class Ghost:
    def __init__(self , app , pos ,number):
        self.app = app
        self.grid_pos = pos
        self.starting_pos = [pos.x,pos.y]
        self.pix_pos = self.get_pix_pos()
        self.radius = int(cell_width//2.3)
        self.number = number
        self.colour = self.set_colour()
        self.direction = vec(0,0)
        self.personality = self.set_personality()
        self.dir_giver = vec(0,0)
#        print(self.personality)
        self.target = None
        self.cur_frame =0
        self.speed = self.set_speed()
        self.ghost_1L = []
        self.ghost_1R =[]
        self.ghost_1U =[]
        self.ghost_1D =[]
        self.ghost_1L.append(pygame.image.load(
            'sprite_ghost_1_left1.png').convert_alpha())
        self.ghost_1L.append(pygame.image.load(
            'sprite_ghost_1_left2.png').convert_alpha())
        self.ghost_1R.append(pygame.image.load(
            'sprite_ghost_1_right1.png').convert_alpha())
        self.ghost_1R.append(pygame.image.load(
            'sprite_ghost_1_right2.png').convert_alpha())
        self.ghost_1U.append(pygame.image.load(
            'sprite_ghost_1_up1.png').convert_alpha())
        self.ghost_1U.append(pygame.image.load(
            'sprite_ghost_1_up2.png').convert_alpha())
        self.ghost_1D.append(pygame.image.load(
            'sprite_ghost_1_down1.png').convert_alpha())
        self.ghost_1D.append(pygame.image.load(
            'sprite_ghost_1_down2.png').convert_alpha())
        self.ghost_2L = []
        self.ghost_2R =[]
        self.ghost_2U =[]
        self.ghost_2D =[]
        self.ghost_2L.append(pygame.image.load(
            'sprite_ghost_2_left1.png').convert_alpha())
        self.ghost_2L.append(pygame.image.load(
            'sprite_ghost_2_left2.png').convert_alpha())
        self.ghost_2R.append(pygame.image.load(
            'sprite_ghost_2_right1.png').convert_alpha())
        self.ghost_2R.append(pygame.image.load(
            'sprite_ghost_2_right2.png').convert_alpha())
        self.ghost_2U.append(pygame.image.load(
            'sprite_ghost_2_up1.png').convert_alpha())
        self.ghost_2U.append(pygame.image.load(
            'sprite_ghost_2_up2.png').convert_alpha())
        self.ghost_2D.append(pygame.image.load(
            'sprite_ghost_2_down1.png').convert_alpha())
        self.ghost_2D.append(pygame.image.load(
            'sprite_ghost_2_down2.png').convert_alpha())
        self.ghost_3L = []
        self.ghost_3R =[]
        self.ghost_3U =[]
        self.ghost_3D =[]
        self.ghost_3L.append(pygame.image.load(
            'sprite_ghost_3_left1.png').convert_alpha())
        self.ghost_3L.append(pygame.image.load(
            'sprite_ghost_3_left2.png').convert_alpha())
        self.ghost_3R.append(pygame.image.load(
            'sprite_ghost_3_right1.png').convert_alpha())
        self.ghost_3R.append(pygame.image.load(
            'sprite_ghost_3_right2.png').convert_alpha())
        self.ghost_3U.append(pygame.image.load(
            'sprite_ghost_3_up1.png').convert_alpha())
        self.ghost_3U.append(pygame.image.load(
            'sprite_ghost_3_up2.png').convert_alpha())
        self.ghost_3D.append(pygame.image.load(
            'sprite_ghost_3_down1.png').convert_alpha())
        self.ghost_3D.append(pygame.image.load(
            'sprite_ghost_3_down2.png').convert_alpha())
        self.ghost_4L = []
        self.ghost_4R = []
        self.ghost_4U = []
        self.ghost_4D = []
        self.ghost_4L.append(pygame.image.load(
            'sprite_ghost_4_left1.png').convert_alpha())
        self.ghost_4L.append(pygame.image.load(
            'sprite_ghost_4_left2.png').convert_alpha())
        self.ghost_4R.append(pygame.image.load(
            'sprite_ghost_4_right1.png').convert_alpha())
        self.ghost_4R.append(pygame.image.load(
            'sprite_ghost_4_right2.png').convert_alpha()) 
        self.ghost_4U.append(pygame.image.load(
            'sprite_ghost_4_up1.png').convert_alpha())
        self.ghost_4U.append(pygame.image.load(
            'sprite_ghost_4_up2.png').convert_alpha())
        self.ghost_4D.append(pygame.image.load(
            'sprite_ghost_4_down1.png').convert_alpha())
        self.ghost_4D.append(pygame.image.load(
            'sprite_ghost_4_down2.png').convert_alpha())


    def update(self):
        self.target = self.set_target()

        if self.target != self.grid_pos:
            self.pix_pos +=self.direction * self.speed

            if self.time_to_move():
                self.move()

            #THE RECTANGLE GRID TRACKING
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_MARGIN +
                            cell_width//2)//cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_MARGIN +
                            cell_height//2)//cell_height+1

    def draw(self):
        if(self.number == 0):
            for i in range(0, 4):
                self.current_dir = self.get_current_dir()
                self.cur_frame += 0.004
                if(self.cur_frame >= 2):
                    self.cur_frame = 0
                if self.current_dir == 'right':
                    self.cur_image = self.ghost_1R[math.floor(self.cur_frame)]
                if self.current_dir == 'left':
                    self.cur_image = self.ghost_1L[math.floor(self.cur_frame)]
                if self.current_dir == 'up':
                    self.cur_image = self.ghost_1U[math.floor(self.cur_frame)]
                if self.current_dir == 'down':
                    self.cur_image = self.ghost_1D[math.floor(self.cur_frame)]
            self.app.screen.blit(self.cur_image,
                                 ((int(self.grid_pos[0]*cell_width+TOP_BOTTOM_MARGIN//2), int(self.grid_pos[1]*cell_height+TOP_BOTTOM_MARGIN//2))))
        if(self.number == 1):
            for i in range(0, 4):
                self.current_dir = self.get_current_dir()
                self.cur_frame += 0.004
                if(self.cur_frame >= 2):
                    self.cur_frame = 0
                if self.current_dir == 'right':
                    self.cur_image = self.ghost_2R[math.floor(self.cur_frame)]
                if self.current_dir == 'left':
                    self.cur_image = self.ghost_2L[math.floor(self.cur_frame)]
                if self.current_dir == 'up':
                    self.cur_image = self.ghost_2U[math.floor(self.cur_frame)]
                if self.current_dir == 'down':
                    self.cur_image = self.ghost_2D[math.floor(self.cur_frame)]
            self.app.screen.blit(self.cur_image,
                                 ((int(self.grid_pos[0]*cell_width+TOP_BOTTOM_MARGIN//2), int(self.grid_pos[1]*cell_height+TOP_BOTTOM_MARGIN//2))))
                            
        if(self.number == 2):
            for i in range(0, 4):
                self.current_dir = self.get_current_dir()
                self.cur_frame += 0.004
                if(self.cur_frame >= 2):
                    self.cur_frame = 0
                if self.current_dir == 'right':
                    self.cur_image = self.ghost_3R[math.floor(self.cur_frame)]
                if self.current_dir == 'left':
                    self.cur_image = self.ghost_3L[math.floor(self.cur_frame)]
                if self.current_dir == 'up':
                    self.cur_image = self.ghost_3U[math.floor(self.cur_frame)]
                if self.current_dir == 'down':
                    self.cur_image = self.ghost_3D[math.floor(self.cur_frame)]
            self.app.screen.blit(self.cur_image,
                                 ((int(self.grid_pos[0]*cell_width+TOP_BOTTOM_MARGIN//2), int(self.grid_pos[1]*cell_height+TOP_BOTTOM_MARGIN//2))))

        if(self.number == 3):
            for i in range(0, 4):
                self.current_dir = self.get_current_dir()
                self.cur_frame += 0.004
                if(self.cur_frame >= 2):
                    self.cur_frame = 0
                if self.current_dir == 'right':
                    self.cur_image = self.ghost_4R[math.floor(self.cur_frame)]
                if self.current_dir == 'left':
                    self.cur_image = self.ghost_4L[math.floor(self.cur_frame)]
                if self.current_dir == 'up':
                    self.cur_image = self.ghost_4U[math.floor(self.cur_frame)]
                if self.current_dir == 'down':
                    self.cur_image = self.ghost_4D[math.floor(self.cur_frame)]
            self.app.screen.blit(self.cur_image,
                                 ((int(self.grid_pos[0]*cell_width+TOP_BOTTOM_MARGIN//2), int(self.grid_pos[1]*cell_height+TOP_BOTTOM_MARGIN//2))))





    def get_current_dir(self):
#        print(self.dir_giver)
        if(self.dir_giver == vec(1, 0)):
            return "right"
        if(self.dir_giver == vec(-1, 0)):
            return "left"
        if(self.dir_giver == vec(0, -1)):
            return "up"
        if(self.dir_giver == vec(0, 1)):
            return "down"
        else:
            return "right"


    def set_speed(self):
        if self.personality == 'speedy':
            return 2
        else:
            return 1

    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_MARGIN//2) % cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0) or self.direction == vec(0,0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_MARGIN//2) % cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0) or self.direction == vec(0,0):
                return True
    
    def set_target(self):
        if self.personality == 'speedy' or self.personality == 'slow':
            return self.app.pac.grid_pos
        else:
            if self.app.pac.grid_pos[0] > COLS//2 and self.app.pac.grid_pos[1] > ROWS//2:
                return vec(1,1)
            elif self.app.pac.grid_pos[0] > COLS//2 and self.app.pac.grid_pos[1] < ROWS//2:
                return vec(1, ROWS-2)
            elif self.app.pac.grid_pos[0] < COLS//2 and self.app.pac.grid_pos[1] > ROWS//2:
                return vec(COLS-2, 1)
            else:
                return vec(COLS-2, ROWS-2)



    def move(self):
        if self.personality == 'random':
            self.direction = self.get_random_direction()
        if self.personality == 'slow':
            self.direction = self.get_path_direction(self.target)
        if self.personality == 'speedy':
            self.direction = self.get_path_direction(self.target)
        if self.personality == 'scared':
            self.direction = self.get_path_direction(self.target)

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
        self.dir_giver = vec(x_dir,y_dir)
        return vec(x_dir,y_dir)

    def get_path_direction(self,target):
        curr_cell = self.next_cell(target)
        xdir = curr_cell[0] - self.grid_pos[0]
        ydir = curr_cell[1] - self.grid_pos[1]
        self.dir_giver = vec(xdir,ydir)
        return vec(xdir, ydir)
    
    def next_cell(self,target):
        # print(self.personality)
        # print("grid pos"+str(type(self.grid_pos)))
        # print("target type "+str(type(self.target)))
        path = self.BFS([int(self.grid_pos.x), int(self.grid_pos.y)],[int(self.target[0]),int(self.target[1 ])])
        return path[1]

    def BFS(self,start, target):
        grid = [[0 for x in range(28)] for x in range(30)]
        for cell in self.app.walls:
            if cell.x < 28 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)]  = 1
            
        queue = [start]
        path =[]    
        vis = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            vis.append(current)
            
            if current == target:
                break
            
            else:
                neighbours = [[0,-1],[1,0],[0,1],[-1,0]]
                for neighbour in neighbours:
                    if neighbour[0] + current[0] >=0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1] + current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0],neighbour[1] + current[1]]
                            if next_cell not in vis:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
        
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0,step["Current"]) 
        
        return shortest

#lives dont work man idk wtf to do


    def get_pix_pos(self):
#        print(self.grid_pos)
        return vec((self.grid_pos[0]*cell_width)+TOP_BOTTOM_MARGIN//2+cell_width//2, (self.grid_pos[1]*cell_height)+TOP_BOTTOM_MARGIN//2+cell_height//2)

    def set_colour(self):
#        print(self.number)
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

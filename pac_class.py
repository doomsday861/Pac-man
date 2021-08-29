from settings import *
import pygame
import app_class
import time
vec = pygame.math.Vector2
class Pac:
    def __init__(self,app,pos): 
        self.app = app
        self.grid_pos = pos
        self.starting_pos = pos   
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.stored_direction = None
        self.able_to_move = True
        self.speed = 2
        self.current_score =0
        self.lives = 3
        self.cur_frame =0
 
    def update(self):
        if self.able_to_move:
            self.pix_pos += self.direction*self.speed
        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction

            self.able_to_move = self.can_move()

        if self.on_coin():
            self.eat_coin()

 
        #THE RECTANGLE GRID TRACKING
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_MARGIN +
                            cell_width//2)//cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_MARGIN +
                            cell_height//2)//cell_height+1
    
    def draw(self):
        #pygame.draw.circle(self.app.screen,GREEN,(int(self.pix_pos.x),int(self.pix_pos.y)),cell_width//2-2)
        # pygame.draw.rect(self.app.screen,RED,(int(self.grid_pos[0]*cell_width+TOP_BOTTOM_MARGIN//2),int(self.grid_pos[1]*cell_height+TOP_BOTTOM_MARGIN//2),cell_width,cell_height),1)
        self.current_dir = self.get_current_dir()
        for i in range(0,3):
            self.cur_frame +=0.04
            if(self.cur_frame>=3.0):
                self.cur_frame = 0
            if self.current_dir == 'right':
                self.cur_image = self.app.pacmanR[int(self.cur_frame)]
            if self.current_dir == 'left':
                self.cur_image = self.app.pacmanL[int(self.cur_frame)]
            if self.current_dir == 'up':
                self.cur_image = self.app.pacmanU[int(self.cur_frame)]
            if self.current_dir == 'down':
                self.cur_image = self.app.pacmanD[int(self.cur_frame)]
#            print(self.cur_frame)
            self.app.screen.blit(self.cur_image,
                             ((int(self.grid_pos[0]*cell_width+TOP_BOTTOM_MARGIN//2), int(self.grid_pos[1]*cell_height+TOP_BOTTOM_MARGIN//2))))
 
            for x in range (self.lives):
                self.app.screen.blit(self.app.pacmanR[int(self.cur_frame)%2+1],(30 + 15*x,HEIGHT- 15))
   
    def get_current_dir(self):
        if(self.stored_direction== vec(1,0)):
            return "right"
        if(self.stored_direction == vec(-1, 0)):
            return "left"
        if(self.stored_direction == vec(0, -1)):
            return "up"
        if(self.stored_direction == vec(0, 1)):
            return "down"
        else:
            return "right"


    def move(self,direction):
 #       print('brooooo workkk')
        self.stored_direction = direction
    
    def get_pix_pos(self):
        print(self.grid_pos)
        return vec((self.grid_pos[0]*cell_width)+TOP_BOTTOM_MARGIN//2+cell_width//2, (self.grid_pos[1]*cell_height)+TOP_BOTTOM_MARGIN//2+cell_height//2)


    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_MARGIN//2) % cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_MARGIN//2) % cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True


    def can_move(self):
            for wall in self.app.walls:
                if vec(self.grid_pos+self.direction) == wall:
                    return False
            return True

    def on_coin(self):
        if self.grid_pos in self.app.coins:
#             print('coin pass')
#             self.app.coins.remove(self.grid_pos)
                if int(self.pix_pos.x+TOP_BOTTOM_MARGIN//2) % cell_width == 0:
                    if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                        return True
                if int(self.pix_pos.y+TOP_BOTTOM_MARGIN//2) % cell_height == 0:
                    if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                        return True
        return False
        
    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        # pygame.mixer.init()
        if self.current_score % 2 == 0:
            pygame.mixer.music.load("sound_chomp1.wav")
        else:
            pygame.mixer.music.load("sound_chomp2.wav")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()
        self.current_score +=1

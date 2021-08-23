from settings import *
import pygame
import app_class
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
        pygame.draw.circle(self.app.screen,GREEN,(int(self.pix_pos.x),int(self.pix_pos.y)),cell_width//2-2)
        # pygame.draw.rect(self.app.screen,RED,(int(self.grid_pos[0]*cell_width+TOP_BOTTOM_MARGIN//2),int(self.grid_pos[1]*cell_height+TOP_BOTTOM_MARGIN//2),cell_width,cell_height),1)
        for x in range (self.lives):
            pygame.draw.circle(self.app.screen,GREEN,(30 + 15*x,HEIGHT- 15),7)
   
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
        self.current_score +=1

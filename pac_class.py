from settings import *
import pygame
vec = pygame.math.Vector2
class Pac:
    def __init__(self,app,pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)

    def get_pix_pos(self):
        return vec((self.grid_pos.x*cell_width)+TOP_BOTTOM_MARGIN//2 + cell_width//2, (self.grid_pos.y*cell_height)+TOP_BOTTOM_MARGIN//2+cell_height//2)
       # print(self.grid_pos, self.pix_pos)
    
    def update(self):
        self.pix_pos +=self.direction 
        #THE RECTANGLE GRID TRACKING
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_MARGIN+cell_width//2)//cell_width+0.8
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_MARGIN+cell_height//2)//cell_height-0.3
    
    def draw(self):
        pygame.draw.circle(self.app.screen,GREEN,(int(self.pix_pos.x),int(self.pix_pos.y)),cell_width//2-2)
        pygame.draw.rect(self.app.screen,RED,(int(self.grid_pos[0]*cell_width+TOP_BOTTOM_MARGIN//2),int(self.grid_pos[1]*cell_height+TOP_BOTTOM_MARGIN),cell_width,cell_height),1)
    def move(self,direction):
        self.direction = direction

from settings import *
import pygame
vec = pygame.math.Vector2
class Pac:
    def __init__(self,app,pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = vec((self.grid_pos.x*cell_width)+TOP_BOTTOM_MARGIN//2 + cell_width//2,(self.grid_pos.y*cell_height)+TOP_BOTTOM_MARGIN//2+cell_height//2)
        print(self.grid_pos, self.pix_pos)
    
    def update(self):
        pass
    
    def draw(self):
        pygame.draw.circle(self.app.screen,GREEN,(int(self.pix_pos.x),int(self.pix_pos.y)),cell_width//2-2)
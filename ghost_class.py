from settings import *
import pygame
import app_class

vec = pygame.math.Vector2

class Ghost:
    def __init__(self,app,pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.radius = int(cell_width//2.3)
    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen,(255,0,0),(int(self.pix_pos.x), int(self.pix_pos.y)),self.radius)

    def get_pix_pos(self):
        print(self.grid_pos)
        return vec((self.grid_pos[0]*cell_width)+TOP_BOTTOM_MARGIN//2+cell_width//2, (self.grid_pos[1]*cell_height)+TOP_BOTTOM_MARGIN//2+cell_height//2)

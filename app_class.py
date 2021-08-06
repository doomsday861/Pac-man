import pygame
import sys
from settings import *

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
    
    def run(self):
 #       print('call run')
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            else:
                pass
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


###################SUPPORT DEFS#################
    def draw_text(self, text, screen, size, pos, color, font_name):
#        print('text_called')
        font = pygame.font.SysFont(font_name, size)
        printing= font.render(text, False, color)
        text_size = printing.get_size()
        pos[0] = pos[0] - text_size[0]//2
        pos[1] = pos[1] - text_size[1]//2
        screen.blit(printing, pos)

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
        self.draw_text('PUSH SPACE BAR',self.screen, START_TEXT_SIZE,[WIDTH//2,HEIGHT//2], (170,132,158),START_FONT)
        pygame.display.update()

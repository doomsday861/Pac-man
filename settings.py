from pygame.math import Vector2 as vec
#height and width of the program
WIDTH,HEIGHT = 610,670
TOP_BOTTOM_MARGIN = 50
ROWS = 30
COLS = 28
MAZE_W = WIDTH - TOP_BOTTOM_MARGIN
MAZE_H = HEIGHT - TOP_BOTTOM_MARGIN
cell_width = MAZE_W//28
cell_height = MAZE_H//30

#FRAMES PS
FPS = 60
#color default
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (107,107,107)
GREEN =(0,255,0)
#START SCREEN SETTINGS
START_TEXT_SIZE = 32
START_FONT = 'PressStart2P-vaV7.ttf'
#MAZE PATH CHANGE ON WINDOWS (ONLY FOR OSX FOR NOW)
MAZE_PATH = 'maze.png'
#PLAYER SETTINGS
P_START_POS = [1,1]
#print('setting call')

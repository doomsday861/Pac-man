from app_class import *
from settings import *
class wallreader:
    def walread(self):       
        with open("walls.txt", "r") as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == '1':
                        self.walls.append(vec(xidx, yidx))
                    if char =='C':
                        self.coins.append(vec(xidx, yidx))
                    if char in ["2","3","4","5"]:
                        self.g_pos.append([xidx,yidx])
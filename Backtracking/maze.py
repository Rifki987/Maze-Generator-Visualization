import pygame as pg
from random import choice
from utils import square_type, BLACK,WHITE,CLOCK
class maze:
    move_possible = {"left":(0,-1),
                     "right":(0,1),
                     "top":(-1,0),
                     "bottom":(1,0)}
    def __init__(self,screen,col:int,row:int):
        self.screen = screen
        self.col = col
        self.row = row
        
    
    def generate(self):
        rowspan = (self.screen.get_height())/self.row
        colspan = (self.screen.get_width())/self.col
        self.all_square: list[list[square_type]]=[[square_type(self.screen,col*colspan,row*rowspan,colspan,rowspan) for col in range(self.col) ] for row in range(self.row)]
    
    def all_possible_move(self,r_idx:int,c_idx:int):
        result =[]   # it will be in formatt tuple (row,col)
        #check left side
        if c_idx>0:
            if not self.all_square[r_idx][c_idx-1].STATUS:
                result.append((r_idx,c_idx-1))
        # check up side
        if r_idx>0:
            if not self.all_square[r_idx-1][c_idx].STATUS:
                result.append((r_idx-1,c_idx))
        #check Bottom
        if r_idx<self.row:
            if not self.all_square[r_idx+1][c_idx].STATUS:
                result.append((r_idx+1,c_idx))
        # check right side
        if c_idx<self.col:
            if not self.all_square[r_idx][c_idx+1].STATUS:
                result.append((r_idx,c_idx+1))
        return result

    def validation(self, r_idx, c_idx)-> bool:
        # True mean valid and unvisited yet , and false mean already visisted and not valid
        if (not (-1<r_idx<self.row)) or (not (-1<c_idx<self.col)):
            return False
        return self.all_square[r_idx][c_idx].STATUS
    def redraw_method(self,r_idx,c_idx,direction):
        if direction=="left":
            current : square_type = self.all_square[r_idx][c_idx]
            current.left = True
            current.draw()
            left_current: square_type = self.all_square[r_idx][c_idx-1]
            left_current.right = True
            left_current.draw()
        elif direction=="right":
            current : square_type = self.all_square[r_idx][c_idx]
            current.right = True
            current.draw()
            left_current: square_type = self.all_square[r_idx][c_idx+1]
            left_current.left = True
            left_current.draw()
        elif direction=="top":
            current : square_type = self.all_square[r_idx][c_idx]
            current.up = True
            current.draw()
            left_current: square_type = self.all_square[r_idx-1][c_idx]
            left_current.bottom = True
            left_current.draw()
        elif direction=="bottom":
            current : square_type = self.all_square[r_idx][c_idx]
            current.bottom = True
            current.draw()
            left_current: square_type = self.all_square[r_idx+1][c_idx]
            left_current.up = True
            left_current.draw()
        
        CLOCK.tick(30)
        pg.display.flip()

    def backtrack_method(self,r_idx,c_idx):
        self.all_square[r_idx][c_idx].STATUS = False
        possible_move:list = list(self.move_possible.keys())
        for i in range(4):
            direction =choice(possible_move)
            koordinate = (self.move_possible[direction][0]+r_idx,self.move_possible[direction][1]+c_idx)
            if not self.validation(*koordinate):

                possible_move.remove(direction)
                continue
            # rendering 
            self.redraw_method(r_idx,c_idx,direction)
            self.backtrack_method(*koordinate)
    def update(self):
        self.backtrack_method(0,0)
import pygame as pg

WHITE=(255, 255, 255)
BLACK = (0, 0, 0)
CLOCK = pg.time.Clock()

class square_type:
    width = 2
    def __init__(self,parent_screen,pos_col,pos_row,colspan,rowspan):
        self.screen:pg.display = parent_screen
        self.pos_col = pos_col
        self.pos_row = pos_row
        self.colspan = colspan
        self.rowspan = rowspan
        self.left=False
        self.right=False
        self.up=False
        self.bottom = False
        self.STATUS = True    #  True Mean unvisited yet
        self.surf = pg.Surface((self.colspan+1,self.rowspan+1))
        self.draw()

    def draw(self):
        self.surf.fill(BLACK)
        if not self.up:
            pg.draw.line(self.surf,WHITE,(0,0),(self.colspan,0),self.width)
        if not self.bottom:
            pg.draw.line(self.surf,WHITE,(0,self.rowspan),(self.colspan,self.rowspan),self.width)
        if not self.left:
            pg.draw.line(self.surf,WHITE,(0,0),(0,self.rowspan),self.width)  
        if not self.right:
            pg.draw.line(self.surf,WHITE,(self.colspan,0),(self.colspan,self.rowspan),self.width)
        self.render()
    
    def render(self):
        self.screen.blit(self.surf,(self.pos_col,self.pos_row))

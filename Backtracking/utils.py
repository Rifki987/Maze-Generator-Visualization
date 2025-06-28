import pygame as pg

WHITE=(255, 255, 255)
BLACK = (0, 0, 0)
CLOCK = pg.time.Clock()

class square:
    """
    Represents a single cell in a maze grid for backtracking-based maze generation.

    Each instance of this class corresponds to one square in the grid and is responsible 
    for rendering itself to the Pygame screen, including its walls.

    Attributes:
        width (int): The thickness of the wall lines.
        screen (pg.display): The Pygame surface where this square is rendered.
        pos_col (int): The x-coordinate (in pixels) of the square's top-left corner on the screen.
        pos_row (int): The y-coordinate (in pixels) of the square's top-left corner on the screen.
        colspan (int): The width (in pixels) of the square.
        rowspan (int): The height (in pixels) of the square.
        left (bool): Whether the left wall is removed (False = wall exists).
        right (bool): Whether the right wall is removed (False = wall exists).
        up (bool): Whether the top wall is removed (False = wall exists).
        bottom (bool): Whether the bottom wall is removed (False = wall exists).
        STATUS (bool): Whether the square is unvisited (True) or already visited (False).
        surf (pg.Surface): Internal surface representing this cell, used for drawing before rendering to screen.

    Methods:
        draw():
            Draws the cell, including its walls based on the left/right/up/bottom flags.
        
        render():
            Blits the internal surface (`surf`) onto the main screen at the appropriate position.

    Usage:
        This class is intended to be used as part of a grid structure in maze generation.
        Walls are removed during maze creation by setting the corresponding wall attributes to True.
    """

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

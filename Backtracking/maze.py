import pygame as pg
from random import choice
from utils import square, BLACK,WHITE,CLOCK
class maze:
    """
    A class to generate and render a maze using the recursive backtracking algorithm with Pygame.

    This class uses a grid of `square` objects (imported from utils) to represent each cell in the maze.
    Each square starts with all walls intact, and the algorithm carves a path by removing walls
    between adjacent squares while marking visited cells.

    Attributes:
        move_possible (dict): A mapping of movement directions to row/column offsets.
        screen (pg.Surface): The Pygame surface where the maze is rendered.
        col (int): Number of columns in the maze grid.
        row (int): Number of rows in the maze grid.
        board (list[list[square]]): 2D grid of square objects representing the maze.

    Methods:
        __init__(screen, col, row):
            Initializes the maze with the given screen and grid size.

        generate():
            Creates and initializes the 2D board with square objects, calculating their sizes
            based on the screen dimensions.

        validation(r_idx, c_idx) -> bool:
            Returns True if the given cell coordinates are inside the grid bounds
            and have not been visited yet.

        redraw_method(r_idx, c_idx, direction):
            Removes the wall between the current square and its neighbor in the given direction,
            updates their appearance on screen, and controls rendering speed using CLOCK.

        backtrack_method(r_idx, c_idx):
            Core recursive method that visits a square, randomly chooses an unvisited neighbor,
            carves a path to it, and continues recursively. Implements depth-first traversal.

        update():
            Entry point to start generating the maze from the top-left corner (0, 0).

    Usage:
        - Create a `maze` instance by passing the Pygame screen and desired grid size.
        - Call `generate()` to build the initial maze grid.
        - Call `update()` to begin generating the maze using recursive backtracking.

    Dependencies:
        - `square` class from utils: Represents individual cells of the maze.
        - `BLACK`, `WHITE`, `CLOCK`: Constants and a clock object from utils for rendering control.
    """

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
        self.board: list[list[square]]=[[square(self.screen,col*colspan,row*rowspan,colspan,rowspan) for col in range(self.col) ] for row in range(self.row)]
    

    def validation(self, r_idx, c_idx)-> bool:
        # True mean valid and unvisited yet , and false mean already visisted and not valid
        if (not (-1<r_idx<self.row)) or (not (-1<c_idx<self.col)):
            return False
        return self.board[r_idx][c_idx].STATUS
    def redraw_method(self,r_idx,c_idx,direction):
        if direction=="left":
            current : square = self.board[r_idx][c_idx]
            current.left = True
            current.draw()
            left_current: square = self.board[r_idx][c_idx-1]
            left_current.right = True
            left_current.draw()
        elif direction=="right":
            current : square = self.board[r_idx][c_idx]
            current.right = True
            current.draw()
            left_current: square = self.board[r_idx][c_idx+1]
            left_current.left = True
            left_current.draw()
        elif direction=="top":
            current : square = self.board[r_idx][c_idx]
            current.up = True
            current.draw()
            left_current: square = self.board[r_idx-1][c_idx]
            left_current.bottom = True
            left_current.draw()
        elif direction=="bottom":
            current : square = self.board[r_idx][c_idx]
            current.bottom = True
            current.draw()
            left_current: square = self.board[r_idx+1][c_idx]
            left_current.up = True
            left_current.draw()
        
        CLOCK.tick(30)
        pg.display.flip()

    def backtrack_method(self,r_idx,c_idx):
        # Even handling for quitting the game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        # Base case
        self.board[r_idx][c_idx].STATUS = False
        possible_move:list = list(self.move_possible.keys())
        for _ in range(4):
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
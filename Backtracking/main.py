
import pygame as pg
from maze import maze
"""
Main module to run the maze visualization using recursive backtracking.

This script initializes Pygame, sets up the display window, and creates an instance of the `maze` class
(from the `maze` module). The maze is then generated and visualized on screen using recursive backtracking.

Functions:
    main(row_size, col_size) -> None:
        Initializes the Pygame environment, creates the maze instance, and handles the event loop
        to keep the window open until the user quits.

Usage:
    Run this script directly to start the maze generation visualization.

Example:
    if __name__ == "__main__":
        row_size = 30
        col_size = 50
        main(row_size, col_size)
"""
def main(row_size,col_size)->None:
    """
    Entry point for the maze visualization application.

    Args:
        row_size (int): Number of rows in the maze grid.
        col_size (int): Number of columns in the maze grid.

    This function:
    - Initializes Pygame and the display screen.
    - Creates a `maze` instance with the specified grid dimensions.
    - Calls `generate()` to initialize the grid of squares.
    - Calls `update()` once to begin generating the maze using recursive backtracking.
    - Runs an event loop to keep the Pygame window open until the user closes it.
    """
    pg.init()
    screen = pg.display.set_mode((1000, 650))
    pg.display.set_caption("Backtrack Maze Visualization")
    Maze=maze(screen,col_size,row_size)
    Maze.generate()

    # Event loop
    Maze.update()  # Start generating the maze using recursive backtracking
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        pg.display.flip()
        
    pg.quit()


if __name__=="__main__":
    row_size = 30
    col_size = 50
    main(row_size,col_size)
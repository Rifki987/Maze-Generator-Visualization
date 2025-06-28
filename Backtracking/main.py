
import pygame as pg
from maze import maze
def main()->None:
    pg.init()
    screen = pg.display.set_mode((1000, 650))
    pg.display.set_caption("Backtrack Maze Visualization")
    Maze=maze(screen,16,12)
    Maze.generate()

    # Event loop
    running = True
    while running:
        Maze.update()        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        pg.display.flip()
        
    pg.quit()


if __name__=="__main__":
    main()
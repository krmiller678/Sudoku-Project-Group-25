"""
Object Oriented pygame event gui
"""
from constants_new import *
import pygame,sys
from cell_new import Cell
from board_new import Board

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)
    
    board = Board(WIDTH, HEIGHT, screen, 30)
    board.draw()

    while True:
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
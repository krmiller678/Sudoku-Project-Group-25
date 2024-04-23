"""
Implementation of Board class
The Board class is the class our main function instantiate 
Board class creates a list of Cell class instances for storing the true value
and sketched value of Sudoku cells
"""

from constants_new import *
import pygame, sys
from cell_new import Cell
from sudoku_generator import generate_sudoku, SudokuGenerator


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty #difficulty is an int

    def draw(self):
        for i in range(1, 9):
            #draw rows
            if i % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LARGE_LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
                
        for i in range(1, 9):
        #draw cols
            if i % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                            (SQUARE_SIZE * i, WIDTH), LARGE_LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                            (SQUARE_SIZE * i, WIDTH), LINE_WIDTH)
                    
        #draw cells
        self.board = generate_sudoku(9,self.difficulty)
        #THIS will be super useful for resetting same board
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]
        #loop through to draw all
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

    def select(self, row, col):
        self.cells[row][col].selected = True
        self.cells[row][col].draw()
        return self.cells[row][col]

    def click(self,x,y):
        row = x // SQUARE_SIZE
        col = y // SQUARE_SIZE
        if row < 9 and col < 9:
            return (int(row),int(col))
        else:
            return None
    
    def clear(self, target):
        #needs to take a cell object as an input
        target.set_cell_value(0)
        target.set_sketched_value(0)
        target.draw()

    def sketch(self,target,value):
        #needs to take a cell object as an input
        target.set_sketched_value(value)
        target.draw()


    def place_number(self,target,value):
        #needs to take a cell object as an input
        target.set_cell_value(value)
        target.draw()

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    self.cells[i][j].value = 0
                    self.cells[i][j].draw()

    def is_full(self):
        #sweeps the whole board looking for real value == 0
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return False
        return True

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        #implements our SudokuGenerator to access is_valid method
        self.board_new = SudokuGenerator(9,0)
        self.board_new.board = [[self.cells[i][j].value for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if not self.board_new.is_valid(i,j,self.board_new.board[i][j]):
                    return False
        return True
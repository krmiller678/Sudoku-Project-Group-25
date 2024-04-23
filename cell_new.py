"""
Implementation of Cell class
The cell class contains the initial value, sketched value, and instructions on
drawing the values to fill the board based on Sudoku Generator numbers
"""

from constants_new import *
import pygame, sys

class Cell:
    def __init__(self,value,row,col,screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self,value):
        #setter to update the cells value -> initially we will have 0s in
        #multiple positions
        self.value = value

    def set_sketched_value(self,value):
        #set up new instance attribute, sketched_value
        self.sketched_value = value

    def draw(self):
        #draws value - note that row and col are 0 indexed
        integer_font = pygame.font.Font(None, INT_FONT)
        if self.value != 0:
            integer = str(self.value)
            integer_surf = integer_font.render(integer, 0, DEFAULT_NUMBER_COLOR)
            integer_rect = integer_surf.get_rect(
                    center=(SQUARE_SIZE * self.row + SQUARE_SIZE/2, SQUARE_SIZE * self.col + SQUARE_SIZE/2))
            self.screen.blit(integer_surf, integer_rect)
        #adding in some more useful conditionals:
        elif self.sketched_value != 0:
            integer = str(self.value)
            integer_surf = integer_font.render(integer, 0, SKETCHED_NUMBER_COLOR)
            integer_rect = integer_surf.get_rect(
                    center=(SQUARE_SIZE * self.row + SQUARE_SIZE/2, SQUARE_SIZE * self.col + SQUARE_SIZE/2))
            self.screen.blit(integer_surf, integer_rect)
            if self.selected == True:
                pygame.draw.rect(self.screen,RED,[SQUARE_SIZE*self.row,SQUARE_SIZE*self.col,SQUARE_SIZE,SQUARE_SIZE],2)
            else:
                pygame.draw.rect(self.screen,LINE_COLOR,[SQUARE_SIZE*self.row,SQUARE_SIZE*self.col,SQUARE_SIZE,SQUARE_SIZE],2)
        else: #self.value == 0
            #clears out a cell
            integer_surf = integer_font.render(None, 0, DEFAULT_NUMBER_COLOR)
            integer_rect = integer_surf.get_rect(
                    center=(SQUARE_SIZE * self.row + SQUARE_SIZE/2, SQUARE_SIZE * self.col + SQUARE_SIZE/2))
            self.screen.blit(integer_surf, integer_rect)
            if self.selected == True:
                pygame.draw.rect(self.screen,RED,[SQUARE_SIZE*self.row,SQUARE_SIZE*self.col,SQUARE_SIZE,SQUARE_SIZE],2)
            else:
                pygame.draw.rect(self.screen,LINE_COLOR,[SQUARE_SIZE*self.row,SQUARE_SIZE*self.col,SQUARE_SIZE,SQUARE_SIZE],2)
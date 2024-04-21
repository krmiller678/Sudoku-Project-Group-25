import pygame
from constants import *

class Cell:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def set(self, val):
        self.value = val

    def draw(self, screen):
        chip_font = pygame.font.Font(None, 133)
        chip_x_surf = chip_font.render('1', 0, DEFAULT_NUMBER_COLOR)
        chip_o_surf = chip_font.render('2', 0, INPUT_NUMBER_COLOR)
        if self.value == 'x':
            chip_x_rect = chip_x_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(chip_x_surf, chip_x_rect)
        elif self.value == 'o':
            chip_o_rect = chip_o_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(chip_o_surf, chip_o_rect)

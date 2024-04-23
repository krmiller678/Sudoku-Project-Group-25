"""
Object Oriented pygame event gui - could be updated to break apart the lengthy
functions in future updates
"""
from constants_new import *
import pygame,sys
from cell_new import Cell
from board_new import Board

def startup(screen):
    #setup fonts
    title_font = pygame.font.Font(None,70)

    #fill in background
    screen.fill(BG_COLOR)

    #setup buttons
    easy_text = title_font.render("EASY", 0, (255, 255, 255))
    medium_text = title_font.render("MEDIUM", 0, (255, 255, 255))
    hard_text = title_font.render("HARD", 0, (255, 255, 255))

    #initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 10))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10,10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 10))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10,10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 10))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10,10))

    #initialize button rectangle
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2, 660))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, 440))
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH//2 , 220))
    
    #draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    #set up in game loop to select buttons
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Mouse button handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    #difficulty = 30
                    winner = game_in_progress(screen,1)
                    return winner
                elif medium_rectangle.collidepoint(event.pos):
                    # difficulty = 40
                    winner = game_in_progress(screen,40)
                    return winner
                elif hard_rectangle.collidepoint(event.pos):
                    # difficulty = 50
                    winner = game_in_progress(screen,50)
                    return winner
                
        pygame.display.update()


def game_in_progress(screen,difficulty=30):
    """
    This function takes as inputs the board difficulty as well as the screen surface
    to initialize the starting point for the game. Event loop included at bottom allows 
    player to interact and play game.
    """
    #setup fonts
    button_font = pygame.font.Font(None,40)

    #fill in background
    screen.fill(BG_COLOR)

    #setup buttons
    reset_text = button_font.render("RESET", 0, (255, 255, 255))
    restart_text = button_font.render("RESTART", 0, (255, 255, 255))
    exit_text = button_font.render("EXIT", 0, (255, 255, 255))

    #initialize button background color and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 10))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10,10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 10))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10,10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 10))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10,10))

    #initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 4, 715))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, 715))
    exit_rectangle = exit_surface.get_rect(
        center=(3*WIDTH // 4, 715))
    
    #draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    #draw board
    board = Board(WIDTH, HEIGHT, screen, difficulty)
    board.draw()

    #sets default target
    target = board.select(0,0)
    #set up in game loop to select buttons
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Mouse button handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rectangle.collidepoint(event.pos):
                    #resets board to original state
                    board.reset_to_original()
                elif restart_rectangle.collidepoint(event.pos):
                    # If the mouse button is on restart, return to main menu
                    startup(screen)
                elif exit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the exit button, exit the program
                    sys.exit()
                else:
                    #if clicked on target cell, remove old target
                    target.selected = False
                    target.draw()
                    rowcol = board.click(event.pos[0],event.pos[1])
                    if rowcol != None:
                        target = board.select(rowcol[0],rowcol[1])

            # Key stroke event handler
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    board.sketch(target,1)
                elif event.key == pygame.K_2:
                    board.sketch(target,2)
                elif event.key == pygame.K_3:
                    board.sketch(target,3)
                elif event.key == pygame.K_4:
                    board.sketch(target,4)    
                elif event.key == pygame.K_5:
                    board.sketch(target,5)
                elif event.key == pygame.K_6:
                    board.sketch(target,6)
                elif event.key == pygame.K_7:
                    board.sketch(target,7)
                elif event.key == pygame.K_8:
                    board.sketch(target,8)
                elif event.key == pygame.K_9:
                    board.sketch(target,9)
                elif event.key == pygame.K_RETURN:
                    board.place_number(target,target.sketched_value)
                elif event.key == pygame.K_BACKSPACE:
                    board.clear(target)
            


                    

        board.update_board()
        pygame.display.update()
        if board.is_full():
            winner = board.check_board()
            return winner


def loser(screen):
    #setup fonts
    title_font = pygame.font.Font(None,70)

    #fill in background
    screen.fill(BG_COLOR)

    #setup buttons
    you_lost_text = title_font.render("Game Over :(", 0, (255, 255, 255))
    restart_text = title_font.render("RESTART", 0, (255, 255, 255))
    
    #initialize button background color and text
    you_lost_surface = pygame.Surface((you_lost_text.get_size()[0] + 20, you_lost_text.get_size()[1] + 10))
    you_lost_surface.fill(LINE_COLOR)
    you_lost_surface.blit(you_lost_text, (10,10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 10))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10,10))


    #initialize button rectangle
    you_lost_rectangle = you_lost_surface.get_rect(
        center=(WIDTH // 2, 220))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, 440))
    
    #draw buttons
    screen.blit(you_lost_surface, you_lost_rectangle)
    screen.blit(restart_surface, restart_rectangle)


    #set up in game loop to select buttons
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Mouse button handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                if you_lost_rectangle.collidepoint(event.pos):
                    print("Better luck next time!")
                elif restart_rectangle.collidepoint(event.pos):
                    # If the mouse button is on restart, return to main menu
                    startup(screen)
                
        pygame.display.update()


def chicken_dinner(screen):
    #setup fonts
    title_font = pygame.font.Font(None,70)

    #fill in background
    screen.fill(BG_COLOR)

    #setup buttons
    you_won_text = title_font.render("Game Won!", 0, (255, 255, 255))
    exit_text = title_font.render("EXIT", 0, (255, 255, 255))
    
    #initialize button background color and text
    you_won_surface = pygame.Surface((you_won_text.get_size()[0] + 20, you_won_text.get_size()[1] + 10))
    you_won_surface.fill(LINE_COLOR)
    you_won_surface.blit(you_won_text, (10,10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 10))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10,10))


    #initialize button rectangle
    you_won_rectangle = you_won_surface.get_rect(
        center=(WIDTH // 2, 220))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2, 440))
    
    #draw buttons
    screen.blit(you_won_surface, you_won_rectangle)
    screen.blit(exit_surface, exit_rectangle)


    #set up in game loop to select buttons
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Mouse button handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                if you_won_rectangle.collidepoint(event.pos):
                    print("Great job!")
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()
                
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)
    
    winner = startup(screen)
    if winner == False:
        loser(screen)
    else:
        chicken_dinner(screen)
    



    while True:
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
# Menu.py file contains the functionality to generate the main menu, buttons to call other functions

from stringprep import in_table_b1
import pygame
from GenerateLevel import *


def main_menu(screen):
    game_over = False
    screen.fill((0, 0, 0))
    pygame.display.update()
    button_colour = (0, 128, 0)
    text_colour = (255, 255, 255)
    button_width = 200
    button_height = 50
    button_rect = [(screen.get_width() - button_width)/2, screen.get_height()/2 - button_height/2  - 250, button_width, button_height]
    button_rect2 = [(screen.get_width() - button_width)/2, screen.get_height()/2 - button_height/2 - 150 , button_width, button_height]
    button_rect3 = [(screen.get_width() - button_width)/2, screen.get_height()/2 - button_height/2 - 50 , button_width, button_height]
    button_rect4 = [(screen.get_width() - button_width)/2, screen.get_height()/2 - button_height/2 + 50 , button_width, button_height]
    button_rect5 = [(screen.get_width() - button_width)/2, screen.get_height()/2 - button_height/2 + 150 , button_width, button_height]
    button_font = pygame.font.SysFont('Arial', 24)
    button_text = button_font.render('New Game', True, text_colour)
    button_text2 = button_font.render('Increase Difficulty', True, text_colour)
    button_text3 = button_font.render('Decrease Difficulty', True, text_colour)
    button_text4 = button_font.render('Solve level', True, text_colour)
    button_text5 = button_font.render('Exit', True, text_colour)
    # screen.fill(100, 100, 100)
    pygame.draw.rect(screen, button_colour, button_rect)
    pygame.draw.rect(screen, button_colour, button_rect2)
    pygame.draw.rect(screen, button_colour, button_rect3)
    pygame.draw.rect(screen, button_colour, button_rect4)
    pygame.draw.rect(screen, button_colour, button_rect5)
    screen.blit(button_text, (button_rect[0] + (button_width - button_text.get_width())/2 ,
                              (button_rect[1] + (button_height/2 - button_text.get_height()) / 2 + 10)))
    screen.blit(button_text2, (button_rect2[0] + (button_width - button_text2.get_width()) / 2,
                               (button_rect2[1] + (button_height / 2 - button_text2.get_height()) / 2 + 10)))
    screen.blit(button_text3, (button_rect3[0] + (button_width - button_text3.get_width()) / 2,
                               (button_rect3[1] + (button_height / 2 - button_text3.get_height()) / 2 + 10)))
    screen.blit(button_text4, (button_rect4[0] + (button_width - button_text4.get_width()) / 2,
                               (button_rect4[1] + (button_height / 2 - button_text4.get_height()) / 2 + 10)))
    screen.blit(button_text5, (button_rect5[0] + (button_width - button_text5.get_width()) / 2,
                               (button_rect5[1] + (button_height / 2 - button_text5.get_height()) / 2 + 10)))

    pygame.display.update()

    int_basedifficulty = 2

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill((0, 0, 0))
                pygame.display.update()
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if(button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1] + button_rect[3]):
                    print("start new game")
                    GenerateLevel(int_basedifficulty, screen)
                elif(button_rect2[0] <= x <= button_rect2[0] + button_rect2[2] and button_rect2[1] <= y <= button_rect2[1] + button_rect2[3]):
                    if int_basedifficulty == 5:
                        int_basedifficulty = 5
                    else:
                        int_basedifficulty = int_basedifficulty + 1
                    print("Difficulty increased to: " + str(int_basedifficulty))
                    
                elif (button_rect3[0] <= x <= button_rect3[0] + button_rect3[2] and button_rect3[1] <= y <=
                      button_rect3[1] + button_rect3[3]):
                    if int_basedifficulty == 2:
                        int_basedifficulty = 2
                    else:
                        int_basedifficulty = int_basedifficulty - 1
                    print("Difficulty decrease to: " + str(int_basedifficulty))
                elif (button_rect4[0] <= x <= button_rect4[0] + button_rect4[2] and button_rect4[1] <= y <=
                          button_rect4[1] + button_rect4[3]):
                    print("Solve level")
                elif(button_rect5[0] <= x <= button_rect5[0] + button_rect5[2] and button_rect5[1] <= y <= button_rect5[1] + button_rect5[3]):
                    print("Game over")
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    game_over = True

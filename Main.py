# Main Script


import pygame
#new code below
from itertools import cycle


pygame.init()

#new code below
BLINK_EVENT = pygame.USEREVENT + 0

screen = pygame.display.set_mode((800, 600), 0, 32)

#new code below
screen_rect = screen.get_rect()
clock = pygame.time.Clock()



sprite1 = pygame.image.load('./images/sudokulogo4.png')
spritewidth = sprite1.get_width()
spriteheight = sprite1.get_height()
white = (255, 255, 255)
Font = pygame.font.SysFont('timesnewroman', 62)
text = Font.render('Press any key to continue', True, white)
pygame.display.set_caption("Kaplan Pygame")
screen.fill((0, 0, 0))
# new code below
blink_rect = text.get_rect()
blink_rect.center = screen_rect.center
off_text_surface = pygame.Surface(blink_rect.size)
blink_surfaces = cycle([text, off_text_surface])
blink_surface = next(blink_surfaces)
pygame.time.set_timer(BLINK_EVENT, 1000)


def main_menu():
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
    #button_rect5 = [(screen.get_width() - button_width)/2, screen.get_height()/2 - button_height/2 + 150 , button_width, button_height]
    button_rect6 = [(screen.get_width() - button_width)/2, screen.get_height()/2 - button_height/2 + 150 , button_width, button_height]
    button_font = pygame.font.SysFont('Arial', 24)
    button_text = button_font.render('New Game', True, text_colour)
    button_text2 = button_font.render('Increase Difficulty', True, text_colour)
    button_text3 = button_font.render('Decrease Difficulty', True, text_colour)
    button_text4 = button_font.render('Analysis', True, text_colour)
    #button_text5 = button_font.render('Solve level', True, text_colour)
    button_text6 = button_font.render('Exit', True, text_colour)
    # screen.fill(100, 100, 100)
    pygame.draw.rect(screen, button_colour, button_rect)
    pygame.draw.rect(screen, button_colour, button_rect2)
    pygame.draw.rect(screen, button_colour, button_rect3)
    pygame.draw.rect(screen, button_colour, button_rect4)
    #pygame.draw.rect(screen, button_colour, button_rect5)
    pygame.draw.rect(screen, button_colour, button_rect6)
    screen.blit(button_text, (button_rect[0] + (button_width - button_text.get_width())/2 ,
                              (button_rect[1] + (button_height/2 - button_text.get_height()) / 2 + 10)))
    screen.blit(button_text2, (button_rect2[0] + (button_width - button_text2.get_width()) / 2,
                               (button_rect2[1] + (button_height / 2 - button_text2.get_height()) / 2 + 10)))
    screen.blit(button_text3, (button_rect3[0] + (button_width - button_text3.get_width()) / 2,
                               (button_rect3[1] + (button_height / 2 - button_text3.get_height()) / 2 + 10)))
    screen.blit(button_text4, (button_rect4[0] + (button_width - button_text4.get_width()) / 2,
                               (button_rect4[1] + (button_height / 2 - button_text4.get_height()) / 2 + 10)))
    #screen.blit(button_text5, (button_rect5[0] + (button_width - button_text5.get_width()) / 2,
                               #(button_rect5[1] + (button_height / 2 - button_text5.get_height()) / 2 + 10)))
    screen.blit(button_text6, (button_rect6[0] + (button_width - button_text6.get_width()) / 2,
                               (button_rect6[1] + (button_height / 2 - button_text6.get_height()) / 2 + 10)))

    pygame.display.update()

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
                elif(button_rect2[0] <= x <= button_rect2[0] + button_rect2[2] and button_rect2[1] <= y <= button_rect2[1] + button_rect2[3]):
                    print("increase difficulty")
                elif (button_rect3[0] <= x <= button_rect3[0] + button_rect3[2] and button_rect3[1] <= y <=
                      button_rect3[1] + button_rect3[3]):
                    print("decrease difficulty")
                elif (button_rect4[0] <= x <= button_rect4[0] + button_rect4[2] and button_rect4[1] <= y <=
                          button_rect4[1] + button_rect4[3]):
                    print("Analysis")
                #elif (button_rect5[0] <= x <= button_rect5[0] + button_rect5[2] and button_rect5[1] <= y <=
                          #button_rect5[1] + button_rect5[3]):
                    #print("Solve level")
                elif(button_rect6[0] <= x <= button_rect6[0] + button_rect6[2] and button_rect6[1] <= y <= button_rect6[1] + button_rect6[3]):
                    print("Game over")
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    game_over = True
                    exit()



game_over = False
while not game_over:
    screen.blit(sprite1, (screen.get_width() / 2 - spritewidth / 2, screen.get_height() / 2 - spriteheight / 2))
    #screen.blit(text, (0+ 100,screen.get_height()/2 + 150))

    #new code below
    screen.blit(blink_surface, (0+ 100,screen.get_height()/2 + 150))
    pygame.display.update()
    clock.tick(60)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        pressed = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            print("a key has been pressed")
            main_menu()
            # continue to main page
        if event.type == BLINK_EVENT:
            blink_surface = next(blink_surfaces)




pygame.quit()

# Call LoadMainMenu()




# Call GenerateLevel(difficulty)

# Call LoadAnalysis()


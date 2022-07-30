import pygame
from Menu import *
from itertools import cycle


pygame.init()

#new code below
BLINK_EVENT = pygame.USEREVENT + 0

screen = pygame.display.set_mode((750, 750), 0, 32)

# Main.py is the default file that will be executed
# Main file will contain first iteration of any screen creation


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
            main_menu(screen)
            # continue to main page
        if event.type == BLINK_EVENT:
            blink_surface = next(blink_surfaces)

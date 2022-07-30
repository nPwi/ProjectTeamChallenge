# GenerateLevel.py takes in a difficulty level and generate a game

from random import sample
import pygame

# Setting the display Width(left) and Height(right)
# screen = pygame.display.set_mode((750, 750))

# Setting the name of the program
pygame.display.set_caption("SUDOKU GAME FOR KAPLAN")
pygame.font.init()
# Initialize variables



def GenerateLevel(int_difficultyLevel, screen):

    int_x = 0
    int_z = 0
    int_sizeOfGame = 650
    int_value = 0
    int_rangeNumber = 0
    int_lineNumber = 0
    int_base = 0
    int_side = 0
    int_diff = 0
    font = pygame.font.SysFont("comicsans", 20)


    # define per side value
    int_rangeNumber = int_difficultyLevel * int_difficultyLevel
    int_lineNumber = int_rangeNumber+1
    int_diff = int_sizeOfGame / int_rangeNumber
    int_base = int_difficultyLevel
    int_side = int_base*int_base

    # inner pattern function
    def pattern(r, c): return (int_base*(r % int_base)+r//int_base+c) % int_side

    # inner shuffle function
    def shuffle(s): return sample(s, len(s))

    rint_Base = range(int_base)

    int_rows = [g*int_base +
                r for g in shuffle(rint_Base) for r in shuffle(rint_Base)]

    int_cols = [g*int_base +
                c for g in shuffle(rint_Base) for c in shuffle(rint_Base)]
    nums = shuffle(range(1, int_base*int_base+1))

    # produce board using randomized int_baseline pattern
    defaultgrid = [[nums[pattern(r, c)] for c in int_cols] for r in int_rows]

    squares = int_side*int_side
    empties = squares * 3//4

    for p in sample(range(squares), empties):
        defaultgrid[p//int_side][p % int_side] = 0

    # Inner cord function
    def cord(pos):
        global int_x
        int_x = pos[0]//int_diff
        global int_z
        int_z = pos[1]//int_diff

    # Inner function for grid selection highlights
    def highlightboint_x():
        for k in range(2):
            pygame.draw.line(screen, (0, 0, 0), (int_x * int_diff-3, (int_z + k)
                             * int_diff), (int_x * int_diff + int_diff + 3, (int_z + k)*int_diff), 7)
            pygame.draw.line(screen, (0, 0, 0), ((int_x + k) * int_diff,
                             int_z * int_diff), ((int_x + k) * int_diff, int_z * int_diff + int_diff), 7)

    # Inner function for graphical lines
    def drawlines():
        for i in range(int_rangeNumber):
            for j in range(int_rangeNumber):
                if defaultgrid[i][j] != 0:
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (i * int_diff, j * int_diff, int_diff + 1, int_diff + 1))
                    teint_xt1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                    screen.blit(
                        teint_xt1, (i * int_diff + 15, j * int_diff + 15))
        for l in range(int_lineNumber):
            if l % int_base == 0:
                thick = 7
            else:
                thick = 1
            # Drawing of lines
            # Line(surface, colour, starting point, ending point, thickness)
            # Surface refers to the display that is to be drawn on
            # colour is RGB, each to a maint_ximum of 255
            # starting point is (int_x,y) whr int_x is horizontal aint_xis, y is vertical aint_xis
            # ending point is the same as starting point (int_x,y)
            pygame.draw.line(screen, (0, 0, 0), (0, l * int_diff),
                             (int_sizeOfGame, l * int_diff), thick)
            pygame.draw.line(screen, (0, 0, 0), (l * int_diff, 0),
                             (l * int_diff, int_sizeOfGame), thick)

    def fillvalue(int_value):
        text1 = font.render(str(int_value), 1, (0, 0, 0))
        screen.blit(
            text1, (int_x * int_diff + 15, int_z * int_diff + 15))


    def raiseerror():
        text1 = font.render("wrong!", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))


    def raiseerror1():
        text1 = font.render(
            "wrong ! enter a valid key for the game", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))


    def validvalue(m, k, l, int_value):
        for it in range(int_rangeNumber):
            if m[k][it] == int_value:
                return False
            if m[it][l] == int_value:
                return False
        it = k//int_base
        jt = l//int_base
        for k in range(it * int_base, it * int_base + int_base):
            for l in range(jt * int_base, jt * int_base + int_base):
                if m[k][l] == int_value:
                    return False
        return True

    # inner function 
    def solvegame(defaultgrid, i, j):

        while defaultgrid[i][j] != 0:
            if i < int_rangeNumber-1:
                i += 1
            elif i == int_rangeNumber-1 and j < int_rangeNumber-1:
                i = 0
                j += 1
            elif i == int_rangeNumber-1 and j == int_rangeNumber-1:
                return True
        pygame.event.pump()
        for it in range(1, int_rangeNumber+1):
            if validvalue(defaultgrid, i, j, it) == True:
                defaultgrid[i][j] = it
                global int_x, int_z
                int_x = i
                int_z = j
                drawlines()
                highlightboint_x()
                pygame.display.update()
                pygame.time.delay(20)
                if solvegame(defaultgrid, i, j) == 1:
                    return True
                else:
                    defaultgrid[i][j] = 0

                drawlines()
                highlightboint_x()
                pygame.display.update()
                pygame.time.delay(50)
        return False


    def gameresult():
        teint_xt1 = font.render("game finished", 1, (0, 0, 0))
        screen.blit(teint_xt1, (20, int_sizeOfGame+50))

    int_flag = True
    int_flag1 = 0
    int_flag2 = 0
    rs = 0
    error = 0

    while int_flag:
        screen.fill((0, 182, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                int_flag = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                int_flag1 = 1
                pos = pygame.mouse.get_pos()
                cord(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    int_x -= 1
                    int_flag1 = 1
                if event.key == pygame.K_RIGHT:
                    int_x += 1
                    int_flag1 = 1
                if event.key == pygame.K_UP:
                    int_z -= 1
                    int_flag1 = 1
                if event.key == pygame.K_DOWN:
                    int_z += 1
                    int_flag1 = 1
                if event.key == pygame.K_1:
                    int_value = 1
                if event.key == pygame.K_2:
                    int_value = 2
                if event.key == pygame.K_3:
                    int_value = 3
                if event.key == pygame.K_4:
                    int_value = 4
                if event.key == pygame.K_5:
                    int_value = 5
                if event.key == pygame.K_6:
                    int_value = 6
                if event.key == pygame.K_7:
                    int_value = 7
                if event.key == pygame.K_8:
                    int_value = 8
                if event.key == pygame.K_9:
                    int_value = 9
                if event.key == pygame.K_RETURN:
                    int_flag2 = 1
                if event.key == pygame.K_r:
                    rs = 0
                    error = 0
                    int_flag2 = 0
                    defaultgrid = [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
                if event.key == pygame.K_d:
                    rs = 0
                    error = 0
                    int_flag2 = 0
                    defaultgrid = [[nums[pattern(r, c)]
                                    for c in int_cols] for r in int_rows]
                    for p in sample(range(squares), empties):
                        defaultgrid[p//int_side][p % int_side] = 0

        if int_flag2 == 1:
            if solvegame(defaultgrid, 0, 0) == False:
                error = 1
            else:
                rs = 1
            int_flag2 = 0
        if int_value != 0:
            fillvalue(int_value)
            if validvalue(defaultgrid, int(int_x), int(int_z), int_value) == True:
                defaultgrid[int(int_x)][int(int_z)] = int_value
                int_flag1 = 0
            else:
                defaultgrid[int(int_x)][int(int_z)] = 0
                raiseerror1()
            int_value = 0

        if error == 1:
            raiseerror()
        if rs == 1:
            gameresult()
        drawlines()
        if int_flag1 == 1:
            highlightboint_x()
        pygame.display.update()
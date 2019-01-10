import pygame
import random

random.seed()
pygame.init()

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
class Pole:
    def __init__(self, color, empty):
        self.empty = empty
        self.color = color

def blockRainfall():
    while True:
        tab = figure(random.randint(0, len(figures) - 1))
        printBlock(random.randint(0, len(blockColors) - 1))

def figure(n):
        tab = [Point() for i in range(4)]
        for i in range(4):
            tab[i].x = figures[n][i] % 2
            tab[i].y = figures[n][i] // 2
        return tab

def printAll():
    for x in range(M):
        for y in range(N):
            if blocksTab[y][x].empty == True:
                pygame.Surface.blit(gameDisplay, blockColors[blocksTab[y][x].color], (x * block_size, y * block_size))

def printBlock(color, tab):
    for i in range(4):
        pygame.Surface.blit(gameDisplay, blockColors[color], (tab[i].x * block_size, tab[i].y * block_size))

def rotate(isEnd):
        if isEnd:
            point = Point(tab[1].x, tab[1].y)
            tmp = [Point() for i in range(4)]
            check_x = True
            check_y = True
            for i in range(4):
                x = tab[i].y - point.y
                y = tab[i].x - point.x
                tmp[i].x = point.x - x
                tmp[i].y = point.y + y
                if tmp[i].x < 0 or tmp[i].x > 10:
                    check_x = False
                if tmp[i].y > 22:
                    check_y = False
            if check_x and check_y:
                for i in range(4):
                    tab[i].x = tmp[i].x
                    tab[i].y = tmp[i].y

def move(xmv, ymv, isEnd):
    if isEnd:
        check_x = True
        check_y = True
        for i in range(4):
            if tab[i].x + xmv < 0 or tab[i].x + xmv > 10:
                check_x = False
            if tab[i].y + ymv > 20:
                check_y = False
        if check_x or check_y:
            for i in range(4):
                if check_x:
                    tab[i].x += xmv
                if check_y:
                    tab[i].y += ymv

def checkHeight():
    check = True
    for i in range(4):
        if tab[i].y + 1 > 20:
            check = False
    return check

# Config
block_size = 30
display_width = 500
display_height = 700
board_width = 300
board_height = 600
M = 20
N = 10

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

bc_yellow = pygame.transform.scale(pygame.image.load('yellow.bmp'), (block_size, block_size))
bc_blue = pygame.transform.scale(pygame.image.load('blue.bmp'), (block_size, block_size))
bc_azure = pygame.transform.scale(pygame.image.load('azure.bmp'), (block_size, block_size))
bc_green = pygame.transform.scale(pygame.image.load('green.bmp'), (block_size, block_size))
bc_red = pygame.transform.scale(pygame.image.load('red.bmp'), (block_size, block_size))
bc_violet = pygame.transform.scale(pygame.image.load('violet.bmp'), (block_size, block_size))
bc_orange = pygame.transform.scale(pygame.image.load('orange.bmp'), (block_size, block_size))

blockColors = [bc_yellow, bc_blue, bc_azure, bc_green, bc_red, bc_violet, bc_orange]

blocksTab = [[Pole(0,False) for col in range(N+1)] for row in range(M+1)]
figures = [[1, 3, 5, 7], [2, 4, 5, 7], [3, 5, 4, 6], [3, 5, 4, 7], [2, 3, 5, 7], [3, 2, 4, 6], [2, 3, 4, 5]]
tab = figure(5)
pos_x = (display_width - block_size) / 2
pos_y = 0
max_x = board_width
max_y = board_height

# Initialization

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.SRCALPHA)
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()
fps = 5
tick = 0
isEnd = True
color = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_UP:
                rotate(isEnd)

    clock.tick(fps)
    xmv = 0
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if True:
            xmv = 1
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if True:
            xmv = -1
    tick += 1
    ymv = 0
    if tick % (fps // 2) == 0: ymv = 1
    if xmv != 0 or ymv != 0:  move(xmv, ymv, isEnd)
    isEnd = checkHeight()

    gameDisplay.fill((0,20,40))
    printBlock(color,tab)
    for i in range(4):
        print(tab[i].x, tab[i].y)
    if not isEnd:
        for i in range(4):
            blocksTab[tab[i].y][tab[i].x].empty = True
            blocksTab[tab[i].y][tab[i].x].color = color
        tab = figure(random.randint(0, len(figures) - 1))
        color = random.randint(0, len(blockColors) - 1)
    printAll()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()

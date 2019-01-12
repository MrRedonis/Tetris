import pygame
import random

random.seed()
pygame.init()


class Point: # Struktrua do tab[]
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Pole: # Struktura do blocksTab
    def __init__(self, color, empty):
        self.empty = empty
        self.color = color

def color_gen(last): # Generator liczb odpowiadajacych kolorom z pominieciem ostatniego.
    col = random.randint(0, len(blockColors) - 1)
    while last == col:
        col = random.randint(0, len(blockColors) - 1)
    return col

def figure(n=-1): # Generator figur
    if n == -1:
        n = random.randint(0, len(figures) - 1)
    tab = [Point() for i in range(4)]
    for i in range(4):
        tab[i].x = figures[n][i] % 2 + 5
        tab[i].y = figures[n][i] // 2
    return tab

def print_all(): # Funkja rysuje już postawione bloki, które są zapisane w blockColors.
    for y in range(M):
        for x in range(N):
            if blocksTab[y][x].empty is True:
                pygame.Surface.blit(gameDisplay, blockColors[blocksTab[y][x].color], (pos_x + x * block_size, pos_y + y * block_size))

def print_block(color): # Funkcja rysuje całą figurę wg wzoru w tab[].
    for i in range(4):
        pygame.Surface.blit(gameDisplay, blockColors[color], (pos_x + tab[i].x * block_size, pos_y + tab[i].y * block_size))

def rotate(isEnd): # Funkcja obraca blok jeśli isEnd == True.
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
                if tmp[i].x < 0 or tmp[i].x > N:
                    check_x = False
                if tmp[i].y > M-1:
                    check_y = False
            if check_x and check_y:
                for i in range(4):
                    tab[i].x = tmp[i].x
                    tab[i].y = tmp[i].y

def move(xmv, ymv, isEnd): # Funkcja sprawdza czy porusza się w siatce gry i porusza blokiem.
    if isEnd:
        check_x = True
        check_y = True
        for i in range(4):
            if tab[i].x + xmv < 0 or tab[i].x + xmv > N-1:
                check_x = False
            if tab[i].y + ymv > M-1:
                check_y = False
        if check_x or check_y:
            for i in range(4):
                if check_x and checkSites():
                    tab[i].x += xmv
                if check_y:
                    tab[i].y += ymv

def check_height(): # Funkcja sprawdza czy blok "dotkął podłogi/ bloku" pod sobą. Jeśli tak to zwraca False, w przeciwnym wypadku True.
    check = True
    for i in range(4):
        if tab[i].y + 1 > M-1:
            check = False
        elif blocksTab[tab[i].y+1][tab[i].x].empty:
            check = False
    return check

def checkSites(): # Funkcja sprawdza czy możliwe jest przemieszczenie w poziomie. Jeśli tak zwraca True, w przeciwnym wypadku False.
    check = True
    for i in range(4):
        x_min = tab[i].x - 1
        x_max = tab[i].x + 1
        if x_min >= 0:
            if blocksTab[tab[i].y][tab[i].x - 1].empty:
                check = False
        if x_max < N:
            if blocksTab[tab[i].y][tab[i].x + 1].empty:
                check = False
    return check

def delete_line(): # Funkcja usuwa wiersze w pełni zapełnione
    for y in range(M):
        counter = 0
        for x in range(N):
            if blocksTab[y][x].empty:
                counter += 1
        if counter == N:
            for line in range(y-1, -1, -1):
                for x in range(0, N):
                    blocksTab[line + 1][x].empty = blocksTab[line][x].empty
                    blocksTab[line + 1][x].color = blocksTab[line][x].color

def view_background():
    gameDisplay.fill((251, 101, 190))
    pygame.draw.rect(gameDisplay, (98, 98, 98), (pos_x - 5, pos_y - 5, board_width + 10, board_height + 10))
    pygame.draw.rect(gameDisplay, black, (pos_x, pos_y, board_width, board_height))
    pygame.Surface.blit(gameDisplay, grid, (pos_x, pos_y))


# Config
M = 20
N = 10
block_size = 30
display_width = 900
display_height = 700
board_width = N * block_size
board_height = M * block_size
pos_x = (display_width - board_width) // 2
pos_y = 50

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Obrazy i zdjęcia
bc_yellow = pygame.transform.scale(pygame.image.load('yellow.bmp'), (block_size, block_size))
bc_blue = pygame.transform.scale(pygame.image.load('blue.bmp'), (block_size, block_size))
bc_azure = pygame.transform.scale(pygame.image.load('azure.bmp'), (block_size, block_size))
bc_green = pygame.transform.scale(pygame.image.load('green.bmp'), (block_size, block_size))
bc_red = pygame.transform.scale(pygame.image.load('red.bmp'), (block_size, block_size))
bc_violet = pygame.transform.scale(pygame.image.load('violet.bmp'), (block_size, block_size))
bc_orange = pygame.transform.scale(pygame.image.load('orange.bmp'), (block_size, block_size))
grid = pygame.image.load('grid.bmp')
panel = pygame.image.load('panel.bmp')

blockColors = [bc_yellow, bc_blue, bc_azure, bc_green, bc_red, bc_violet, bc_orange]

blocksTab = [[Pole(0, False) for col in range(N)] for row in range(M)]
figures = [[1, 3, 5, 7], [2, 4, 5, 7], [3, 5, 4, 6], [3, 5, 4, 7], [2, 3, 5, 7], [3, 2, 4, 6], [2, 3, 4, 5]]
tab = figure()

# Initialization
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.SRCALPHA)
pygame.display.set_caption('Tetris')
pygame.display.set_icon(bc_yellow)
clock = pygame.time.Clock()
fps = 8
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
    ymv = 0
    speed = fps // 2
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
            xmv = 1
    if pygame.key.get_pressed()[pygame.K_LEFT]:
            xmv = -1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
            speed -= 3

    tick += 1
    if tick % (speed) == 0: ymv = 1
    if xmv != 0 or ymv != 0:
        move(xmv, ymv, isEnd)
    isEnd = check_height()

    view_background()
    print_block(color)

    if not isEnd:
        for i in range(4):
            blocksTab[tab[i].y][tab[i].x].empty = True
            blocksTab[tab[i].y][tab[i].x].color = color
        tab = figure()
        color = color_gen(color)
    delete_line()
    print_all()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()

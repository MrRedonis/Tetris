import pygame
import random

pygame.init()

class Point: # Struktrua do tab[]
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Pole: # Struktura do blocksTab
    def __init__(self, color, empty):
        self.empty = empty
        self.color = color

class Menu:
    def __init__(self):
        self.open_function = 0
        self.engine()

    def main_menu(self):
        self.background()
        for x in range(5):
            x_pos = pos_x + 50
            y_pos = pos_y + 150 + 80 * x
            if self.mouse_contained(x_pos, y_pos, x_pos + button_w, y_pos + button_h):
                gameDisplay.blit(button_1, (x_pos, y_pos))
                if pygame.mouse.get_pressed() == (1,0,0):
                    self.open_function = x + 1
            else:
                gameDisplay.blit(button_2, (x_pos, y_pos))
            text = font.render(menu_texts[x], True, white)
            gameDisplay.blit(text, (x_pos + (button_w - text.get_width()) // 2, y_pos))
        print(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        pygame.display.update()

    def mouse_contained(self, x1, y1, x2, y2):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if x >= x1 and x<= x2:
            if y >= y1 and y <= y2:
                return True
            else:
                return False
        else:
            return False

    def engine(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            if self.open_function == 0:
                self.main_menu()
            elif self.open_function == 1:
                self.play()
            elif self.open_function == 2:
                self.high_scores_menu()
            elif self.open_function == 3:
                self.options_menu()
            elif self.open_function == 4:
                self.about()
            elif self.open_function == 5:
                self.quit_menu()

        pygame.quit()
        quit()

    def play(self):
        Game()
        pass

    def high_scores_menu(self):
        pass

    def options_menu(self):
        pass

    def about(self):
        self.background()
        x_pos = pos_x + 50
        y_pos = pos_y + 50
        if self.mouse_contained(x_pos, y_pos, x_pos + button_w, y_pos + button_h):
            gameDisplay.blit(button_1, (x_pos, y_pos))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.open_function = 0
        else:
            gameDisplay.blit(button_2, (x_pos, y_pos))
        text = font.render('Back', True, white)
        gameDisplay.blit(text, (x_pos + (button_w - text.get_width()) // 2, y_pos))
        length = 0
        height = 0
        to_print = about_text.split(" ")
        for i in range(len(to_print)):
            text = menu_font.render(to_print[i]+" ", True, white)
            if pos_x + 20 + length > pos_x + board_width - 70:
                height += 1
                length = 0
            gameDisplay.blit(text, (pos_x + 20 + length, y_pos + 100 + 30 * height))
            length += text.get_width()

            print(length, height)
        pygame.display.update()
        pass

    def quit_menu(self):
        pygame.quit()
        quit(0)

    def background(self):
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(menu_panel, (pos_x, pos_y))


class Game:
    def __init__(self):
        self.bc_blue = pygame.transform.scale(pygame.image.load('blue.bmp'), (block_size, block_size))
        self.bc_azure = pygame.transform.scale(pygame.image.load('azure.bmp'), (block_size, block_size))
        self.bc_green = pygame.transform.scale(pygame.image.load('green.bmp'), (block_size, block_size))
        self.bc_red = pygame.transform.scale(pygame.image.load('red.bmp'), (block_size, block_size))
        self.bc_violet = pygame.transform.scale(pygame.image.load('violet.bmp'), (block_size, block_size))
        self.bc_orange = pygame.transform.scale(pygame.image.load('orange.bmp'), (block_size, block_size))
        self.grid = pygame.image.load('grid.bmp')
        self.panel = pygame.image.load('panel.bmp')

        self.blockColors = [bc_yellow, self.bc_blue, self.bc_azure, self.bc_green, self.bc_red, self.bc_violet, self.bc_orange]
        self.blocksTab = [[Pole(0, False) for col in range(N)] for row in range(M)]
        self.figures = [[1, 3, 5, 7], [2, 4, 5, 7], [3, 5, 4, 6], [3, 5, 4, 7], [2, 3, 5, 7], [3, 2, 4, 6], [2, 3, 4, 5]]
        self.tab = self.figure()
        self.clock = pygame.time.Clock()
        self.fps = 8
        self.tick = 0
        self.isEnd = True
        self.color = 1

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
                        self.rotate(self.isEnd)

            self.clock.tick(self.fps)
            xmv = 0
            ymv = 0
            speed = self.fps // 2
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                xmv = 1
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                xmv = -1
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                speed -= 3

            self.tick += 1
            if self.tick % (speed) == 0: ymv = 1
            if xmv != 0 or ymv != 0:
                self.move(xmv, ymv, self.isEnd)
            self.isEnd = self.check_height()

            self.view_background()
            self.print_block(self.color)

            if not self.isEnd:
                for i in range(4):
                    self.blocksTab[self.tab[i].y][self.tab[i].x].empty = True
                    self.blocksTab[self.tab[i].y][self.tab[i].x].color = self.color
                self.tab = self.figure()
                self.color = self.color_gen(self.color)

            self.delete_line()
            self.print_all()

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        quit()

    def color_gen(self, last):  # Generator liczb odpowiadajacych kolorom z pominieciem ostatniego.
        col = random.randint(0, len(self.blockColors) - 1)
        while last == col:
            col = random.randint(0, len(self.blockColors) - 1)
        return col

    def figure(self, n=-1):  # Generator figur
        if n == -1:
            n = random.randint(0, len(self.figures) - 1)
        tab = [Point() for i in range(4)]
        for i in range(4):
            tab[i].x = self.figures[n][i] % 2 + 5
            tab[i].y = self.figures[n][i] // 2
        return tab

    def print_all(self):  # Funkja rysuje już postawione bloki, które są zapisane w blockColors.
        for y in range(M):
            for x in range(N):
                if self.blocksTab[y][x].empty is True:
                    pygame.Surface.blit(gameDisplay, self.blockColors[self.blocksTab[y][x].color],
                                        (pos_x + x * block_size, pos_y + y * block_size))

    def print_block(self, color):  # Funkcja rysuje całą figurę wg wzoru w tab[].
        for i in range(4):
            pygame.Surface.blit(gameDisplay, self.blockColors[color],
                                (pos_x + self.tab[i].x * block_size, pos_y + self.tab[i].y * block_size))

    def rotate(self, isEnd):  # Funkcja obraca blok jeśli isEnd == True.
        if isEnd:
            point = Point(self.tab[1].x, self.tab[1].y)
            tmp = [Point() for i in range(4)]
            check_x = True
            check_y = True
            for i in range(4):
                x = self.tab[i].y - point.y
                y = self.tab[i].x - point.x
                tmp[i].x = point.x - x
                tmp[i].y = point.y + y
                if tmp[i].x < 0 or tmp[i].x > N:
                    check_x = False
                if tmp[i].y > M - 1:
                    check_y = False
            if check_x and check_y:
                for i in range(4):
                    self.tab[i].x = tmp[i].x
                    self.tab[i].y = tmp[i].y

    def move(self, xmv, ymv, isEnd):  # Funkcja sprawdza czy porusza się w siatce gry i porusza blokiem.
        if isEnd:
            check_x = True
            check_y = True
            for i in range(4):
                if self.tab[i].x + xmv < 0 or self.tab[i].x + xmv > N - 1:
                    check_x = False
                if self.tab[i].y + ymv > M - 1:
                    check_y = False
            if check_x or check_y:
                for i in range(4):
                    if check_x and self.check_sites():
                        self.tab[i].x += xmv
                    if check_y:
                        self.tab[i].y += ymv

    def check_height(self):  # Funkcja sprawdza czy blok "dotkął podłogi/ bloku" pod sobą. Jeśli tak to zwraca False, w przeciwnym wypadku True.
        check = True
        for i in range(4):
            if self.tab[i].y + 1 > M - 1:
                check = False
            elif self.tab[i].x > N - 1 or self.blocksTab[self.tab[i].y + 1][self.tab[i].x].empty:
                check = False
        return check

    def check_sites(self):  # Funkcja sprawdza czy możliwe jest przemieszczenie w poziomie. Jeśli tak zwraca True, w przeciwnym wypadku False.
        check = True
        for i in range(4):
            x_min = self.tab[i].x - 1
            x_max = self.tab[i].x + 1
            if x_min >= 0:
                if self.blocksTab[self.tab[i].y][self.tab[i].x - 1].empty:
                    check = False
            if x_max < N:
                if self.blocksTab[self.tab[i].y][self.tab[i].x + 1].empty:
                    check = False
        return check

    def delete_line(self):  # Funkcja usuwa wiersze w pełni zapełnione
        for y in range(M):
            counter = 0
            for x in range(N):
                if self.blocksTab[y][x].empty:
                    counter += 1
            if counter == N:
                for line in range(y - 1, -1, -1):
                    for x in range(0, N):
                        self.blocksTab[line + 1][x].empty = self.blocksTab[line][x].empty
                        self.blocksTab[line + 1][x].color = self.blocksTab[line][x].color

    def view_background(self):
        gameDisplay.blit(background, (0, 0))
        pygame.draw.rect(gameDisplay, (98, 98, 98), (pos_x - 5, pos_y - 5, board_width + 10, board_height + 10))
        pygame.draw.rect(gameDisplay, (45, 53, 73), (pos_x, pos_y, board_width, board_height))
        pygame.Surface.blit(gameDisplay, self.grid, (pos_x, pos_y))

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

button_w = 200
button_h = 50

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

font = pygame.font.SysFont("comicsansms", 30)
menu_font = pygame.font.SysFont("comicsansms", 20)
menu_texts = ["Play", "High Scores", "Options", "About", "Quit"]
about_text = "Game crated by Damian Jurkiewicz (MrRedonis). Main menu background graphic created by Freepic."

# Obrazy i zdjęcia
bc_yellow = pygame.transform.scale(pygame.image.load('yellow.bmp'), (block_size, block_size))
background = pygame.transform.scale(pygame.image.load('tło.bmp'), (display_width, display_height))
menu_panel = pygame.transform.scale(pygame.image.load('test.bmp'), (300, 600))
button_1 = pygame.transform.scale(pygame.image.load('button.bmp'), (button_w, button_h))
button_2 = pygame.transform.scale(pygame.image.load('button2.bmp'), (button_w, button_h))

# Initialization
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.SRCALPHA)
pygame.display.set_caption('Tetris')
pygame.display.set_icon(bc_yellow)

if __name__ == "__main__":
    Menu()
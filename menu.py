import pygame
import random

pygame.init()

class Point: # Struktrua do tab[]
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.name = 0

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
            if self.mouse_contained(x_pos, y_pos, x_pos + menu_button_w, y_pos + menu_button_h):
                gameDisplay.blit(button_1, (x_pos, y_pos))
                if pygame.mouse.get_pressed() == (1,0,0):
                    self.open_function = x + 1
            else:
                gameDisplay.blit(button_2, (x_pos, y_pos))
            text = font.render(menu_texts[x], True, white)
            gameDisplay.blit(text, (x_pos + (menu_button_w - text.get_width()) // 2, y_pos))
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
                Game(self)
                self.open_function = 0
            elif self.open_function == 2:
                self.high_scores_menu()
            elif self.open_function == 3:
                self.options_menu()
            elif self.open_function == 4:
                self.about()
            elif self.open_function == 5:
                self.quit_menu()

    def high_scores_menu(self):
        self.background()
        self.return_button()
        pygame.display.update()
        pass

    def options_menu(self):
        self.background()
        self.return_button()
        pygame.display.update()
        pass

    def about(self):
        x_pos = pos_x + 50
        y_pos = pos_y + 50
        self.background()
        self.return_button()
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
        pygame.display.update()

    def quit_menu(self):
        pygame.quit()
        quit(0)

    def background(self):
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(menu_panel, (pos_x, pos_y))
        font = pygame.font.SysFont("comicsansms", 60)
        text = font.render('Tetris', True, white)
        gameDisplay.blit(text, (pos_x + (board_width - text.get_width()) // 2, pos_y + 30))

    def return_button(self):
        x_pos = pos_x + 50
        y_pos = pos_y + 50
        if self.mouse_contained(x_pos, y_pos, x_pos + menu_button_w, y_pos + menu_button_h):
            gameDisplay.blit(button_1, (x_pos, y_pos))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.open_function = 0
        else:
            gameDisplay.blit(button_2, (x_pos, y_pos))
        text = font.render('Return', True, white)
        gameDisplay.blit(text, (x_pos + (menu_button_w - text.get_width()) // 2, y_pos))


class Game:
    def __init__(self, menu):
        self.Menu = menu
        self.bc_blue = pygame.transform.scale(pygame.image.load('blue.bmp'), (block_size, block_size))
        self.bc_azure = pygame.transform.scale(pygame.image.load('azure.bmp'), (block_size, block_size))
        self.bc_green = pygame.transform.scale(pygame.image.load('green.bmp'), (block_size, block_size))
        self.bc_red = pygame.transform.scale(pygame.image.load('red.bmp'), (block_size, block_size))
        self.bc_violet = pygame.transform.scale(pygame.image.load('violet.bmp'), (block_size, block_size))
        self.bc_orange = pygame.transform.scale(pygame.image.load('orange.bmp'), (block_size, block_size))
        self.grid = pygame.image.load('grid.bmp')

        self.blockColors = [bc_yellow, self.bc_blue, self.bc_azure, self.bc_green, self.bc_red, self.bc_violet, self.bc_orange]
        self.blocksTab = [[Pole(0, False) for col in range(N)] for row in range(M)]
        self.figures = [[1, 3, 5, 7], [2, 4, 5, 7], [3, 5, 4, 6], [3, 5, 4, 7], [2, 3, 5, 7], [3, 2, 4, 6], [2, 3, 4, 5]]
        self.tab = self.figure()
        self.clock = pygame.time.Clock()
        self.fps = 10
        self.tick = 0
        self.isEnd = True
        self.color = 1
        self.points = 0
        self.paused = False
        self.stop = False

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
                        self.tab = self.rotate(self.isEnd, self.tab)

            self.clock.tick(self.fps)
            xmv = 0
            ymv = 0
            speed = self.fps
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                xmv = 1
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                xmv = -1
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                speed -= self.fps + 1

            self.tick += 1
            if self.tick % (speed) == 0:
                ymv = 1
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.points += 1
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
            if self.check_gameover():
                pygame.image.save(gameDisplay, 'surface.bmp')
                gameDisplay.blit(pygame.image.load('surface.bmp'), (0, 0))
                pygame.display.update()
                pygame.time.wait(2000)
                return
            self.pause_button(800, 600)
            self.stop_button(720, 600)
            if self.stop is True: return
            pygame.display.update()
            self.clock.tick(60)
            print(self.points)
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
            tab[i].x = self.figures[n][i] % 2 + 4
            tab[i].y = self.figures[n][i] // 2 - 1
        tab[0].name = n
        tab = self.rotate(True, tab)
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

    def rotate(self, isEnd, tab):  # Funkcja obraca blok jeśli isEnd == True.
        if isEnd:
            if tab[0].name == 6:
                return tab
            point = Point(tab[1].x, tab[1].y)
            tmp = [Point() for i in range(4)]
            check_x = True
            check_y = True
            for i in range(4):
                x = tab[i].y - point.y
                y = tab[i].x - point.x
                tmp[i].x = point.x - x
                tmp[i].y = point.y + y
                if tmp[i].x < 0 or tmp[i].x > N - 1:
                    check_x = False
                if tmp[i].y > M - 1:
                    check_y = False
            if check_x and check_y:
                for i in range(4):
                    tab[i].x = tmp[i].x
                    tab[i].y = tmp[i].y
        return tab

    def move(self, xmv, ymv, isEnd):  # Funkcja sprawdza czy porusza się w siatce gry i porusza blokiem.
        if isEnd:
            check_x = True
            check_y = True
            for i in range(4):
                if self.tab[i].x + xmv < 0 or self.tab[i].x + xmv > N - 1:
                    check_x = False
                if self.tab[i].y + ymv > M - 1:
                    check_y = False
            check = self.check_sites()
            if check_x or check_y:
                for i in range(4):
                    if check_x and check:
                        self.tab[i].x += xmv
                    if check_y:
                        self.tab[i].y += ymv

    def check_height(self):  # Funkcja sprawdza czy blok "dotkął podłogi/ bloku" pod sobą. Jeśli tak to zwraca False, w przeciwnym wypadku True.
        for i in range(4):
            if self.tab[i].y + 1 > M - 1:
                return False
            elif self.blocksTab[self.tab[i].y + 1][self.tab[i].x].empty:
                return False
        return True

    def check_sites(self):  # Funkcja sprawdza czy możliwe jest przemieszczenie w poziomie. Jeśli tak zwraca True, w przeciwnym wypadku False.
        for i in range(4):
            x_min = self.tab[i].x - 1
            x_max = self.tab[i].x + 1
            if x_min >= 0:
                if self.blocksTab[self.tab[i].y][self.tab[i].x - 1].empty:
                    return False
            if x_max < N:
                if self.blocksTab[self.tab[i].y][self.tab[i].x + 1].empty:
                    return False
        return True

    def delete_line(self):  # Funkcja usuwa wiersze w pełni zapełnione
        for y in range(M):
            counter = 0
            for x in range(N):
                if self.blocksTab[y][x].empty:
                    counter += 1
            if counter == N:
                self.points += 200
                for line in range(y - 1, -1, -1):
                    for x in range(0, N):
                        self.blocksTab[line + 1][x].empty = self.blocksTab[line][x].empty
                        self.blocksTab[line + 1][x].color = self.blocksTab[line][x].color

    def view_background(self):
        gameDisplay.blit(background, (0, 0))
        self.print_panel((pos_x-200) // 2, pos_y + 66)
        self.print_panel((pos_x-200) // 2, pos_y + 332)
        gameDisplay.blit(play_panel, (pos_x - 25, pos_y - 25))
        pygame.draw.rect(gameDisplay, (98, 98, 98), (pos_x - 5, pos_y - 5, board_width + 10, board_height + 10))
        pygame.draw.rect(gameDisplay, (45, 53, 73), (pos_x, pos_y, board_width, board_height))
        pygame.Surface.blit(gameDisplay, self.grid, (pos_x, pos_y))

    def print_panel(self, x, y):
        gameDisplay.blit(obszar, (x, y))
        gameDisplay.blit(obszar_light, (x + 10, y + 10))

    def can_rotate(self):
        for i in range(4):
            if self.tab[i].x >= 2 and self.tab[i].x <= 17:
                return True
            elif self.tab[i].x == 1:
                pass

    def check_gameover(self):
        for x in range(N):
            if self.blocksTab[0][x].empty is True:
                return True
        return False

    def pause_button(self, x=800, y=600):
        gameDisplay.blit(button_background, (x, y))
        if Menu.mouse_contained(self.Menu, x, y, x + 50, y + 50):
            gameDisplay.blit(button_inside2, (x + 3, y + 3))
            gameDisplay.blit(pause, (x, y))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.image.save(gameDisplay, 'surface.bmp')
                if self.paused is False:
                    self.paused = True
                else:
                    self.paused = False
                self.game_pause(x, y)
        else:
            gameDisplay.blit(button_inside1, (x + 3, y + 3))
            gameDisplay.blit(pause, (x, y))

    def stop_button(self, x=720, y=600):
        gameDisplay.blit(button_background, (x, y))
        if Menu.mouse_contained(self.Menu, x, y, x + 50, y + 50):
            gameDisplay.blit(button_inside2, (x + 3, y + 3))
            gameDisplay.blit(stop, (x, y))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.paused = False
                self.stop = True
        else:
            gameDisplay.blit(button_inside1, (x + 3, y + 3))
            gameDisplay.blit(stop, (x, y))

    def game_pause(self, x, y):
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            gameDisplay.blit(pygame.image.load('surface.bmp'), (0, 0))
            font = pygame.font.SysFont("comicsansms", 60)
            text = font.render('Game paused', True, white)
            gameDisplay.blit(text, (pos_x + (board_width - text.get_width()) // 2, 300))
            self.pause_button(x, y)
            self.stop_button(720, 600)
            pygame.display.update()




# Config
M = 20
N = 10
block_size = 30
display_width = 900
display_height = 700
board_width = N * block_size
board_height = M * block_size
pos_x = (display_width - board_width) // 2
pos_y = (display_height - board_height) // 2

menu_button_w = 200
menu_button_h = 50

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
menu_panel = pygame.transform.scale(pygame.image.load('panel.bmp'), (board_width, board_height))
play_panel = pygame.transform.scale(pygame.image.load('panel.bmp'), (board_width + 50, board_height + 50))
obszar = pygame.transform.scale(pygame.image.load('panel_kwadrat.bmp'), (200, 200))
obszar_light = pygame.transform.scale(pygame.image.load('panel_kwadrat2.bmp'), (180, 180))
button_1 = pygame.transform.scale(pygame.image.load('button.bmp'), (menu_button_w, menu_button_h))
button_2 = pygame.transform.scale(pygame.image.load('button2.bmp'), (menu_button_w, menu_button_h))

# Przyciski play/pause/stop
button_background = pygame.transform.scale(pygame.image.load('panel_kwadrat.bmp'), (50, 50))
button_inside1 = pygame.transform.scale(pygame.image.load('panel_kwadrat2.bmp'), (44, 44))
button_inside2 = pygame.transform.scale(pygame.image.load('panel_kwadrat3.bmp'), (44, 44))
pause = pygame.transform.scale(pygame.image.load('pause-play_button.bmp'), (50, 50))
stop = pygame.transform.scale(pygame.image.load('stop.bmp'), (50, 50))

# Initialization
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.SRCALPHA)
pygame.display.set_caption('Tetris')
pygame.display.set_icon(bc_yellow)

if __name__ == "__main__":
    Menu()
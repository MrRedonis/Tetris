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

def InsertionSort(tab):
    for x in range(1,len(tab)):
        key = tab[x]
        y = x-1
        while y >= 0 and tab[y] < key:
            tab[y+1] = tab[y]
            y = y-1
        tab[y+1] = key

class Menu:
    def __init__(self):
        self.open_function = 0
        self.music = True

        self.engine()

    def main_menu(self):
        self.background()
        for x in range(5):
            x_pos = pos_x + 50
            y_pos = pos_y + 150 + 80 * x
            if self.mouse_contained(x_pos, y_pos, x_pos + menu_button_w, y_pos + menu_button_h):
                gameDisplay.blit(button_1, (x_pos, y_pos))
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if self.music and x % 5 != 0:
                        button_sound.play()
                    self.open_function = x + 1
            else:
                gameDisplay.blit(button_2, (x_pos, y_pos))
            text = font.render(menu_texts[x], True, white)
            gameDisplay.blit(text, (x_pos + (menu_button_w - text.get_width()) // 2, y_pos))
        pygame.display.update()

    def mouse_contained(self, x1, y1, x2, y2):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if x1 <= x <= x2:
            if y1 <= y <= y2:
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
        self.return_button(pos_x, pos_y)
        self.reset_button(pos_x, pos_y + 400)
        max = len(high_scores)
        for i in range(1,11):
            if i < max + 1:
                text = menu_font.render(str(i)+".  "+str(high_scores[i-1]), True, white)
            else:
                text = menu_font.render(str(i) + ".  ", True, white)
            gameDisplay.blit(text, (pos_x + 20, pos_y + 100 + 30 * i))
        pygame.display.update()

    def options_menu(self):
        self.background()
        self.return_button(pos_x, pos_y)
        music_text = ['Music ON', 'Music OFF']
        x_pos = pos_x + 50
        y_pos = pos_y + 150
        if self.music:
            text = font.render('Music OFF', True, white)
        else:
            text = font.render('Music ON', True, white)
        if self.mouse_contained(x_pos, y_pos, x_pos + menu_button_w, y_pos + menu_button_h):
            gameDisplay.blit(button_1, (x_pos, y_pos))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.music:
                        button_sound.play()
                    if self.music:
                        text = font.render(music_text[0], True, white)
                        self.music = False
                    else:
                        text = font.render(music_text[1], True, white)
                        self.music = True
        else:
            gameDisplay.blit(button_2, (x_pos, y_pos))
            if self.music:
                text = font.render(music_text[0], True, white)
            else:
                text = font.render(music_text[1], True, white)

        gameDisplay.blit(text, (x_pos + (menu_button_w - text.get_width()) // 2, y_pos))

        pygame.display.update()
        print(self.music)



    def about(self):
        x_pos = pos_x + 50
        y_pos = pos_y + 50
        self.background()
        self.return_button(pos_x, pos_y)
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

    def return_button(self, x, y):
        x_pos = x + 50
        y_pos = y + 50
        if self.mouse_contained(x_pos, y_pos, x_pos + menu_button_w, y_pos + menu_button_h):
            gameDisplay.blit(button_1, (x_pos, y_pos))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.music:
                    button_sound.play()
                self.open_function = 0
        else:
            gameDisplay.blit(button_2, (x_pos, y_pos))
        text = font.render("Return", True, white)
        gameDisplay.blit(text, (x_pos + (menu_button_w - text.get_width()) // 2, y_pos))

    def reset_button(self, x, y):
        x_pos = x + 50
        y_pos = y + 50
        if self.mouse_contained(x_pos, y_pos, x_pos + menu_button_w, y_pos + menu_button_h):
            gameDisplay.blit(button_1, (x_pos, y_pos))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.music:
                    button_sound.play()
                plik = open("wyniki.txt", "w")
                plik.write("")
                plik.close()
                high_scores.clear()
        else:
            gameDisplay.blit(button_2, (x_pos, y_pos))
        text = font.render("Reset", True, white)
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
        self.tab_next = self.figure()
        self.color = self.color_gen()
        self.color_next = self.color_gen(self.color)
        self.clock = pygame.time.Clock()
        self.move_speed = 14
        self.fps = 14
        self.tick = 0
        self.isEnd = True
        self.points = 0
        self.paused = False
        self.stop = False
        self.level = 1
        self.level_points = 0

        if self.Menu.music:
            start_game.play()

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
                speed = 1

            self.tick += 1
            if self.tick % speed == 0:
                ymv = 1
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.points += 1
                    self.level_points += 1
                    print(self.level_points)
            if xmv != 0 or ymv != 0:
                self.move(xmv, ymv)
            self.isEnd = self.check_height()

            self.view_background()
            self.print_block(self.color, self.tab, pos_x, pos_y)

            if not self.isEnd:
                for i in range(4):
                    self.blocksTab[self.tab[i].y][self.tab[i].x].empty = True
                    self.blocksTab[self.tab[i].y][self.tab[i].x].color = self.color

                self.tab = self.tab_next
                self.tab_next = self.figure()
                self.color = self.color_next
                self.color_next = self.color_gen(self.color)

            self.delete_line()
            self.print_all()
            if self.check_gameover():
                return
            self.pause_button(pause_x, pause_y)
            self.stop_button(stop_x, stop_y)
            if self.stop is True:
                return
            pygame.display.update()

    def color_gen(self, last=-1):  # Generator liczb odpowiadajacych kolorom z pominieciem ostatniego.
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
            tab[i].y = self.figures[n][i] // 2
        tab[0].name = n
        tab = self.rotate(True, tab, True)
        self.set_default_position(tab)
        return tab

    def print_all(self):  # Funkcja rysuje już postawione bloki, które są zapisane w blockColors.
        for y in range(M):
            for x in range(N):
                if self.blocksTab[y][x].empty is True:
                    pygame.Surface.blit(gameDisplay, self.blockColors[self.blocksTab[y][x].color],
                                        (pos_x + x * block_size, pos_y + y * block_size))

    def print_block(self, color, tab, x, y):  # Funkcja rysuje całą figurę wg wzoru w tab[].
        for i in range(4):
            pygame.Surface.blit(gameDisplay, self.blockColors[color],
                                (x + tab[i].x * block_size, y + tab[i].y * block_size))

    def rotate(self, is_end, tab, first=False):  # Funkcja obraca blok jeśli isEnd == True.
        if is_end and self.can_rotate(tab, first):
            if tab[0].name == 6:
                if self.Menu.music:
                    rotate_sound.play()
                return tab
            point = Point(tab[1].x, tab[1].y)
            tmp = [Point() for _ in range(4)]
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
                if self.Menu.music and not first:
                    rotate_sound.play()
                for i in range(4):
                    tab[i].x = tmp[i].x
                    tab[i].y = tmp[i].y
        return tab

    def move(self, xmv, ymv):  # Funkcja sprawdza czy porusza się w siatce gry i porusza blokiem.
        if True:
            check_x = True
            check_y = True
            for i in range(4):
                if self.tab[i].x + xmv < 0 or self.tab[i].x + xmv > N - 1:
                    check_x = False
                if self.tab[i].y + ymv > M - 1:
                    check_y = False
            if check_x and self.check_sites(xmv):
                for i in range(4):
                    self.tab[i].x += xmv
            if check_y:
                for i in range(4):
                    self.tab[i].y += ymv

    def check_height(self):  # Funkcja sprawdza czy blok "dotkął podłogi/ bloku" pod sobą. Jeśli tak to zwraca False, w przeciwnym wypadku True.
        for i in range(4):
            if self.tab[i].y + 1 > M - 1:
                return False
            elif self.blocksTab[self.tab[i].y + 1][self.tab[i].x].empty:
                return False
        return True

    def check_sites(self, xmv):  # Funkcja sprawdza czy możliwe jest przemieszczenie w poziomie. Jeśli tak zwraca True, w przeciwnym wypadku False.
        for i in range(4):
            x = self.tab[i].x + xmv
            if 0 > x or x >= N:
                return False
            elif self.blocksTab[self.tab[i].y][x].empty is True:
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
                self.level_points += 200
                for line in range(y - 1, -1, -1):
                    for x in range(0, N):
                        self.blocksTab[line + 1][x].empty = self.blocksTab[line][x].empty
                        self.blocksTab[line + 1][x].color = self.blocksTab[line][x].color

    def view_background(self):
        gameDisplay.blit(background, (0, 0))
        if self.level < 3:
            self.next_block_panel()
        self.score_panel()
        gameDisplay.blit(play_panel, (pos_x - 25, pos_y - 25))
        pygame.draw.rect(gameDisplay, (98, 98, 98), (pos_x - 5, pos_y - 5, board_width + 10, board_height + 10))
        pygame.draw.rect(gameDisplay, (45, 53, 73), (pos_x, pos_y, board_width, board_height))
        pygame.Surface.blit(gameDisplay, self.grid, (pos_x, pos_y))

    def print_panel(self, x, y):
        gameDisplay.blit(obszar, (x, y))
        gameDisplay.blit(obszar_light, (x + 10, y + 10))

    def can_rotate_simple(self, tab):
        if tab[0].name == {2, 3, 6}:
            return True
        else:
            if tab[0].name == {1, 4}:
                if tab[1].y >= 1:
                    return True
                return False
            else:
                if tab[1].y >= 2:
                    return True
                return False

    def can_rotate(self, tab, check):
        if check:
            return True
        if self.can_rotate_simple(tab):
            tmp = [Point() for _ in range(4)]
            for i in range(4):
                tmp[i].x = tab[i].x
                tmp[i].y = tab[i].y
            point = Point(tmp[1].x, tmp[1].y)
            for i in range(4):
                x = tab[i].y - point.y
                y = tab[i].x - point.x
                tmp[i].x = point.x - x
                tmp[i].y = point.y + y
                if tmp[i].x < 0 or tmp[i].x > N - 1:
                    return False
                if tmp[i].y > M - 1:
                    return False
            for i in range(4):
                if self.blocksTab[tmp[i].y][tmp[i].x].empty:
                    return False
            return True

    def check_gameover(self):
        for x in range(N):
            if self.blocksTab[0][x].empty is True:
                self.gameover()
                return True
        return False

    def gameover(self, paused=False):
        if not paused:
            pygame.image.save(gameDisplay, 'surface.bmp')
        gameDisplay.blit(pygame.image.load('surface.bmp'), (0, 0))
        gameDisplay.blit(button_background, (pause_x, pause_y))
        gameDisplay.blit(button_inside1, (pause_x + 3, pause_y + 3))
        gameDisplay.blit(pause, (pause_x, pause_y))
        gameDisplay.blit(button_background, (stop_x, stop_y))
        gameDisplay.blit(button_inside1, (stop_x + 3, stop_y + 3))
        gameDisplay.blit(stop, (stop_x, stop_y))
        font = pygame.font.SysFont("comicsansms", 60)
        text = font.render('Game over', True, white)
        gameDisplay.blit(text, (pos_x + (board_width - text.get_width()) // 2, 300))
        pygame.display.update()
        high_scores.append(self.points)
        InsertionSort(high_scores)
        text = open("wyniki.txt", "w")
        for x in range(len(high_scores) - 1):
            text.write(str(high_scores[x])+",")
        text.write(str(high_scores[len(high_scores) - 1]))
        text.close()
        pygame.time.wait(2000)

    def pause_button(self, x=690, y=600):
        gameDisplay.blit(button_background, (x, y))
        if Menu.mouse_contained(self.Menu, x, y, x + 50, y + 50):
            gameDisplay.blit(button_inside2, (x + 3, y + 3))
            gameDisplay.blit(pause, (x, y))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Menu.music:
                        button_sound.play()
                    pygame.image.save(gameDisplay, 'surface.bmp')
                    if self.paused is False:
                        self.paused = True
                    else:
                        self.paused = False
                    return self.game_pause(x, y, pygame.image.load('surface.bmp'))
        else:
            gameDisplay.blit(button_inside1, (x + 3, y + 3))
            gameDisplay.blit(pause, (x, y))

    def stop_button(self, x=780, y=600):
        gameDisplay.blit(button_background, (x, y))
        if Menu.mouse_contained(self.Menu, x, y, x + 50, y + 50):
            gameDisplay.blit(button_inside2, (x + 3, y + 3))
            gameDisplay.blit(stop, (x, y))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Menu.music:
                        button_sound.play()
                    if self.paused:
                        self.paused = False
                        self.gameover(True)
                    else:
                        self.gameover(False)

                    pygame.display.update()
                    self.stop = True
        else:
            gameDisplay.blit(button_inside1, (x + 3, y + 3))
            gameDisplay.blit(stop, (x, y))

    def game_pause(self, x, y, surface):
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            gameDisplay.blit(surface, (0, 0))
            font = pygame.font.SysFont("comicsansms", 60)
            text = font.render('Game paused', True, white)
            gameDisplay.blit(text, (pos_x + (board_width - text.get_width()) // 2, 300))
            self.pause_button(x, y)
            self.stop_button(stop_x, stop_y)
            pygame.display.update()

    def print_score(self):
        text = font.render('Score', True, white)
        x = ((pos_x - 200) // 2) + (200 - text.get_width()) // 2
        gameDisplay.blit(text, (x, pos_y + 340))
        text = font.render(str(self.points), True, white)
        x = ((pos_x - 200) // 2) + (200 - text.get_width()) // 2
        gameDisplay.blit(text, (x, pos_y + 380))

    def check_block_size(self, tab):
        x_min = tab[0].x
        x_max = tab[0].x
        y_min = tab[0].y
        y_max = tab[0].y
        for i in range(1,4):
            if tab[i].x > x_max: x_max = tab[i].x
            if tab[i].x < x_min: x_min = tab[i].x
            if tab[i].y > y_max: y_max = tab[i].y
            if tab[i].y < y_min: y_min = tab[i].y
        return x_min, x_max, y_min, y_max

    def next_block_panel(self):
        size = self.check_block_size(self.tab_next)
        self.print_panel((pos_x - 200) // 2, pos_y + 66)
        text = font.render('Next block', True, white)
        gameDisplay.blit(text, (50 + (200 - text.get_width()) // 2, 130))
        self.print_block(self.color_next, self.tab_next, 35 - size[0] * 30 + (200 - (size[1] - size[0]) * 30) // 2,
                         160 - size[2] * 30 + (100 - (size[3] - size[2]) * 30) // 2)

    def score_panel(self):
        self.print_panel((pos_x - 200) // 2, pos_y + 332)
        self.print_score()
        self.print_level()
        if self.level_points >= 1000:
            self.level_points -= 1000
            self.level += 1

    def set_default_position(self, tab):
        size = self.check_block_size(tab)
        r_x = size[1] - size[0] + 1 # Długość bloku
        rx = (N - r_x) // 2 # Gdzie powinien być min x

        for j in range(size[2]):
            for i in range(4):
                tab[i].y -= 1

        if rx - size[0] < 0:
            x = 1
        else:
            x = -1
        size = abs(rx - size[0])
        for j in range(size):
            for i in range(4):
                tab[i].x -= x

    def print_level(self):
        text = font.render('Level', True, white)
        x = ((pos_x - 200) // 2) + (200 - text.get_width()) // 2
        gameDisplay.blit(text, (x, pos_y + 420))
        text = font.render(str(self.level), True, white)
        x = ((pos_x - 200) // 2) + (200 - text.get_width()) // 2
        gameDisplay.blit(text, (x, pos_y + 460))

    def last_move(self):
        pass



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

stop_x = 780
stop_y = 600
pause_x = 690
pause_y = 600

font = pygame.font.SysFont("comicsansms", 30)
menu_font = pygame.font.SysFont("comicsansms", 20)
menu_texts = ["Play", "High Scores", "Options", "About", "Quit"]
about_text = "Game crated by Damian Jurkiewicz (MrRedonis). Main menu background graphic created by Freepic."

high_scores = []
text = open("wyniki.txt", "r")
readings = (text.readline())
text.close()
if not readings == "":
    words = readings.split(",")
    for x in range(len(words)):
        high_scores.append(int(words[x]))

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

# Music
start_game = pygame.mixer.Sound('start_game.ogg')
rotate_sound = pygame.mixer.Sound('rotate.ogg')
button_sound = pygame.mixer.Sound('button.ogg')
move_sound = pygame.mixer.Sound('move.ogg')

if __name__ == "__main__":
    Menu()
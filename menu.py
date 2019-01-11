import pygame

pygame.init()

class Game:
    def __init__(self):
        self.open_function = 0
        self.engine()

    def main_menu(self):
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(menu_panel, (pos_x, pos_y))
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
        pass

    def high_scores_menu(self):
        pass

    def options_menu(self):
        pass

    def about(self):
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(menu_panel, (pos_x, pos_y))
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

Game()
import pygame
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)
grey = (115, 115, 115)
orange = (230, 115, 0)


class Brush_and_Colours():
    def __init__(self, display):
        pygame.init()
        self.mouse_position_x = 0
        self.mouse_position_y = 0
        self.game_display = display
        self.colours = {
            "black": (0, 0, 0),
            "red": (200, 0, 0),
            "green": (40, 200, 0),
            "blue": (60, 120, 210),
            "navy": (5, 45, 115),
            "yellow": (250, 200, 0),
            "purple": (100, 0, 200),
            "brown": (130, 65, 0),
            "orange": (255,105,0),
        }
        self.x_coordinates={
            "black": (425),
            "red": (500),
            "green": (575),
            "blue": (650),
            "navy": (725),
            "yellow": (800),
            "purple": (875),
            "brown": (950),
            "orange":(1025),
        }
    def Colour_Blots(self):
        for i in self.colours:
            self.blot_border = pygame.Rect(self.x_coordinates[i]-2, 3, 54, 54)
            self.blot=pygame.Rect(self.x_coordinates[i],5,50,50)
            pygame.draw.ellipse(self.game_display, black, self.blot_border)
            pygame.draw.ellipse(self.game_display, self.colours[i], self.blot)


class Canvas():
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.screen = pygame.Rect(0, 0, *self.screen_size)
        pygame.init()
        self.game_display = pygame.display.set_mode(screen_size)

    def drawing_prompt_box(self):
        self.drawing_prompt_border = pygame.Rect(0, 0, 200, 100)
        self.drawing_prompt = pygame.Rect(1, 1, 198, 98)
        pygame.draw.rect(self.game_display, black, self.drawing_prompt_border)
        pygame.draw.rect(self.game_display, grey, self.drawing_prompt)

    def timer_prompt_box(self):
        self.timer_box_border = pygame.Rect(200, 0, 200, 100)
        self.timer_box = pygame.Rect(200, 1, 198, 98)
        pygame.draw.rect(self.game_display, black, self.timer_box_border)
        pygame.draw.rect(self.game_display, grey, self.timer_box)

    def colour_pallete(self):
        self.colours_box_border = pygame.Rect(400, 0, 800, 100)
        self.colours_box = pygame.Rect(399, 1, 798, 98)
        pygame.draw.rect(self.game_display, black, self.colours_box_border)
        pygame.draw.rect(self.game_display, orange, self.colours_box)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

    def run(self):
        clock = pygame.time.Clock()
        drawing = Brush_and_Colours(self.game_display)
        while True:
            self.game_display.fill(white)
            self.drawing_prompt_box()
            self.timer_prompt_box()
            self.colour_pallete()
            drawing.Colour_Blots()
            self.event_handler()
            pygame.display.update()
            clock.tick(15)


if __name__ == "__main__":
    size = (1200, 800)
    new_game = Canvas(size)
    new_game.run()

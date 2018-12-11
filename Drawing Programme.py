import pygame
from pygame.locals import *
import time
import random
black = (0, 0, 0)
white = (255, 255, 255)
grey = (115, 115, 115)
orange = (230, 115, 0)


class Brush_and_Colours():
    def __init__(self, display):
        pygame.init()
        pygame.font.init()
        self.mouse_position=pygame.mouse.get_pos()
        self.brush_strokes = []
        self.brush_strokes_colour=[]
        self.clear_button = pygame.Rect(1100, 5, 50, 50)
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
        self.selected_colour = self.colours["black"]
    def Colour_Blots(self):
        for i in self.colours:
            if self.selected_colour==self.colours[i]:
                self.blot_border = pygame.Rect(self.x_coordinates[i] - 2, 3, 54, 54)
                self.blot = pygame.Rect(self.x_coordinates[i], 5, 50, 50)
                pygame.draw.ellipse(self.game_display, white, self.blot_border)
                pygame.draw.ellipse(self.game_display, self.colours[i], self.blot)
            else:
                self.blot_border = pygame.Rect(self.x_coordinates[i]-2, 3, 54, 54)
                self.blot=pygame.Rect(self.x_coordinates[i],5,50,50)
                pygame.draw.ellipse(self.game_display, black, self.blot_border)
                pygame.draw.ellipse(self.game_display, self.colours[i], self.blot)
    def Clear_Canvas_Button(self):
        self.clear_border = pygame.Rect(1098, 3, 54, 54)

        pygame.draw.ellipse(self.game_display, black, self.clear_border)
        pygame.draw.ellipse(self.game_display, white, self.clear_button)

        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text=self.font.render("C",True,black)
        self.game_display.blit(self.text, (1115, 8))
    def Clear_Canvas(self):
        if self.clear_button.collidepoint(self.mouse_position)==True and pygame.mouse.get_pressed()[0]==True:
            self.brush_strokes=[]
            self.brush_strokes_colour=[]
        else:
            pass
    def Brush(self):

        for i in range (len(self.brush_strokes)-1):
            pygame.draw.ellipse(self.game_display,self.brush_strokes_colour[i],self.brush_strokes[i])

    def Colour_Selection(self):
        for i in self.x_coordinates:
            self.detection_rect=pygame.Rect(self.x_coordinates[i]-2, 3, 54, 54)
            if self.detection_rect.collidepoint(self.mouse_position)==True and pygame.mouse.get_pressed()[0]==True:
                self.selected_colour=self.colours[i]

            else:
                pass
    def event_handler(self):
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]==True:

                if self.mouse_position[1]>100:
                    self.brush_strokes.append(pygame.Rect(self.mouse_position[0], self.mouse_position[1], 20, 20))
                    self.brush_strokes_colour.append(self.selected_colour)
                else:
                    pass
            elif event.type==QUIT:
                pygame.quit()
                quit()
    def run (self):

        self.mouse_position=pygame.mouse.get_pos()
        self.Colour_Blots()
        self.Clear_Canvas_Button()
        self.Clear_Canvas()
        self.Colour_Selection()
        self.Brush()
        self.event_handler()

class Timer():

    def __init__(self,display):

        self.game_display=display
        self.time_limit=60
        self.endtime = int(time.time()) + self.time_limit
        self.remaining_time=self.endtime-int(time.time())
    def timer_display(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render(str(self.remaining_time), True, white)
        self.game_display.blit(self.text, (202, 35))
    def event_handler(self):
        if self.remaining_time==0:
            pygame.quit()
            quit()
    def run(self):
        self.remaining_time = self.endtime - int(time.time())
        self.event_handler()
        self.timer_display()
class Drawing_Prompt():
    def __init__(self,display):
        self.game_display = display
        self.drawing_prompts=["Aeroplane","Cat","Dog"]
        self.selected_prompt=self.drawing_prompts[random.randint(0,2)]
    def prompt_display(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render(str(self.selected_prompt), True, white)
        self.game_display.blit(self.text, (2, 35))
    def run(self):
        self.prompt_display()
class Canvas():
    def __init__(self, display):
        self.game_display = display

    def drawing_prompt_box(self):
        self.drawing_prompt_border = pygame.Rect(0, 0, 200, 100)
        self.drawing_prompt = pygame.Rect(1, 1, 198, 98)
        pygame.draw.rect(self.game_display, black, self.drawing_prompt_border)
        pygame.draw.rect(self.game_display, grey, self.drawing_prompt)

        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render("Drawing Prompt:", True, white)
        self.game_display.blit(self.text, (2, 0))

    def timer_prompt_box(self):
        self.timer_box_border = pygame.Rect(200, 0, 200, 100)
        self.timer_box = pygame.Rect(200, 1, 198, 98)
        pygame.draw.rect(self.game_display, black, self.timer_box_border)
        pygame.draw.rect(self.game_display, grey, self.timer_box)

        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render("Timer:", True, white)
        self.game_display.blit(self.text,(202,0))

    def colour_pallete(self):
        self.colours_box_border = pygame.Rect(400, 0, 800, 100)
        self.colours_box = pygame.Rect(399, 1, 798, 98)
        pygame.draw.rect(self.game_display, black, self.colours_box_border)
        pygame.draw.rect(self.game_display, orange, self.colours_box)


    def run(self):
        clock = pygame.time.Clock()
        drawing = Brush_and_Colours(self.game_display)
        time=Timer(self.game_display)
        prompt=Drawing_Prompt(self.game_display)
        while True:
            self.game_display.fill(white)
            self.drawing_prompt_box()
            self.timer_prompt_box()
            self.colour_pallete()
            drawing.run()
            prompt.run()
            time.run()
            pygame.display.update()
            clock.tick(5000)
class Game():
    def __init__(self,screen_size):
        self.screen_size = screen_size
        self.screen = pygame.Rect(0, 0, *self.screen_size)
        pygame.init()
        self.game_display = pygame.display.set_mode(screen_size)


    def run (self):
        display =Canvas(self.game_display)

        while True:
            display.run()



if __name__ == "__main__":
    size = (1200, 800)
    new_game = Game(size)
    new_game.run()

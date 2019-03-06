import pygame
from pygame.locals import *
from keras.models import load_model
import time
import random
black = (0, 0, 0)
white = (255, 255, 255)
grey = (115, 115, 115)
orange = (230, 115, 0)
drawing_prompts=["Apple","Pineapple","Dog","Grapes","Banana","Airplane","Bat"]
Round_Times_Remaining=[]
Round_Active = True
Rounds_Played=1

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
    def Drawing(self):
        if pygame.mouse.get_pressed()[0]==True:
            if self.mouse_position[1]>100:
                self.brush_strokes.append(pygame.Rect(self.mouse_position[0], self.mouse_position[1], 20, 20))
                self.brush_strokes_colour.append(self.selected_colour)
            else:
                pass

    def run (self):

        self.mouse_position=pygame.mouse.get_pos()
        self.Colour_Blots()
        self.Clear_Canvas_Button()
        self.Clear_Canvas()
        self.Colour_Selection()
        self.Brush()
        self.Drawing()

class Timer():

    def __init__(self,display):

        self.game_display=display

        self.end_round_button = pygame.Rect(300, 12, 75, 75)
        self.time_limit=10
        self.endtime = int(time.time()) + self.time_limit
        self.remaining_time=self.endtime-int(time.time())
    def timer_display(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render(str(self.remaining_time), True, white)
        self.game_display.blit(self.text, (202, 35))
    def timer_complete(self):
        global Round_Active
        if self.remaining_time==0 :
            Round_Active=False


    def end_round_early_button(self):
        self.end_round_button_border = pygame.Rect(298, 10, 79, 79)

        pygame.draw.rect(self.game_display, black, self.end_round_button_border)
        pygame.draw.rect(self.game_display, white, self.end_round_button)

        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text1 = self.font.render("End ", True, black)
        self.text2 = self.font.render("Early", True, black)
        self.game_display.blit(self.text1, (303, 8))
        self.game_display.blit(self.text2, (303, 38))

    def event_handler(self):
        global Round_Times_Remaining
        self.mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:

                if self.end_round_button.collidepoint(self.mouse_position)==True:

                    Round_Times_Remaining.append(self.remaining_time)
                    self.remaining_time=0
            elif event.type==QUIT:
                pygame.quit()
                quit()

    def run(self):

        self.remaining_time = self.endtime - int(time.time())
        self.end_round_early_button()
        self.timer_display()
        self.event_handler()
        self.timer_complete()




class Drawing_Prompt():
    def __init__(self,display):
        global drawing_prompts
        self.game_display = display
        self.selected_prompt=drawing_prompts[random.randint(0,(len(drawing_prompts)-1))]
        drawing_prompts.remove(self.selected_prompt)
    def prompt_display(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render(str(self.selected_prompt), True, white)
        self.game_display.blit(self.text, (2, 35))
    def run(self):
        self.prompt_display()


class Round_Transition():
    def __init__(self, display):
        self.game_display = display
    def transition_message(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 50)
        self.text = self.font.render("Prepare for the next Round", True, orange)
        self.game_display.blit(self.text, (100, 100))
    def drawing_capture(self):
        self.capture_rect = pygame.Rect(0, 100, 1200,700)
        self.sub_surface = self.game_display.subsurface(self.capture_rect)
        pygame.image.save(self.sub_surface, ("Image"+str(Rounds_Played)+".tiff"))
    def run(self):
        global Round_Active
        global Rounds_Played
        self.drawing_capture()
        self.game_display.fill(black)
        self.transition_message()
        Round_Active = True
        Rounds_Played = Rounds_Played + 1

        pygame.display.update()
        time.sleep(0.5)




class End_Game_Screen():
    def __init__(self, display):
        self.game_display = display

    def score(self):
        self.score_box_border = pygame.Rect(0, 0, 200, 100)
        self.score_box = pygame.Rect(1, 1, 198, 98)
        pygame.draw.rect(self.game_display, black,  self.score_box_border)
        pygame.draw.rect(self.game_display, grey, self.score_box)

        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render("Score", True, white)
        self.game_display.blit(self.text, (2, 0))
    def average_accuracy(self):
        self.average_accuracy_border = pygame.Rect(200, 0, 300, 100)
        self.average_accuracy_box = pygame.Rect(201, 1, 298, 98)
        pygame.draw.rect(self.game_display, black, self.average_accuracy_border)
        pygame.draw.rect(self.game_display, grey, self.average_accuracy_box )

        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text = self.font.render("Average Accuracy", True, white)
        self.game_display.blit(self.text, (202, 0))
    def Play_Again_Button(self):
        self.Play_Again_border = pygame.Rect(500, 0, 800, 800)
        self.Play_Again_box = pygame.Rect(501, 1, 798, 798)
        pygame.draw.rect(self.game_display, black, self.Play_Again_border)
        pygame.draw.rect(self.game_display, orange, self.Play_Again_box)

        self.font = pygame.font.SysFont('Comic Sans MS', 50)
        self.text = self.font.render("Play Again", True, white)
        self.game_display.blit(self.text, (702, 375))
   # def load_model(self):
        #self.model = load_model('images.h5')
    def event_handler(self):
        global Rounds_Played
        global drawing_prompts
        self.mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]==True and self.mouse_position[0]>600:
                Rounds_Played=1
                drawing_prompts=["Aeroplane","Cat","Dog","Car","Lorry","Van","Bird"]

            elif event.type == QUIT:
                pygame.quit()
                quit()
    def run(self):
        clock = pygame.time.Clock()
        while Rounds_Played>5:
            self.game_display.fill(white)
            self.score()
            self.average_accuracy()
            self.Play_Again_Button()
            self.event_handler()
            pygame.display.update()
            clock.tick(5000)

class Canvas():
    def __init__(self,display):

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
        transition = Round_Transition(self.game_display)
        while Rounds_Played<=5:

            if Round_Active==True:
                self.game_display.fill(white)
                self.drawing_prompt_box()
                self.timer_prompt_box()
                self.colour_pallete()
                time.run()
                drawing.run()
                prompt.run()
                pygame.display.update()
                clock.tick(5000)
            else:
                transition.run()
                time = Timer(self.game_display)
                drawing = Brush_and_Colours(self.game_display)
                prompt = Drawing_Prompt(self.game_display)

class Game():
    def __init__(self,screen_size):
        self.screen_size = screen_size
        pygame.init()
        self.game_display = pygame.display.set_mode(screen_size)


    def run (self):
        display =Canvas(self.game_display)
        end_game = End_Game_Screen(self.game_display)
        while True:
            if Rounds_Played<=5:
                display.run()
            else:
                end_game.run()

if __name__ == "__main__":
    size = (1200, 800)
    new_game = Game(size)
    new_game.run()

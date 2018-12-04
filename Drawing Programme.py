import pygame
from pygame.locals import*
black=(0,0,0)
white=(255,255,255)
grey=(115,115,115)
orange=(230,115,0)
class Canvas():
    def __init__(self, screen_size):
        self.screen_size=screen_size
        self.screen=pygame.Rect(0,0,*self.screen_size)
        pygame.init()
        self.game_display=pygame.display.set_mode(screen_size)
    def drawing_prompt_box(self):
        self.drawing_prompt_border=pygame.Rect(0,0,200,100)
        self.drawing_prompt=pygame.Rect(1,1,198,98)
        pygame.draw.rect(self.game_display,black,self.drawing_prompt_border)
        pygame.draw.rect(self.game_display,grey,self.drawing_prompt)
    def timer_prompt_box(self):
        self.timer_box_border=pygame.Rect(200,0,200,100)
        self.timer_box=pygame.Rect(200,1,198,98)
        pygame.draw.rect(self.game_display,black,self.timer_box_border)
        pygame.draw.rect(self.game_display,grey,self.timer_box)
    def colour_pallete(self):
        self.colours_box_border = pygame.Rect(400, 0, 800, 100)
        self.colours_box = pygame.Rect(399, 1, 798, 98)
        pygame.draw.rect(self.game_display, black, self.colours_box_border)
        pygame.draw.rect(self.game_display, orange, self.colours_box)
    def event_handler(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                quit()
    def run(self):
        clock=pygame.time.Clock()
        while True:

            self.game_display.fill(white)
            self.drawing_prompt_box()
            self.timer_prompt_box()
            self.colour_pallete()
            self.event_handler()
            pygame.display.update()
            clock.tick(15)
if __name__=="__main__":
    size =(1200, 800)
    new_game = Canvas(size)
    new_game.run()

class Brush_and_Colours():
    def __init__(self):
        self.mouse_position_x=0
        self.mouse_position_y=0
        self.colours={
            "black":(0,0,0),
            "red":(200,0,0),
            "green":(0,200,0),
            "blue":(0,200,0),
            "orange":(230,115,0),
            "yellow":(250,200,0),
            "purple":(100,0,200),
            "brown":(130,65,0),



        }


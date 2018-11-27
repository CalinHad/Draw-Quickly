import pygame
from pygame.locals import*
white=(255,255,255)
class Canvas():
    def __init__(self, screen_size):
        self.screen_size=screen_size
        self.screen=pygame.Rect(0,0,*self.screen_size)
        pygame.init()
        self.game_display=pygame.display.set_mode(screen_size)
    def event_handler(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                quit()
    def run(self):
        clock=pygame.time.Clock()
        while True:
            self.game_display.fill(white)
            self.event_handler()
            pygame.display.update()
            clock.tick(15)
if __name__=="__main__":
    size =(1200, 800)
    new_game = Canvas(size)
    new_game.run()

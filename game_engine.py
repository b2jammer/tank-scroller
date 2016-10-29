import pygame,sys
from pygame.locals import *

class game_engine(object):
    def __init__(self,size=(800,600),title="Game Engine"):
        game_engine.DISPLAYWIDTH = size[0]
        game_engine.DISPLAYHEIGHT = size[1]
        self.DISPLAYSURF = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.BGCOLOR = (0,0,0)
        self.DISPLAYSURF.fill(self.BGCOLOR)

        self.GAME_CLOCK = pygame.time.Clock()

    def clock(self):
        return self.GAME_CLOCK

    def display(self):
        return self.DISPLAYSURF

    def tick(self,fps=60):
        self.DISPLAYSURF.fill(self.BGCOLOR)
        self.GAME_CLOCK.tick(fps)

ENGINE = game_engine((800,600),"The Little Voxel that Could")

CROSSHAIR = pygame.image.load('crosshair.png').convert()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        ENGINE.tick()
        crossPos = (pygame.mouse.get_pos()[0]-CROSSHAIR.get_width()//2,
                    pygame.mouse.get_pos()[1]-CROSSHAIR.get_height()//2)
        ENGINE.display().blit(CROSSHAIR,crossPos)
        pygame.display.update()

if __name__ == '__main__':main()

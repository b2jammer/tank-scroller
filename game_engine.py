import pygame,sys
from pygame.locals import *
import mob_class, settings

DISPLAYSURF = pygame.display.set_mode((320,240),RESIZABLE)

class game_engine(object):
    def __init__(self,size=(320,240),title="Game Engine"):
        game_engine.DISPLAYWIDTH = size[0]
        game_engine.DISPLAYHEIGHT = size[1]
        self.SURF = pygame.surface.Surface(size)
        pygame.display.set_caption(title)
        self.BGCOLOR = (0,0,0)
        self.SURF.fill(self.BGCOLOR)

        self.GAME_CLOCK = pygame.time.Clock()

        self.SPRITES = pygame.sprite.Group()

    def clock(self):
        return self.GAME_CLOCK

    def display(self):
        return self.SURF

    def tick(self,fps=settings.FPS):
        self.SURF.fill(self.BGCOLOR)
        ENGINE.sprites().update()
        ENGINE.sprites().draw(self.SURF)
        self.GAME_CLOCK.tick(fps)

    def sprites(self):
        return self.SPRITES

ENGINE = game_engine((320,240),"The Little Voxel that Could")

CROSSHAIR = pygame.image.load('crosshair.png').convert()
PLAYER = mob_class.player(3)
ENGINE.sprites().add(PLAYER)

PLAYER2 = mob_class.player(3)
ENGINE.sprites().add(PLAYER2)
PLAYER2.rect.y = 0

WINDOWSIZE = pygame.display.get_surface().get_size()

# Draw surface onto display, maintaining aspect ratio while filling as much
# screen real estate as possible.
def draw_screen(surface,display):
    global WINDOWSIZE
    display.fill((10,10,20))
    s_w = surface.get_width()
    s_h = surface.get_height()
    d_w = WINDOWSIZE[0]
    d_h = WINDOWSIZE[1]
    if ((d_w/d_h) > (s_w/s_h)): # Display wider than surface.
        s_a = s_w/s_h
        new_h = d_h
        new_w = d_h * s_a
        new_x = (d_w - new_w) // 2
        new_y = 0
    else:# Display taller than surface.
        s_a = s_h/s_w
        new_w = d_w
        new_h = d_w * s_a
        new_y = (d_h - new_h) // 2
        new_x = 0
##    print("Display:",(d_w,d_h))
##    print("Surface:",(new_w,new_h,new_y,new_x))
##    print('--------------')
    new_surf = pygame.transform.scale(surface,(int(new_w),int(new_h)))
    display.blit(new_surf,(int(new_x),int(new_y)))

def main():
    global WINDOWSIZE
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
               WINDOWSIZE = event.size
               DISPLAYSURF = pygame.display.set_mode(WINDOWSIZE,RESIZABLE)
        ENGINE.tick()
        draw_screen(ENGINE.display(),pygame.display.get_surface())
        pygame.display.update()

if __name__ == '__main__':main()

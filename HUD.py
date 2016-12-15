## HUD.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (150, 0, 0)
GREEN = (0, 255, 0)
clock_resolution = (200, 50)
timer_resolution = (180, 46)
hpbar_resolution = (156, 30)

class HUD(object):
    def __init__(self, DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT, timer_font, pcmaxhp):
        self.font = timer_font
        self.maxhp = pcmaxhp
        self.DISPLAYSURF = DISPLAYSURF
        self.DISPLAYWIDTH = DISPLAYWIDTH
        self.DISPLAYHEIGHT = DISPLAYHEIGHT
        self.CLOCKSURF = pygame.Surface(clock_resolution)
        self.CLOCKSURF.fill(BLACK)
        self.HPBARSURF = pygame.Surface(hpbar_resolution)
        self.HPBARSURF.fill(BLACK)

    def health_display(self, pchp):
        self.hp = pchp
        self.hppercent = (self.hp * 100)//self.maxhp
        self.pixeldraw = int(self.hppercent * 1.5)
        self.hpbarxstart = 3
        self.hpbarystart = 3
        self.HPBARSURF.fill(BLACK)
        pygame.draw.rect(self.HPBARSURF, RED, Rect((3, 3), (hpbar_resolution[0] - 6, hpbar_resolution[1] - 6)))
        if self.hp > 0:
            pygame.draw.rect(self.HPBARSURF, GREEN, Rect((3, 3), (self.pixeldraw, hpbar_resolution[1] - 6)))
        self.DISPLAYSURF.blit(self.HPBARSURF, (self.DISPLAYWIDTH//20, self.DISPLAYHEIGHT//36))
 
    def timer_display(self, time_remaining):

        minutes = time_remaining//3600
        temp_time = time_remaining - (minutes * 3600)
        seconds = temp_time//60
        if seconds < 10:
            display_seconds = "0" + str(seconds)
        else:
            display_seconds = seconds
            
        temp_time = (time_remaining - (minutes * 3600)) - (seconds * 60)
        centiseconds = int(temp_time * (100/60))
        if centiseconds < 10:
            display_centiseconds = "0" + str(centiseconds)
        else:
            display_centiseconds = centiseconds

        remaining_time = str(minutes) + ":" + str(display_seconds) + ":" + str(display_centiseconds)

        self.CLOCKSURF.fill(BLACK)
        TIMERSURF = self.font.render(remaining_time, True, WHITE, None)
        TIMERSURF = pygame.transform.scale(TIMERSURF, timer_resolution)
        self.CLOCKSURF.blit(TIMERSURF, (10, 2))
        self.DISPLAYSURF.blit(self.CLOCKSURF, ((self.DISPLAYWIDTH//12) * 5, self.DISPLAYHEIGHT//36))

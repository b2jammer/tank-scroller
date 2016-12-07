## menuLineG.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *

class menuLineG(object):
    def __init__(self, font, text):
        self.font = font
        self.text = text
        self.color = (255, 255, 255)
        self.SURF = self.font.render(text, True, self.color, None)
        self.text_size = self.SURF.get_size()
        self.SURF = pygame.transform.scale(self.SURF, self.text_size)
        SURF = self.SURF
        # Python had troubles calling self.SURF from this class for some
        # reason, but didn't have any problems calling SURF.

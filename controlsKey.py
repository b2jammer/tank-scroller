## controlsKey.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *

class controlsKey(object):

    def __init__(self, font1, font2, controlkey, text, DISPLAYHEIGHT, DISPLAYWIDTH):
        self.font1 = font1
        self.font2 = font2
        self.key = controlkey
        self.text = text
        self.color = (255, 255, 255)
        self.bgcolor = (0, 0, 0)
        
        self.surfheight = DISPLAYHEIGHT//7.2
        self.surfwidth = DISPLAYWIDTH//2
        self.CONTROLSSURF = pygame.Surface((self.surfwidth, self.surfheight))
        self.CONTROLSSURF.fill(self.bgcolor)

            
        def key_display(self):
            self.KEYSURF = pygame.Surface((self.surfheight, self.surfheight))

            pygame.draw.rect(self.KEYSURF, self.color, Rect((0, 0), (self.surfheight, self.surfheight)))
            pygame.draw.rect(self.KEYSURF, self.bgcolor, Rect((self.surfheight//10, self.surfheight//10), (self.surfheight - (self.surfheight//5), self.surfheight - (self.surfheight//5))))

            self.KEYLETTERSURF = self.font1.render(self.key, True, self.color, None)
            self.letter_size = self.KEYLETTERSURF.get_size()
            self.KEYLETTERSURF = pygame.transform.scale(self.KEYLETTERSURF, self.letter_size)

            self.KEYSURF.blit(self.KEYLETTERSURF, (self.surfheight//5, self.surfheight//5))
            
        def tutorial_text_display(self):

            self.CONTROLTEXTSURF = self.font2.render(self.text, True, self.color, None)
            self.text_size = self.CONTROLTEXTSURF.get_size()
            self.CONTROLTEXTSURF = pygame.transform.scale(self.CONTROLTEXTSURF, self.text_size)

        
        key_display(self)
        tutorial_text_display(self)

        self.CONTROLSSURF.blit(self.KEYSURF, (0, 0))
        self.CONTROLSSURF.blit(self.CONTROLTEXTSURF, (int(self.surfheight * 1.5), self.surfheight//5))
        CONTROLSSURF = self.CONTROLSSURF


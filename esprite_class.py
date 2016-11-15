import pygame,sys
from pygame.locals import *
import settings

class engine_sprite(pygame.sprite.Sprite):
    def __init__(self,engine):
        pygame.sprite.Sprite.__init__(self)
        self.move_x = 0
        self.move_y = 0
        self.ENGINE = engine
        self.ENGINE.sprites().add(self)

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
    
    def on_event(self,event):
        pass


import pygame,sys
from pygame.locals import *
import settings

class engine_sprite(pygame.sprite.Sprite):
    def __init__(self,engine):
        pygame.sprite.Sprite.__init__(self)
        self.move_x = 0
        self.move_y = 0
        self.dead = False
        self.draw_hitbox = False
        self.hitboxes = []
        self.ENGINE = engine
        self.ENGINE.sprites().add(self)

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        if not(self.alive()):
            del self

    def on_collision(self,other,hitbox,otherbox):
        pass
    
    def on_event(self,event):
        pass

    def kill(self):
        super().kill()
        del self

class hitbox(object):
    def __init__(self,rect,color,esprite):
        self.owner = esprite
        self.rect = rect
        self.color = color
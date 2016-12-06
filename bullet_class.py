import pygame,sys
from pygame.locals import *
import settings
import esprite_class
from esprite_class import engine_sprite
from vectors import Vector2D

class Bullet(engine_sprite):
    def __init__(self,engine,pos,direction=(1,0),damage=1):
        engine_sprite.__init__(self,engine)
        dirvec = Vector2D(direction[0],direction[1])
        normdir = dirvec.normalized()
        self.move_x,self.move_y = normdir*settings.BULLETSPEED
        self.damage = damage
        bullet_image = pygame.image.load('bullet.png').convert()
        self.image = pygame.transform.scale(bullet_image,(12,12))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = pos
        self.hitboxes.append(esprite_class.hitbox(self.rect,(0,255,0),self))

    def update(self):
        super().update()
        if self.rect.x > 1290 or self.rect.x < -10 or self.rect.y > 730 or self.rect.y < -10:
            self.kill()

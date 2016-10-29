import pygame,sys
from pygame.locals import *

class mob(pygame.sprite.Sprite):
    def __init__(self,health=1):
        pygame.sprite.Sprite.__init__(self)
        # Set up health variables.
        self.max_health = health
        self.health = self.max_health
        self.dead = False

    def update(self):
        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.on_death()

    def on_death(self):
        pass

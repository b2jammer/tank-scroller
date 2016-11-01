import pygame,sys
from pygame.locals import *
import settings

class mob(pygame.sprite.Sprite):
    def __init__(self,health=1):
        pygame.sprite.Sprite.__init__(self)
        # Set up health variables.
        self.max_health = health
        self.health = self.max_health
        self.dead = False
        # When mercy frames > 0, mob blinks and cannot take damage until
        # mercy frames drops back down to 0.
        self.mercy_frames = 0 

    # Call this method every frame.
    def update(self):
        self.check_health()
        if self.mercy_frames > 0:
            self.mercy_frames -= 1

    # Return true if still alive.
    def check_health(self):
        # Only do this check if not already dead.
        if self.health <= 0 and not self.dead:
            self.health = 0
            self.dead = True
            self.on_death()
        return not self.dead

    def take_damage(damage):
        self.health -= damage
        if self.check_health():
            self.on_survive()

    # Call this method if mob is still alive after taking damage.
    def on_survive(self):
        pass

    def on_death(self):
        pass

class player(mob):
    def __init__(self,health=3):
        mob.__init__(self,health)
        self.mercy_max = 90
        self.image = pygame.image.load(settings.PLAYER_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.y = 200

    def update(self):
        self.rect.x += 2.5
        if self.rect.x > 320:
            self.rect.x = -24

    def on_survive(self):
        self.mercy_frames = self.mercy_max

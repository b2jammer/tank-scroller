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

    def on_event(self,event):
        pass

class mob(engine_sprite):
    def __init__(self,engine,health=1):
        engine_sprite.__init__(self,engine)
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
        self.rect.x += self.move_x
        self.rect.y += self.move_y

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
    #Dict of vehicle names and corresponding sprites.
    vehicles = {'tank':pygame.image.load(settings.PLAYER_TANK_IMAGE),
                'plane':pygame.image.load(settings.PLAYER_PLANE_IMAGE)}
    def __init__(self,engine,health=3):
        mob.__init__(self,engine,health)
        self.mercy_max = 90
        self.vehicle_mode = 'plane'
        self.image = player.vehicles[self.vehicle_mode]
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 120

        self.x_speed = 2
        self.y_speed = 2

    def update(self):
        mob.update(self)
        if K_LEFT in self.ENGINE.key:
            self.move_x = -self.x_speed
        elif K_RIGHT in self.ENGINE.key:
            self.move_x = self.x_speed
        else:
            self.move_x = 0
        if K_UP in self.ENGINE.key:
            self.move_y = -self.y_speed
        elif K_DOWN in self.ENGINE.key:
            self.move_y = self.y_speed
        else:
            self.move_y = 0

    def on_event(self,event):
        pass

    def on_survive(self):
        self.mercy_frames = self.mercy_max

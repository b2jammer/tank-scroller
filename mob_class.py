import pygame,sys
from pygame.locals import *
import settings
from bullet_class import Bullet
import esprite_class
from esprite_class import engine_sprite

class mob(engine_sprite):
    def __init__(self,engine,health=1, sprite_kill_list=0, type_killed_num=0, indexnum=1000):
        engine_sprite.__init__(self,engine)
        pygame.sprite.Sprite.__init__(self)
        # Set up health variables.
        self.max_health = health
        self.health = self.max_health
        self.dead = False
        self.list_index = indexnum
        self.sprite_kill_list = sprite_kill_list
        self.type_killed_num = type_killed_num
        ## This is for the end of level--tracks how many of each enemy
        ## were killed and displays it.
        # When mercy frames > 0, mob blinks and cannot take damage until
        # mercy frames drops back down to 0.
        self.mercy_frames = 0 

    # Call this method every frame.
    def update(self):
        engine_sprite.update(self)
        self.check_health()
        if self.mercy_frames > 0:
            self.mercy_frames -= 1

    # Return true if still alive.
    def check_health(self):
        # Only do this check if not already dead.
        if self.health <= 0 and not self.dead:
            self.health = 0
            self.dead = True
            self.on_death(self.sprite_kill_list)
        return not self.dead

    def take_damage(self,damage):
        self.health -= damage
        if self.check_health():
            self.on_survive()

    # Call this method if mob is still alive after taking damage.
    def on_survive(self):
        pass

    def on_death(self):
        if self.list_index < 1000:
            self.sprite_kill_list.append(self.list_index)
            self.type_killed_num += 1
    ## Adds itself to a list that will be used to remove it from the
    ## drawn list.
    
    def index_update(self, indexnum):
        self.list_index = indexnum
    ## Called every time the sprite list is updated--whether it's from
    ## one being killed or one going offscreen, this is called
    ## to ensure it knows what its index location in the list is.

class meteor(mob):
    def __init__(self,engine,health=2,type_killed_num):
        mob.__init__(self,engine,health,type_killed_num)
        self.image = pygame.image.load('meteor.png').convert()
        self.rect = self.image.get_rect()
        self.hitboxes.append(esprite_class.hitbox(self.rect, (0, 255, 0), self))
        self.move_x = -5
    def update(self):
        super().update()
        if self.rect.x < -10 or self.rect.y > 730 or self.rect.y < -10:
            self.kill()
    def on_collision(self,other,hitbox,otherbox):
        print("Asteroid hit by something!")
        if type(other) is Bullet:
            print("Asteroid hit by Bullet!")
            print("Health before: "+str(self.health))
            self.take_damage(other.damage)
            print("Health after: "+str(self.health))
    def on_death(self):
        print("DIE!")
        self.type_killed_num += 1
        self.kill()
        if (self.alive()):
            print("KILL DOES NOTHING!")


class player(mob):
    #Dict of vehicle names and corresponding sprites.
    vehicles = {'tank':pygame.image.load(settings.PLAYER_TANK_IMAGE),
                'plane':pygame.image.load(settings.PLAYER_PLANE_IMAGE)}
    def __init__(self,engine,health=3):
        mob.__init__(self,engine,health)
        self.mercy_max = 90
        self.draw_hitbox = True
        self.vehicle_mode = 'plane'
        self.image = player.vehicles[self.vehicle_mode]
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 120

        self.x_speed = 10
        self.y_speed = 10

        self.bullet_timer = 0

        self.hitboxes.append(esprite_class.hitbox(self.rect, (0, 255, 0), self))

    def update(self):
        mob.update(self)

        if (self.bullet_timer > 0):
            self.bullet_timer -= 1
        
        if K_LEFT in self.ENGINE.key:
            self.move_x = -self.x_speed
        elif K_RIGHT in self.ENGINE.key:
            self.move_x = self.x_speed
        else:
            self.move_x = 0
            
        if pygame.mouse.get_pressed()[0]:
            if self.bullet_timer <= 0:
                new_bullet = Bullet(self.ENGINE,(self.rect.x+self.rect.width,
                                             self.rect.y+self.rect.height//2),
                                (1,0),1)
                self.bullet_timer = 10
            
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

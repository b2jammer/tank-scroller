## enemyTestClasses.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

## minion_list.append(0)
## minion_list[len(minion_list) - 1] = minionTestClass((DRAWDISTANCE, temp_y) minion_kill_list)

class minionTestClass(object):
    def __init__(self, pos, indexnum, sprite_kill_list, hp=10):
        self.pos = pos
        self.index_num = indexnum
        self.hp = hp
        self.sprite_kill_list = sprite_kill_list
        self.MINSURF = pygame.Surface((60, 50))
        self.MINSURF = pygame.image.load("entities\enemy_minion.jpg")
        MINSURF = self.MINSURF

    def pos_change(self):
        self.pos = (self.pos[0] - 4, self.pos[1])
        pos = self.pos
        if self.pos[0] < -60:
            self.sprite_kill_list.append(self.index_num)

    def index_update(self, indexnum):
        self.index_num = indexnum



class strikerTestClass(object):
    def __init__(self, pos, indexnum, sprite_kill_list, hp=40):
        self.pos = pos
        self.index_num = indexnum
        self.hp = hp
        self.sprite_kill_list = sprite_kill_list
        self.pixel_frac_balance = 1
        self.STRISURF = pygame.Surface((90, 75))
        self.STRISURF = pygame.image.load("entities\enemy_striker.jpg")
        STRISURF = self.STRISURF

    def pos_change(self):
        self.pixel_scroll_num = 2
        if self.pixel_frac_balance == 3:
            self.pixel_scroll_num = 1
            self.pixel_frac_balance = 1
        else:
            self.pixel_frac_balance += 1
        self.pos = (self.pos[0] - self.pixel_scroll_num, self.pos[1])
        pos = self.pos
        if self.pos[0] < -75:
            self.sprite_kill_list.append(self.index_num)
        
    def index_update(self, indexnum):
        self.index_num = indexnum



class turretTestClass(object):
    def __init__(self, pos, indexnum, sprite_kill_list, torf, hp=20):
        self.pos = pos
        self.index_num = indexnum
        self.sprite_kill_list = sprite_kill_list
        self.hp = hp
        self.torf = torf
        self.pixel_frac_balance = 1
        self.scrolled_amount = 0
        self.DRAWDISTANCE = pos[0]
        self.TURSURF = pygame.Surface((60, 50))
        self.TURSURF = pygame.image.load("entities\enemy_turret.jpg")
        TURSURF = self.TURSURF

    def pos_change(self):
        if self.torf == 1:
            self.pixel_scroll_num = 2
            if self.pixel_frac_balance == 3:
                self.pixel_scroll_num = 3
                self.pixel_frac_balance = 1
            else:
                self.pixel_frac_balance += 1
            # Balances out the cut off 0.33 pixel lost in a scroll rate of
            # 140 / 60 (2.33 pixels) per frame speed. If scroll speed is
            # adjusted, this part will need to be tweaked slightly.
            self.scrolled_amount += self.pixel_scroll_num
            self.pos = (self.DRAWDISTANCE - self.scrolled_amount, self.pos[1])
            pos = self.pos

        if self.torf == 2:
            self.pixel_scroll_num = 3
            if self.pixel_frac_balance == 4:
                self.pixel_scroll_num = 4
                self.pixel_frac_balance = 1
            else:
                self.pixel_frac_balance += 1
            self.scrolled_amount += self.pixel_scroll_num
            self.pos = (self.DRAWDISTANCE - self.scrolled_amount, self.pos[1])
            pos = self.pos
        if self.pos[0] < -60:
            self.sprite_kill_list.append(self.index_num)

    def index_update(self, indexnum):
        self.index_num = indexnum



class asteroidTestClass(object):
    def __init__(self, pos, DISPLAYHEIGHT, hp=60):
        self.pos = pos
        self.hp = hp
        self.DISPLAYHEIGHT = DISPLAYHEIGHT
        self.ASTSURF = pygame.Surface((210, 210))
        self.ASTSURF = pygame.image.load("entities\enemy_asteroid.jpg")
        ASTSURF = self.ASTSURF
        pos = self.pos

    def pos_change(self):
        self.pos = (self.pos[0] - 5, self.pos[1])
        pos = self.pos
        if self.pos[0] < -210:
            newx = randint(8, 12) * 300
            newy = randint(70, self.DISPLAYHEIGHT - 280)
            self.pos = (newx, newy)
            pos = self.pos



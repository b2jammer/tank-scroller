## enemy_generation.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *
from random import randint
from enemyTestClasses import minionTestClass, strikerTestClass, turretTestClass

pygame.init()

## minion_gen(minion_list, minion_kill_list, DISPLAYWIDTH, DISPLAYHEIGHT)

def minion_gen(minion_list, minion_kill_list, DISPLAYWIDTH, DISPLAYHEIGHT):
    wing_temp = randint(3, 5)
    wing_vert = wing_temp * (DISPLAYHEIGHT//9)
    wing_y_top = randint(0, DISPLAYHEIGHT - (wing_vert + 20))
    wing_y_bot = wing_y_top + wing_vert
    for x in range(wing_temp):
        minion_list.append(0)
        minion_list[len(minion_list) - 1] = minionTestClass((DISPLAYWIDTH * 1.1, (x * DISPLAYHEIGHT//9) + wing_y_top),len(minion_list), minion_kill_list)


## striker_gen(striker_list, striker_kill_list, DISPLAYWIDTH, DISPLAYHEIGHT)

def striker_gen(striker_list, striker_kill_list, DISPLAYWIDTH, DISPLAYHEIGHT):
    striker_y_max = DISPLAYHEIGHT - 100
    striker_y = randint(0, striker_y_max)
    striker_list.append(0)
    striker_list[len(striker_list)] = strikerTestClass((DISPLAYWIDTH * 1.1, striker_y), len(striker_list), striker_kill_list)


## turret_gen(turret_list, striker_kill_list, temp_row, lvl_type_choice)

def turret_gen(turret_list, turret_kill_list, tile_row, torf):

    row_assigned = 0
    if tile_row == 6 and row_assigned == 0:
        row = 0
        row_assigned = 1
    elif tile_row == 5 and row_assigned == 0:
        row = 1
        row_assigned = 1
    elif tile_row == 4 and row_assigned == 0:
        row = 2
        row_assigned = 1
    elif tile_row == 3 and row_assigned == 0:
        row = 3
        row_assigned = 1
    elif tile_row == 2 and row_assigned == 0:
        row = 4
        row_assigned = 1
    elif tile_row == 1 and row_assigned == 0:
        row = 5
        row_assigned = 1
    turret_list.append(0)
    turret_list[len(turret_list) - 1] = turretTestClass((1410, (row * 140) - 50), len(turret_list) - 1, turret_kill_list, torf)
    turret_list.append(0)
    turret_list[len(turret_list) - 1] = turretTestClass((1480, (row * 140) - 50), len(turret_list) - 1, turret_kill_list, torf)


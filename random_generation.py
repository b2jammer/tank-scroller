## random_generation.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *
from random import randint

def level_start():
    past_row = 1
    prev_row = 1
    if t_or_f_level == 1:
        temp_row = tile_gen_tank(past_row, prev_row, cur_row)
    if t_or_f_level == 2:
        temp_row = tile_gen_fight(past_row, prev_row, cur_row)
    cur_row = temp_row
    start_tile11 = tileFactory(scroll_speed, t_or_f_level, temp_row)

    

def tile_gen_tank(past_row, prev_row, cur_row):
    
    temp_row = randint(1, 6)
    if cur_row == 5:
        if (cur_row - 3) >= prev_row:
            if prev_row == 1:
                temp_row = randint(1, 2)
                return temp_row
            if prev_row == 2:
                temp_row = randint(1, 3)
                return temp_row
        elif prev_row == 4:
            temp_row = 3
            return temp_row
        elif prev_row == 3:
            temp_row = randint(1, 2)
            return temp_row
        else:
            temp_row = randint(1, 3)
            return temp_row
            
    if cur_row == 6:
        if prev_row == 1:
            temp_row = randint(1, 3)
            return temp_row
        elif prev_row == 5:
            temp_row = 1
            return temp_row
        else:
            temp_row = randint(1, 4)
            return temp_row
        
    if (cur_row - 3) >= prev_row:
        if prev_row == 1:
            temp_row = randint(1, 2)
            return temp_row
        if prev_row == 2:
            temp_row = randint(1, 3)
            return temp_row

    if (cur_row + 3) <= prev_row:
        if cur_row == 1:
            temp_row = 1
            return temp_row
        temp_row = randint(1, cur_row)
        return temp_row
        
    if prev_row == cur_row:
        if cur_row == 1:
            temp_row = randint(2, 6)
            return temp_row
        if cur_row == 2:
            balance = randint(1, 5)
            if balance == 1:
                temp_row = 1
                return temp_row
            if balance > 1:
                temp_row = randint(3, 6)
                return temp_row

                    
    temp_row = randint(1, 6)
    if temp_row == (cur_row + 1):
        if cur_row == 4:
            temp_row = randint(1, 4)
            return temp_row
        else:
            temp_row = randint(1, 3)
            return temp_row
    return temp_row


def tile_gen_fight(past_row, prev_row, cur_row):

    temp_row = randint(1, 6)
    return temp_row




    

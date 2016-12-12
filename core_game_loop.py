## core_game_loop.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

## Issue 1: Mobs need to be given their own surface, as f

import pygame, sys
from pygame.locals import *
from random import randint
from random_generation import tile_gen_tank, tile_gen_fight
from tileFactory import tileFactory
from level_end import level_end

BLACK = (0, 0, 0)
LEVEL_LENGTH_CONTROL = 20
## Seconds in the level + 10 in preparation for level_end.py.


def core_game_loop(DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT):

    ranlevel = randint(1, 2)
    if ranlevel == 1:
        lvl_type_choice = "t"
    if ranlevel == 2:
        lvl_type_choice = "f"

    if lvl_type_choice == "t":
        t_or_f_level = 1
        scroll_speed = 140
    if lvl_type_choice == "f":
        t_or_f_level = 2
        scroll_speed = 210

    tile_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    minion_list = []
    striker_list = []
    turret_list = []

    wait_control = 0
    level_end_in = LEVEL_LENGTH_CONTROL * 60
    
    tile_make_in = 0
    minions_make_in = 0
    striker_make_in = 0
    turret_make_in = 0
    
    minions_killed = 0
    strikers_killed = 0
    turrets_killed = 0
    asteroids_killed = 0
    
    if lvl_type_choice == "t":
        tile_make_in_max = 60
        tile_list_clear_max = 600
    if lvl_type_choice == "f":
        tile_make_in_max = 43
        tile_list_clear_max = 430
        ## For some reason this is the number needed to make the tiles line up.
    tile_num = 11
    print(lvl_type_choice)
    
    start_tile1 = tileFactory(scroll_speed, t_or_f_level, 1, 0)
    start_tile2 = tileFactory(scroll_speed, t_or_f_level, 1, 140)
    start_tile3 = tileFactory(scroll_speed, t_or_f_level, 1, 280)
    start_tile4 = tileFactory(scroll_speed, t_or_f_level, 1, 420)
    start_tile5 = tileFactory(scroll_speed, t_or_f_level, 1, 560)
    start_tile6 = tileFactory(scroll_speed, t_or_f_level, 1, 700)
    start_tile7 = tileFactory(scroll_speed, t_or_f_level, 1, 840)
    start_tile8 = tileFactory(scroll_speed, t_or_f_level, 1, 980)
    start_tile9 = tileFactory(scroll_speed, t_or_f_level, 1, 1120)
    start_tile10 = tileFactory(scroll_speed, t_or_f_level, 1, 1260)
    
    past_row = 1
    prev_row = 1
    cur_row = 1
    if t_or_f_level == 1:
        temp_row = tile_gen_tank(past_row, prev_row, cur_row)
    if t_or_f_level == 2:
        temp_row = tile_gen_fight(past_row, prev_row, cur_row)
    cur_row = temp_row
    start_tile11 = tileFactory(scroll_speed, t_or_f_level, temp_row)

    tile_list[0] = start_tile1
    tile_list[1] = start_tile2
    tile_list[2] = start_tile3
    tile_list[3] = start_tile4
    tile_list[4] = start_tile5
    tile_list[5] = start_tile6
    tile_list[6] = start_tile7
    tile_list[7] = start_tile8
    tile_list[8] = start_tile9
    tile_list[9] = start_tile10
    tile_list[10] = start_tile11
##    HUD_time_display = HUD(DISPLAYSURF, level_end_in)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if wait_control == 0 or wait_control == 1:
            pygame.time.wait(17)
            wait_control += 1
        else:
            pygame.time.wait(16)
            wait_control = 0

        if tile_make_in == tile_make_in_max:
            if level_end_in <= 600 and lvl_type_choice == "t":
                tile_list.append(0)
                tile_list[tile_num] = tileFactory(scroll_speed, t_or_f_level, 1)
                temp_list = []
                for index in range(len(tile_list) - 1):
                    temp_list.append(tile_list[index + 1])
                tile_list = temp_list
                tile_make_in = 0
            ## Tells the loop to generate tiles only on row 1 as the level will
            ## end in ten seconds.
            elif level_end_in > 600:
                if t_or_f_level == 1:
                    temp_row = tile_gen_tank(past_row, prev_row, cur_row)
                if t_or_f_level == 2:
                    temp_row = tile_gen_fight(past_row, prev_row, cur_row)
                past_row = prev_row
                prev_row = cur_row
                cur_row = temp_row
                tile_list.append(0)
                tile_list[tile_num] = tileFactory(scroll_speed, t_or_f_level, temp_row)
                temp_list = []
                for index in range(len(tile_list) - 1):
                    temp_list.append(tile_list[index + 1])
                    ## Change "index + 1" into "len(tile_list) - 1" for a
                    ## hilarious bug.
                tile_list = temp_list
                tile_make_in = 0
            elif level_end_in <= 600 and lvl_type_choice == "f":
                temp_list = []
                for index in range(len(tile_list) - 1):
                    temp_list.append(tile_list[index + 1])
            ## Tells the loop to stop generating tiles if it's a fighter level,
            ## since the level will end in ten seconds.
    
        tile_make_in += 1
        level_end_in -= 1

##        for index in minion_kill_list:
####            DISPLAYSURF.blit(minion_list[index].surf, (DISPLAYWIDTH + 1, DISPLAYHEIGHT + 1))
##            minion_list[index] = 0
##        minion_kill_list = []
##        for index in striker_kill_list:
####            DISPLAYSURF.blit(striker_list[index].surf, (DISPLAYWIDTH + 1, DISPLAYHEIGHT + 1))
##            striker_list[index] = 0
##        striker_kill_list = []
##        for index in turret_kill_list:
####            DISPLAYSURF.blit(turret_list[index].surf, (DISPLAYWIDTH + 1, DISPLAYHEIGHT + 1))
##            turret_list[index] = 0
##        turret_kill_list = []
        ## Removes a sprite class from their sprite list at the index stored in
        ## their kill list (which should always be accurate at this point) and
        ## replaces it with a 0. (Does not directly remove them from the list
        ## as that would make the rest of the indicies in the kill list
        ## inaccurate due to list length being changed.)
        ## 
        ## The DISPLAYSURF.blit is strictly for moving them offscreen first
        ## so they don't remain and interact with other entites. Will not work
        ## at this moment.

##        for minion in minion_list:
##            minion.update()
##        for striker in striker_list:
##            striker.update()
##        for turret in turret_list:
##            turret.update()
            
        for tile in tile_list:
            tile.pos_change()
        DISPLAYSURF.fill(BLACK)
        for tile in tile_list:
            DISPLAYSURF.blit(tile.TILESURF, tile.pos)
##        HUD_time_display.timer_display(level_end_in)

        if level_end_in == 0:
            level_end(DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT, tile_list, lvl_type_choice, minions_killed, strikers_killed, turrets_killed, asteroids_killed)
            
        pygame.display.update()




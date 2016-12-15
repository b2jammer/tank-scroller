## core_game_loop.py
## Andrew Herrera and Benjamin Rose
## Fall 2016



import pygame, sys
from pygame.locals import *
from random import randint
from random_generation import tile_gen_tank, tile_gen_fight
from tileFactory import tileFactory
from level_end import level_end
from enemy_generation import minion_gen, striker_gen, turret_gen
from enemyTestClasses import asteroidTestClass
from HUD import HUD

BLACK = (0, 0, 0)
LEVEL_LENGTH_CONTROL = 130
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

    minion_kill_list = []
    striker_kill_list = []
    turret_kill_list = []

    wait_control = 0
    calc_control = 1
    level_end_in = LEVEL_LENGTH_CONTROL * 60
    
    tile_make_in = 0
    minion_make_in = 0
    striker_make_in = 0
    turret_make_in = 0
    asteroid_make_in = 0

    minion_make_in_max = 5 * 60
    striker_make_in_max = 3 * 60
    turret_make_in_max = 4 * 60
    
    minions_killed = 0
    strikers_killed = 0
    turrets_killed = 0
    asteroids_killed = 0
    
    if lvl_type_choice == "t":
        tile_make_in_max = 60
        tile_list_clear_max = 600
        pcmaxhp = 150
        pccurhp = 150
    if lvl_type_choice == "f":
        tile_make_in_max = 43
        tile_list_clear_max = 430
        ## For some reason this is the number needed to make the tiles line up.
        pcmaxhp = 80
        pccurhp = 80
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

    timer_font = pygame.font.Font("Fixedsys.ttf", 30)
    
    HUD_display = HUD(DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT, timer_font, pcmaxhp)
    great_asteroid = asteroidTestClass((randint(8, 12) * 300, randint(70, 440)), DISPLAYHEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if wait_control == 0 or wait_control == 1:
            wait_amount = 17
            wait_control += 1
        else:
            wait_amount = 16
            wait_control = 0

        if calc_control == 1 or calc_control == 2 or calc_control == 3:
            wait_amount = wait_amount - 4
        if calc_control == 4: 
            wait_amount = wait_amount - 3
        if calc_control == 5:
            wait_amount = wait_amount - 3
            calc_control = 0

        pygame.time.wait(wait_amount)
        calc_control += 1

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
                if turret_make_in >= turret_make_in_max and level_end_in > 600:
                    turret_gen(turret_list, turret_kill_list, temp_row, t_or_f_level)
                    turret_make_in = 0
            elif level_end_in <= 600 and lvl_type_choice == "f":
                temp_list = []
                for index in range(len(tile_list) - 1):
                    temp_list.append(tile_list[index + 1])
            ## Tells the loop to stop generating tiles if it's a fighter level,
            ## since the level will end in ten seconds.


        if minion_make_in == minion_make_in_max and level_end_in > 600:
            minion_gen(minion_list, minion_kill_list, DISPLAYWIDTH, DISPLAYHEIGHT)
            minion_make_in = 0
        if striker_make_in == striker_make_in_max and level_end_in > 600:
            striker_gen(striker_list, striker_kill_list, DISPLAYWIDTH, DISPLAYHEIGHT)
            striker_make_in = 0

        ## Generate enemies here and supply classes with their indicies.
    
        tile_make_in += 1
        minion_make_in += 1
        striker_make_in += 1
        turret_make_in += 1
        level_end_in -= 1

        if len(minion_list) > 0:
            for x in range(len(minion_list)):
                minion_list[x].index_update(x)
                minion_list[x].pos_change()
        if len(striker_list) > 0:
            for x in range(len(striker_list)):
                striker_list[x].index_update(x)
                striker_list[x].pos_change()
        if len(turret_list) > 0:
            for x in range(len(turret_list)):
                turret_list[x].index_update(x)
                turret_list[x].pos_change()
        great_asteroid.pos_change()


        ## check for collision and enemy death here

        if len(minion_kill_list) > 0:
            for index in minion_kill_list:
                DISPLAYSURF.blit(minion_list[index].MINSURF, (DISPLAYWIDTH + 1, DISPLAYHEIGHT + 1))
                minion_list[index] = 0
            minion_kill_list = []

        if len(striker_kill_list) > 0:
            for index in striker_kill_list:
                DISPLAYSURF.blit(striker_list[index].STRISURF, (DISPLAYWIDTH + 1, DISPLAYHEIGHT + 1))
                striker_list[index] = 0
            striker_kill_list = []

        if len(turret_kill_list) > 0:
            for index in turret_kill_list:
                DISPLAYSURF.blit(turret_list[index].TURSURF, (DISPLAYWIDTH + 1, DISPLAYHEIGHT + 1))
                turret_list[index] = 0
            turret_kill_list = []
            
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

        if 0 in minion_list:
            temp_list = []
            for x in range(len(minion_list)):
                if not minion_list[x] == 0:
                    temp_list.append(minion_list[x])
            minion_list = temp_list
            for x in range(len(minion_list)):
                minion_list[x].index_update(x)

        if 0 in striker_list:
            temp_list = []
            for x in range(len(striker_list)):
                if not striker_list[x] == 0:
                    temp_list.append(striker_list[x])
            striker_list = temp_list
            for x in range(len(striker_list)):
                striker_list[x].index_update(x)

        if 0 in turret_list:
            temp_list = []
            for x in range(len(turret_list)):
                if not turret_list[x] == 0:
                    temp_list.append(turret_list[x])
            turret_list = temp_list
            for x in range(len(turret_list)):
                turret_list[x].index_update(x)
            
        for tile in tile_list:
            tile.pos_change()
        DISPLAYSURF.fill(BLACK)
        for tile in tile_list:
            DISPLAYSURF.blit(tile.TILESURF, tile.pos)
        for minion in minion_list:
            DISPLAYSURF.blit(minion.MINSURF, minion.pos)
        for striker in striker_list:
            DISPLAYSURF.blit(striker.STRISURF, striker.pos)
        for turret in turret_list:
            DISPLAYSURF.blit(turret.TURSURF, turret.pos)
        DISPLAYSURF.blit(great_asteroid.ASTSURF, great_asteroid.pos)
        HUD_display.timer_display(level_end_in)
        HUD_display.health_display(pccurhp)

        if level_end_in%60 == 0:
            if pccurhp > 0:
                pccurhp -= 1

        if level_end_in == 0:
            level_end(DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT, tile_list, lvl_type_choice, minions_killed, strikers_killed, turrets_killed, asteroids_killed)
            
        pygame.display.update()




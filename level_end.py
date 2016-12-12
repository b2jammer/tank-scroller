## level_end.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *
from tileFactory import tileFactory
from menuLineG import menuLineG

pygame.init()

BLACK = (0, 0, 0)

def level_end(DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT, tile_list, lvl_type_choice, minions_killed, strikers_killed, turrets_killed, asteroids_killed):
    DISPLAYSURF.fill(BLACK)
    tile_list = []
    lines_shown = []
    level_end_end_in = 6 * 60
    wait_control = 0
    ## The seconds of the level ending.
    if lvl_type_choice == "t":
        for x in range(10):
            tile_list.append(0)
            tile_list[x] = tileFactory(140, 1, 1, x * 140)

    minion_text = "Minions Killed: " + str(minions_killed)
    striker_text = "Strikers Killed: " + str(strikers_killed)
    turret_text = "Turrets Killed: " + str(turrets_killed)
    asteroid_text = "Asteroids Killed: " + str(asteroids_killed)

    score = (minions_killed * 10) + (strikers_killed * 30) + (turrets_killed * 15) + (asteroids_killed * 50)
    score_text = "Score: " + str(score)
    
    level_complete_font = pygame.font.Font("Fixedsys.ttf", 40)
    level_end_font = pygame.font.Font("Fixedsys.ttf", 30)

    end_line1_pos = (int(DISPLAYWIDTH * 0.4), int(DISPLAYHEIGHT * 0.15))
    end_line2_pos = (int(DISPLAYWIDTH * 0.35), int(DISPLAYHEIGHT * 0.3))
    end_line3_pos = (int(DISPLAYWIDTH * 0.35), int(DISPLAYHEIGHT * 0.4))
    end_line4_pos = (int(DISPLAYWIDTH * 0.35), int(DISPLAYHEIGHT * 0.5))
    end_line5_pos = (int(DISPLAYWIDTH * 0.35), int(DISPLAYHEIGHT * 0.6))
    end_line6_pos = (int(DISPLAYWIDTH * 0.35), int(DISPLAYHEIGHT * 0.7))
    
    level_complete_line = menuLineG(level_complete_font, "Level Complete!", end_line1_pos)
    minions_killed_line = menuLineG(level_end_font, minion_text, end_line2_pos)
    strikers_killed_line = menuLineG(level_end_font, striker_text, end_line3_pos)
    turrets_killed_line = menuLineG(level_end_font, turret_text, end_line4_pos)
    asteroids_killed_line = menuLineG(level_end_font, asteroid_text, end_line5_pos)
    score_line = menuLineG(level_end_font, score_text, end_line6_pos)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        ## Make the player move 210 pixels/second to the right here. At this
        ## point they will also possible need to be made immune to not die.
        ## The tiles no longer move at this point so generation isn't needed.

        if wait_control == 0 or wait_control == 1:
            pygame.time.wait(17)
            wait_control += 1
        else:
            pygame.time.wait(16)
            wait_control = 0

        level_end_end_in -= 1
        if level_end_end_in == 350:
            lines_shown.append(level_complete_line)
        elif level_end_end_in == 300:
            lines_shown.append(minions_killed_line)
        elif level_end_end_in == 250:
            lines_shown.append(strikers_killed_line)
        elif level_end_end_in == 200:
            lines_shown.append(turrets_killed_line)
        elif level_end_end_in == 150:
            lines_shown.append(asteroids_killed_line)
        elif level_end_end_in == 90:
            lines_shown.append(score_line)

##        if level_end_end_in == 0:
##            pygame.quit()
##            sys.exit()

        DISPLAYSURF.fill(BLACK)
        for tile in tile_list:
            DISPLAYSURF.blit(tile.TILESURF, tile.pos)
        for line in lines_shown:
            DISPLAYSURF.blit(line.SURF, line.pos)

        pygame.display.update()

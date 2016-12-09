## menu_controls.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *
from menuLineG import menuLineG
from controlsKey import controlsKey

BLACK = (0, 0, 0)

def menu_controls(DISPLAYSURF, TITLETEXTSURF, DISPLAYWIDTH, DISPLAYHEIGHT):
    menufont6 = pygame.font.Font("OdalisqueNF.ttf", 30)
    menufont7 = pygame.font.Font("OdalisqueNf.ttf", 15)
    controls_line1 = controlsKey(menufont6, menufont6, "W", "- Press to Move Upward", DISPLAYHEIGHT, DISPLAYWIDTH)
    controls_line2 = controlsKey(menufont6, menufont6, "S", "- Press to Move Downward", DISPLAYHEIGHT, DISPLAYWIDTH)
    controls_line3 = menuLineG(menufont6, "(Tank Only - Press to Fall Quickly, Creating a Shockwave on Landing)")
    controls_line4 = menuLineG(menufont6, "Left Mouse Button - Shoot")
    controls_line5 = menuLineG(menufont6, "(Tank Only - Towards the Location of Your Cursor)")
    exit_line = menuLineG(menufont7, "Press Enter to Return to Main Menu")
    line1_pos = (DISPLAYWIDTH//4, DISPLAYHEIGHT//6 + DISPLAYHEIGHT//8)
    line2_pos = (DISPLAYWIDTH//4, DISPLAYHEIGHT//6 + DISPLAYHEIGHT//4)
    line3_pos = (DISPLAYWIDTH//4, DISPLAYHEIGHT//6 + DISPLAYHEIGHT//4 + DISPLAYHEIGHT//8)
    line4_pos = (DISPLAYWIDTH//4, DISPLAYHEIGHT//6 + DISPLAYHEIGHT//2)
    line5_pos = (DISPLAYWIDTH//4, DISPLAYHEIGHT//6 + DISPLAYHEIGHT//2 + DISPLAYHEIGHT//8)
    line6_pos = (DISPLAYWIDTH//5, DISPLAYHEIGHT - DISPLAYWIDTH//10)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[K_RETURN] == 1:
            return
        
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(TITLETEXTSURF, (180, 75))
        DISPLAYSURF.blit(controls_line1.CONTROLSSURF, line1_pos)
        DISPLAYSURF.blit(controls_line2.CONTROLSSURF, line2_pos)
        DISPLAYSURF.blit(controls_line3.SURF, line3_pos)
        DISPLAYSURF.blit(controls_line4.SURF, line4_pos)
        DISPLAYSURF.blit(controls_line5.SURF, line5_pos)
        DISPLAYSURF.blit(exit_line.SURF, line6_pos)
        pygame.display.update()

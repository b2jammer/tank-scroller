## menu_controls.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *
from menuLineG import menuLineG
from controlsKey import controlsKey

BLACK = (0, 0, 0)

def menu_controls(DISPLAYSURF, TITLETEXTSURF, DISPLAYWIDTH, DISPLAYHEIGHT):
    menufont6 = pygame.font.Font("Fixedsys.ttf", 40)
    menufont7 = pygame.font.Font("ARCADECLASSIC.ttf", 30)
    menufont8 = pygame.font.Font("Fixedsys.ttf", 30)
    controls_line1 = controlsKey(menufont6, menufont6, "W", "- Press to Move Upward", DISPLAYHEIGHT, DISPLAYWIDTH)
    controls_line2 = controlsKey(menufont6, menufont6, "S", "- Press to Move Downward", DISPLAYHEIGHT, DISPLAYWIDTH)
    controls_line3 = menuLineG(menufont8, "(Tank Only - Press to Fall Quickly, Creating")
    controls_line4 = menuLineG(menufont8, "a Shockwave on Landing)")
    controls_line5 = menuLineG(menufont8, "Left Mouse Button - Shoot")
    controls_line6 = menuLineG(menufont8, "(Tank Only - Towards the Location of Your")
    controls_line7 = menuLineG(menufont8, "Cursor)")
    exit_line = menuLineG(menufont7, "Press ESCAPE to Return to Main Menu")
    line1_pos = (DISPLAYWIDTH//4, DISPLAYHEIGHT//10 + DISPLAYHEIGHT//8)
    line2_pos = (DISPLAYWIDTH//4, DISPLAYHEIGHT//10 + DISPLAYHEIGHT//4)
    line3_pos = (DISPLAYWIDTH//4, DISPLAYHEIGHT//10 + DISPLAYHEIGHT//4 + DISPLAYHEIGHT//8)
    line4_pos = (DISPLAYWIDTH//4, 400)
    line5_pos = (DISPLAYWIDTH//4, 450)
    line6_pos = (DISPLAYWIDTH//4, 500)
    line7_pos = (DISPLAYWIDTH//4, 550)
    exit_line_pos = (DISPLAYWIDTH//3.5, DISPLAYHEIGHT - DISPLAYWIDTH//20)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[K_ESCAPE] == 1:
            return
        
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(TITLETEXTSURF, (DISPLAYWIDTH//4.8, DISPLAYHEIGHT//15))
        DISPLAYSURF.blit(controls_line1.CONTROLSSURF, line1_pos)
        DISPLAYSURF.blit(controls_line2.CONTROLSSURF, line2_pos)
        DISPLAYSURF.blit(controls_line3.SURF, line3_pos)
        DISPLAYSURF.blit(controls_line4.SURF, line4_pos)
        DISPLAYSURF.blit(controls_line5.SURF, line5_pos)
        DISPLAYSURF.blit(controls_line6.SURF, line6_pos)
        DISPLAYSURF.blit(controls_line7.SURF, line7_pos)
        DISPLAYSURF.blit(exit_line.SURF, exit_line_pos)
        pygame.display.update()

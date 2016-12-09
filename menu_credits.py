## menu_credits.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *
from menuLineG import menuLineG

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def menu_credits(DISPLAYSURF, TITLETEXTSURF, DISPLAYWIDTH, DISPLAYHEIGHT):
    menufont4 = pygame.font.Font("OdalisqueNF.ttf", 30)
    menufont5 = pygame.font.Font("OdalisqueNF.ttf", 15)
    credits_line1 = menuLineG(menufont4, "Andrew Herrera - Lead Designer,")
    credits_line2 = menuLineG(menufont4, "Lead Artist, Programmer")
    credits_line3 = menuLineG(menufont4, "Benjamin Rose - Lead Programmer,")
    credits_line4 = menuLineG(menufont4, "Lead Engineer, Designer")
    exit_line = menuLineG(menufont5, "Press Enter to Return to Main Menu")
    line1_pos = (DISPLAYWIDTH//3, DISPLAYHEIGHT//4)
    line2_pos = (DISPLAYWIDTH//3, DISPLAYHEIGHT//4 + DISPLAYHEIGHT//8)
    line3_pos = (DISPLAYWIDTH//3, DISPLAYHEIGHT//2)
    line4_pos = (DISPLAYWIDTH//3, DISPLAYHEIGHT//2 + DISPLAYHEIGHT//8)
    line5_pos = (DISPLAYWIDTH//5, DISPLAYHEIGHT - DISPLAYWIDTH//10)
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
        DISPLAYSURF.blit(credits_line1.SURF, line1_pos)
        DISPLAYSURF.blit(credits_line2.SURF, line2_pos)
        DISPLAYSURF.blit(credits_line3.SURF, line3_pos)
        DISPLAYSURF.blit(credits_line4.SURF, line4_pos)
        DISPLAYSURF.blit(exit_line.SURF, line5_pos)
        pygame.display.update()

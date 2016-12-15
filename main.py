## main.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

import pygame, sys
from pygame.locals import *
from menuLineG import menuLineG
from menu_credits import menu_credits
from menu_controls import menu_controls
from core_game_loop import core_game_loop

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
flashing_white = [255, 255, 255]

DISPLAYWIDTH = 1280
DISPLAYHEIGHT = 720
DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT), DOUBLEBUF)
pygame.display.set_caption("The Little Voxel that Could")
DISPLAYSURF.fill(BLACK)


def menu_loop(TITLETEXTSURF):
    sel_pos = 1
    DISPLAYSURF.fill(BLACK)
    menufont3 = pygame.font.Font("ARCADECLASSIC.ttf", 40)
    main_menu_line1 = menuLineG(menufont3, "Play Game")
    main_menu_line2 = menuLineG(menufont3, "Controls")
    main_menu_line3 = menuLineG(menufont3, "Credits")
    main_menu_line4 = menuLineG(menufont3, "Exit")
    line1_pos = (DISPLAYWIDTH//2.5, (DISPLAYHEIGHT//3) + (DISPLAYHEIGHT//10) + (DISPLAYHEIGHT//12))
    line2_pos = (DISPLAYWIDTH//2.5, (DISPLAYHEIGHT//3) + ((DISPLAYHEIGHT//10) * 2) + (DISPLAYHEIGHT//12))
    line3_pos = (DISPLAYWIDTH//2.5, (DISPLAYHEIGHT//3) + ((DISPLAYHEIGHT//10) * 3) + (DISPLAYHEIGHT//12))
    line4_pos = (DISPLAYWIDTH//2.5, (DISPLAYHEIGHT//3) + ((DISPLAYHEIGHT//10) * 4) + (DISPLAYHEIGHT//12))
    CURSORSURF = pygame.Surface((60, 60), flags=SRCALPHA, depth=32)
    CURSORSURF = pygame.image.load("game_cursor.jpg")
    CURSORSIZE = (30, 30)
    CURSORSURF = pygame.transform.scale(CURSORSURF, CURSORSIZE)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.wait(50)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_RETURN] == 1:
            if sel_pos == 1:
                core_game_loop(DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT)
            if sel_pos == 2:
                menu_controls(DISPLAYSURF, TITLETEXTSURF, DISPLAYWIDTH, DISPLAYHEIGHT)
            if sel_pos == 3:
                menu_credits(DISPLAYSURF, TITLETEXTSURF, DISPLAYWIDTH, DISPLAYHEIGHT)
            if sel_pos == 4:
                pygame.quit()
                sys.exit()
        if (keys_pressed[K_DOWN] + keys_pressed[K_s] + keys_pressed[K_UP] + keys_pressed[K_w]) > 1:
            pass
        elif (keys_pressed[K_DOWN] + keys_pressed[K_s] + keys_pressed[K_UP] + keys_pressed[K_w]) > 0:
            if sel_pos > 1 and (keys_pressed[K_UP] == 1 or keys_pressed[K_w]) == 1:
                sel_pos -= 1
                pygame.time.wait(50)
            elif sel_pos == 1 and (keys_pressed[K_UP] == 1 or keys_pressed[K_w]) == 1:
                sel_pos = 4
                pygame.time.wait(50)
            if sel_pos < 4 and (keys_pressed[K_DOWN] == 1 or keys_pressed[K_s]) == 1:
                sel_pos += 1
                pygame.time.wait(50)
            elif sel_pos == 4 and (keys_pressed[K_DOWN] == 1 or keys_pressed[K_s]) == 1:
                sel_pos = 1
                pygame.time.wait(50)
##            while keys_pressed[K_DOWN] == 1 or keys_pressed[K_s] == 1 or keys_pressed[K_UP] == 1 or keys_pressed[K_w] == 1:
##                while True:
##                    for event in pygame.event.get():
##                        if event.type == QUIT:
##                            pygame.quit()
##                            sys.exit()
##                keys_pressed = pygame.key.get_pressed()
##                pygame.display.update()
        if sel_pos == 1:
            sel_cursor_pos = ((DISPLAYWIDTH//3) + 35, (DISPLAYHEIGHT//3) + (DISPLAYHEIGHT//10) + (DISPLAYHEIGHT//12) + 5)
        elif sel_pos == 2:
            sel_cursor_pos = ((DISPLAYWIDTH//3) + 35, (DISPLAYHEIGHT//3) + ((DISPLAYHEIGHT//10) * 2) + (DISPLAYHEIGHT//12) + 5)
        elif sel_pos == 3:
            sel_cursor_pos = ((DISPLAYWIDTH//3) + 35, (DISPLAYHEIGHT//3) + ((DISPLAYHEIGHT//10) * 3) + (DISPLAYHEIGHT//12) + 5)
        elif sel_pos == 4:
            sel_cursor_pos = ((DISPLAYWIDTH//3) + 35, (DISPLAYHEIGHT//3) + ((DISPLAYHEIGHT//10) * 4) + (DISPLAYHEIGHT//12) + 5)
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(TITLETEXTSURF, (DISPLAYWIDTH//4.8, DISPLAYHEIGHT//15))
        DISPLAYSURF.blit(main_menu_line1.SURF, line1_pos)
        DISPLAYSURF.blit(main_menu_line2.SURF, line2_pos)
        DISPLAYSURF.blit(main_menu_line3.SURF, line3_pos)
        DISPLAYSURF.blit(main_menu_line4.SURF, line4_pos)
        DISPLAYSURF.blit(CURSORSURF, sel_cursor_pos)
        pygame.display.update()

class clickAnywhereG(object):
    def __init__(self, surf):
        self.SURF = surf

    def fade(self, TITLETEXTSURF, menufont1, TX1):
        menufont2 = pygame.font.Font("ARCADECLASSIC.ttf", 30)
        reappear_delay = 0
        fade = 1
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0] == 1:
                TITLETEXTSURF.fill(BLACK)
                TITLETEXTSURF = menufont1.render("The Little Vector that Could", True, WHITE, None)
                TITLETEXTSURF = pygame.transform.scale(TITLETEXTSURF, TX1)
                menu_loop(TITLETEXTSURF)
            pygame.time.wait(10)
            if flashing_white[0] > 0 and fade == 1:
                flashing_white[0] -= 5
                flashing_white[1] -= 5
                flashing_white[2] -= 5
            elif fade == 0:
                flashing_white[0] += 5
                flashing_white[1] += 5
                flashing_white[2] += 5
            else:
                if reappear_delay < 10:
                    reappear_delay += 1
                else:
                    reappear_delay = 0
                    flashing_white[0] += 5
                    flashing_white[1] += 5
                    flashing_white[2] += 5
                    fade = 0
            if flashing_white[0] == 255:
                fade = 1
              
##            TITLETEXTSURF = menuFont1.render("The Little Vector that Could", True, WHITE, None)
##            TITLETEXTSURF = pygame.transform.scale(TITLETEXTSURF, TX1)      
            FADETEXTSURF = menufont2.render("CLICK ANYWHERE TO BEGIN", True, flashing_white, None)
            TX2 = FADETEXTSURF.get_size()
            FADETEXTSURF = pygame.transform.scale(FADETEXTSURF, TX2)
            self.SURF.blit(FADETEXTSURF, (DISPLAYWIDTH//2.9, DISPLAYHEIGHT//8 * 7))
            pygame.display.update()


def main():
    menufont1 = pygame.font.Font("Fixedsys.ttf", 50)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        TITLETEXTSURF = menufont1.render("The Little Vector that Could", True, WHITE, None)
        TX1 = TITLETEXTSURF.get_size()
        TITLETEXTSURF = pygame.transform.scale(TITLETEXTSURF, TX1)
        DISPLAYSURF.blit(TITLETEXTSURF, (DISPLAYWIDTH//4.8, DISPLAYHEIGHT//15))
        fadetext = clickAnywhereG(DISPLAYSURF)
        fadetext.fade(TITLETEXTSURF, menufont1, TX1)
        

main()

















## tileFactory.py
## Andrew Herrera and Benjamin Rose
## Fall 2016

# Example of a call:
# temp_row = randint(1,6)
# tile1 = tileFactory(140, 1, temp_row)
# tiles_list.append(tile1)
# possible "tile" + str(tile_count) = tileFactory(140, 1, temp_row)

import pygame, sys
from pygame.locals import *
from random import randint

BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((1280, 720))
DISPLAYSURF.fill(BLACK)


class tileFactory(object):
    def __init__(self, scrollspeed, tankorfighterlevel, tilerow):
        self.scroll = scrollspeed
        self.torf = tankorfighterlevel
        self.scrolled_amount = 0
        self.pixel_frac_balance = 1
        row_assigned = 0
        TILESIZE = 140
        self.DRAWDISTANCE = 2000
        # If there are performance problems, lowering the draw distance
        # should help. But it should never go below DISPLAYHEIGHT + 140.
        
        if tilerow == 6 and row_assigned == 0:
            self.row = 0
            row_assigned = 1
        # It's easier to think about the tile rows as going from row 1, the
        # lowest, to row 6, the highest, calculations are easier if it goes
        # from 0 being the top row to 5 being the bottom row. This part allows
        # the input to be the easier-to-think about one and then simply
        # changes the row value to the one far more convenient for in-code
        # uses.
        elif tilerow == 5 and row_assigned == 0:
            self.row = 1
            row_assigned = 1
        elif tilerow == 4 and row_assigned == 0:
            self.row = 2
            row_assigned = 1
        elif tilerow == 3 and row_assigned == 0:
            self.row = 3
            row_assigned = 1
        elif tilerow == 2 and row_assigned == 0:
            self.row = 4
            row_assigned = 1
        elif tilerow == 1 and row_assigned == 0:
            self.row = 5
            row_assigned = 1

        self.pos = (self.DRAWDISTANCE, int(self.row * TILESIZE))

        self.TILESURF = pygame.Surface((TILESIZE, TILESIZE))
        self.TILESURF = pygame.image.load("tile.png")
        self.TILESURF = pygame.transform.scale(self.TILESURF, (TILESIZE, TILESIZE))
        TILESURF = self.TILESURF

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
            pass
        # Will be written once fighter scroll speed is determined.

def main():
    tile_list = []
##    tile1 = tileFactory(140, 1, 1)
##    tile_list.append(tile1)
    t = 0
    tile_make_in = 0
    tm = [0, 0, 0, 0, 0]
##    
##    for x in range(5):
##        temp_row = randint(1, 6)
##        tile_list[x] = tileFactory(140, 1, temp_row)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.time.wait(17)
        t += 1

        if tile_make_in == 61:
            temp_row = randint(1, 6)
            for x in range(1):
                tile_list[x] = tileFactory(140, 1, temp_row)
                tile_make_in = 0
    
        tile_make_in += 1

##        if t >= 60 and t < 120 and tm[0] == 0:
##            tile2 = tileFactory(140, 1, 2)
##            tile_list.append(tile2)
##            tm[0] = 1
##        elif t >= 120 and t < 180 and tm[1] == 0:
##            tile3 = tileFactory(140, 1, 3)
##            tile_list.append(tile3)
##            tm[1] = 1
##        elif t >= 180 and t < 240 and tm[2] == 0:
##            tile4 = tileFactory(140, 1, 4)
##            tile_list.append(tile4)
##            tm[2] = 1
##        elif t >= 240 and t < 300 and tm[3] == 0:
##            tile5 = tileFactory(140, 1, 5)
##            tile_list.append(tile5)
##            tm[3] = 1
##        elif t >= 300 and tm[4] == 0:
##            tile6 = tileFactory(140, 1, 6)
##            tile_list.append(tile6)
##            tm[4] = 1
            
        
        for tile in tile_list:
            tile.pos_change()
        DISPLAYSURF.fill(BLACK)
        for tile in tile_list:
            DISPLAYSURF.blit(tile.TILESURF, tile.pos)
            
        pygame.display.update()

main()

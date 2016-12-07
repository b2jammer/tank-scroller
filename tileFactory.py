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

class tileFactory(object):
    def __init__(self, scrollspeed, tankorfighterlevel, tilerow):
        self.scroll = scrollspeed
        self.torf = tankorfighterlevel
        self.scrolled_amount = 0
        self.pixel_frac_balance = 1
        row_assigned = 0
        TILESIZE = 140
        DRAWDISTANCE = 2000
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

        self.pos = (DRAWDISTANCE, int(self.row * TILESIZE))

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
            self.pos = (DRAWDISTANCE - self.scrolled_amount, self.pos[1])

        if self.torf == 2:
            pass
        # Will be written once fighter scroll speed is determined.















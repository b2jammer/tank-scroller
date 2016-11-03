import pygame,sys
from pygame.locals import *

# A list of all tile names. Not actually used for anything (perhaps
# besides sanity checking).
TILENAMES = ('air','concrete')
# A dictionary that connects each tilename to a list of its variant images.
# Variants will be drawn at random to make the grid pattern less obvious.
#(using a fixed seed so the map doesn't flicker)
VARIANTS = {'air':None,'concrete':('0.png','1.png')}

# A map of tiles. Use this for a level.
# A level will be stored as a dictionary of tuples to tilename strings. When
# retreiving a 
class tile_map(object):
    def __init__(self,tile_dict):
        self.tiles = tile_dict
        
    def get_tile(self,pos):
        if pos in tile_dict:
            return tile_dict[pos]
        else:
            return 'air'

    def x_bounds(self):
        poslist = list(self.tiles.keys())
        xlist = [item[0] for item in poslist]
        return (min(xlist),max(xlist))
    
    def y_bounds(self):
        poslist = list(self.tiles.keys())
        ylist = [item[1] for item in poslist]
        return (min(ylist),max(ylist))

    def width(self):
        xb = self.x_bounds()
        return xb[1]-xb[0]

    def height(self):
        yb = self.y_bounds()
        return yb[1]-yb[0]
    
    # Draw a portion of the tile map from one corner to the other.
    def draw_map(self,top_left,low_right):
        

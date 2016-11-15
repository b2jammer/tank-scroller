## vectors.py
## BENROSE
## 10NOV2016

from math import *

#2D vector factory
class Vector2D(object):
    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        self.vector = (self.x,self.y)

    def __str__(self):
        return str(self.vector)

    def __add__(self,right):
        return (self.x+right.x,self.y+right.y)

    def __sub__(self,right):
        return (self.x-right.x,self.y-right.y)

    def __neg__(self):
        return (-self.x,-self.y)

    def __mul__(self,scale):
        return (self.x*scale,self.y*scale)

    def length(self):
        return sqrt((self.x**2)+(self.y**2))
    def normalized(self):
        mag = self.length()
        X = self.x/mag
        Y = self.y/mag
        return Vector2D(X,Y)
    def dot(self,right):
        return ((self.x*right.x)+(self.y*right.y))
    def cross(self,right):
        return (self.x*right.y - self.y*right.x)
    def rotate(self,theta):
        rad = radians(theta)
        X = (self.x * cos(rad) - self.y * sin(rad))
        Y = self.x * sin(rad) + self.y * cos(rad)
        return Vector2D(X,Y)

    @staticmethod
    def from_points(P1,P2):

        return Vector2D(P2[0]-P1[0],P2[1]-P1[1])

#j-kawa
import math

class Bullet :
    def __init__(self,x=0,y=0,size=1,radian=0,v=10,damage=5):
        self.x = x
        self.y = y
        self.size = size
        self.rad = rad
        self.v = v
        self.damage = damage
        self.dx = math.round(math.cos(rad)*v)
        self.dy = math.round(marh.sin(rad)*v)
    def move() :
        self.x += self.dx
        self.y += self.dy

    ##-----------------------------------------------------
#if __name__ == '__main__':
#    print("sucsess")

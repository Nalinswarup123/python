#wap to create circle class and compute area and perimeter
import math

class circle:
    def __init__(self,r):
        self.a=(math.pi)*(r)*(r)
        self.p=2*(math.pi)*(r)
        print('area=',self.a)
        print('perimeter=',self.p)
o=circle(int(input('enter radius')))

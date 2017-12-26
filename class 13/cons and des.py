class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self,z=5):
        #class_name = self__class__name__
        print('x=',self.x,'y=',self.y)
        print(z)
pt1=point(1,2)
pt2=pt1
print(id(pt1))
print(id(pt2))
del pt1,pt2
#del pt2


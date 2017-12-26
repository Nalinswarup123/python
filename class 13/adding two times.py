class time:
    def __init__(self):
        self.h=int(input('enter hr:'))
        self.m=int(input('enter min:'))
        self.s=int(input('enter sec:'))
    def output(self,o,o1):
        x,y,z=0,0,0
        z=o.s+o1.s
        y=z//60
        z=z%60
        y=o.m+o1.m+y
        x=y//60
        y=y%60
        x=o.h+o1.h+x
        print(o.h,o.m,o.s)
        print(o1.h,o1.m,o1.s)
        print(x,y,z)

obj=time()
obj1=time()
obj.output(obj,obj1)

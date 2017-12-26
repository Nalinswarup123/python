class a():
    def foo(self):
        print('a')
class b(a):
    def foo(self):
        print('b')
        #super(b,self).foo()
class c(a):
    def foo(self):
        print('c')
        super(c,self).foo()
class d(b,c):
    def foo(self):
        print('d')
        super(d,self).foo()
D=d()
D.foo()


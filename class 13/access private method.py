#how to access a private method

class p:
    def __init__(self,name,alias):
        self.name=name
        self.__alias=alias
    def who(self):
        print('name:',self.name)
        print('alias:',self.__alias)
    def __foo(self):
        print('this is private method')
    def foo(self):
        print('this is pubilc method')
        self.__foo()
x=p('aditya','adi')
x._p__foo()
x.foo()
print(x._p__alias)

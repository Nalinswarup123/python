class parent:
    parentattr=100
    def __init__(self):
        print('calling parent constructor')
    def parentmethod(self):
        print('calling parent method')
        self.__s=10
        print(self.__s)
    def setattr(self,attr):
        parent.parentattr=attr
    def getattr(self):
        print('parent attribute :',parent.parentattr)

class child(parent):
    def __init__(self):
        print('calling child constructor')
    def childmethod(self):
        print('calling child method')

c=child()
#p=parent()
c.childmethod()
c.parentmethod()
c.setattr(200)
c.getattr()


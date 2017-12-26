'''to override a method the method must be defined in subclass using
the same method as in its super class.
it is necessary for the sub class to modify the implementation of the method 
defined in the super class'''
class parent:
    def mymethod(self):
        print('calling parent method')

class child(parent):
    def mymethod(self):
        print('calling child method')
        super(child,self).mymethod()

c=child()
c.mymethod()

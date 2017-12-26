from tkinter import *
class abc:
    def __init__(self):
        window=Tk()
        b1=Button(window,text='ok',fg='blue',command=self.fun1)
        b2=Button(window,text='click',fg='red',command=self.fun2)
        b1.pack()
        b2.pack()
        window.mainloop()
    def fun1(self):
        print('clicked ok button')
    def fun2(self):
        print('clicked cancel button')
abc()

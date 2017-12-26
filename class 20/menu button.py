from tkinter import *
top=Tk()
mb=Menubutton(top,text='cricketers',relief=RAISED)
mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb['menu']=mb.menu
x=IntVar()
y=IntVar()
mb.menu.add_checkbutton(label='sachin',variable=x)
mb.menu.add_checkbutton(label='Virat',variable=y)
mb.pack()
top.mainloop()

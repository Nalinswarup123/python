from tkinter import * 
from tkinter import messagebox
top=Tk()
c=Canvas(top,bg='blue',height=250,width=300)
coord=100,10,1000,1000
arc=c.create_arc(coord,start=0,extend=150,fill='red')
c.pack()
top.mainloop()

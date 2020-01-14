import tkinter
import sys
from random import randrange
def n(event):
    global t
    c.delete(t)
    t=c.create_text(20,20,text=str(randrange(1,119)),font='Arial')
def q(event):
    q()
t=tkinter.Tk()
f=tkinter.Frame(t)
f.pack(side=tkinter.TOP)
c=tkinter.Canvas(t,width=400,height=500,bg='#ffffff')
c.pack(side=tkinter.LEFT)
sub=tkinter.Button(f,text='Submit')
sub.pack(side=tkinter.LEFT)
vans=tkinter.Button(f,text='View answer')
vans.pack(side=tkinter.LEFT)
q=tkinter.Button(f,text='Quit')
q.pack(side=tkinter.LEFT)
q.bind('<1>',)
new=tkinter.Button(f,text='New')
new.pack(side=tkinter.LEFT)
new.bind('<1>',n)
t=c.create_text(20,20,text=str(randrange(1,119)),font='Arial')

import tkinter
import sys
from random import randrange
import p
rt=dict(zip(p.ptablesym,range(1,119)))
def n(event):
    global t,pe
    c.delete(t)
    c.delete(pe)
    an=randrange(1,119)
    t=c.create_text(20,20,text=str(an),font='Arial')
    pe=c.create_text(200,250,text=p.ptablesym[an-1],font=('Arial',200))
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
an=randrange(1,119)
t=c.create_text(20,20,text=str(an),font='Arial')
pe=c.create_text(200,250,text=p.ptablesym[an-1],font=('Arial',200))

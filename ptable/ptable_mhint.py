import tkinter
from random import randrange
import p
from time import sleep
out=''
rt=dict(zip(p.ptablesym,range(1,119)))
def n(event):
    global pe,an
    c.delete(pe)
    an=randrange(1,119)
    pe=c.create_text(20,20,text=str(an),font=('Arial',20))
def ni():
    ge.config(fg='#000000')
    ge.delete('1.0',tkinter.END)
    n(None)
def qt(event):
    raise SystemExit()
def hint(i):
    if i in p.ptablesym:
        return 'That element is '+str(abs(an-1-p.ptablesym.index(i)))+' element'+('s' if abs(an-1-p.ptablesym.index(i))!=1 else '')+' away from the entered element'
    return 'That doesn\'t seem like any element in the table, please try again.'
def s(event):
    global m
    i=ge.get('1.0',tkinter.END)[:-1]
    o=i[:]
    i=i[:1].upper()+i[1:].lower()
    if len(i)!=0:
        if p.ptablesym[an-1]==o:
            ge.config(fg='#008000')
        elif p.ptablesym[an-1]==i:
            ge.config(fg='#ffff00')
        else:
            ge.config(fg='#ff0000')
            m+=1
            l.set('Mistakes:'+str(m))
            hv.set(hint(i))
            t.update()
            sleep(1)
            ge.config(fg='#000000')
            return
        hv.set('')
        t.update()
        sleep(1)
        if m>=5: raise SystemExit()
        ni()
def va(event):
    ge.delete('1.0',tkinter.END)
    ge.insert(tkinter.END,p.ptablesym[an-1])
    ge.config(fg='#ff0000')
    t.update()
    sleep(1)
    ni()
m=0
t=tkinter.Tk()
f=tkinter.Frame(t)
f.pack(side=tkinter.TOP)
hv=tkinter.StringVar()
h=tkinter.Label(t,textvariable=hv,font=('Arial',10))
h.pack()
l=tkinter.StringVar()
left=tkinter.Label(t,textvariable=l,font=('Arial',10))
l.set('Mistakes:'+str(m))
left.pack(side=tkinter.TOP)
c=tkinter.Canvas(t,width=400,height=500,bg='#ffffff')
c.pack(side=tkinter.LEFT)
sub=tkinter.Button(f,text='Submit')
sub.pack(side=tkinter.LEFT)
sub.bind('<1>',s)
vans=tkinter.Button(f,text='View answer')
vans.pack(side=tkinter.LEFT)
vans.bind('<1>',va)
q=tkinter.Button(f,text='Quit')
q.pack(side=tkinter.LEFT)
q.bind('<1>',qt)
new=tkinter.Button(f,text='New')
new.pack(side=tkinter.LEFT)
new.bind('<1>',n)
an=randrange(1,119)
ge=tkinter.Text(relief=tkinter.GROOVE,font=('Arial',150),bg='#ffffee',wrap=tkinter.NONE)
tx=c.create_window(200,250,window=ge,height=250,width=300)
pe=c.create_text(20,20,text=str(an),font=('Arial',20))
t.mainloop()

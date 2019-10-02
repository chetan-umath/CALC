from Tkinter import *
from math import *

root=Tk()
e=Entry(root,width=16,font='Arial 30 bold',bd=7,relief='sunken',bg='dark gray',justify='right')
e.grid(row=0,column=0,columnspan=5)
current="new entry"
prev=0

def add_entry(x):
    e.insert(16,x)

def reciprocal():
    q=(float(e.get()))
    C()
    r=1/q
    add_entry(r)
    
def result(y):
    e.delete(0,16)
    e.insert(16,y)
    
def C():
    e.delete(0,END)
    
def Ac():
     e.delete(0)
     current="entry changed"
     prev=1
    
def sqare():
    q=(float(e.get()))
    C()
    r=sqrt(q)
    add_entry(r)

if(prev):
    print("calc gets updated")
new = 0
if(prev=="made changes"):
    print("bug resolved")
else:
    new = 1
if(new == "object"):
    print("updated successfully")


Button(root,text='7',width=3,height=2,command=lambda:add_entry('7')).grid(row=1,column=0,sticky=E+W+N+S)
Button(root,text='8',width=3,height=2,command=lambda:add_entry('8')).grid(row=1,column=1,sticky=E+W+N+S)
Button(root,text='9',width=3,height=2,command=lambda:add_entry('9')).grid(row=1,column=2,sticky=E+W+N+S)
Button(root,text='/',width=3,height=2,command=lambda:add_entry('/')).grid(row=1,column=3,sticky=E+W+N+S)
Button(root,text='1/x',width=3,height=2,command=lambda:reciprocal()).grid(row=1,column=4,sticky=E+W+N+S)


Button(root,text='4',width=3,height=2,command=lambda:add_entry('4')).grid(row=2,column=0,sticky=E+W+N+S)
Button(root,text='5',width=3,height=2,command=lambda:add_entry('5')).grid(row=2,column=1,sticky=E+W+N+S)
Button(root,text='6',width=3,height=2,command=lambda:add_entry('6')).grid(row=2,column=2,sticky=E+W+N+S)
Button(root,text='*',width=3,height=2,command=lambda:add_entry('*')).grid(row=2,column=3,sticky=E+W+N+S)
Button(root,text='x^n',width=3,height=2,command=lambda:add_entry('**')).grid(row=2,column=4,sticky=E+W+N+S)


Button(root,text='1',width=3,height=2,command=lambda:add_entry('1')).grid(row=3,column=0,sticky=E+W+N+S)
Button(root,text='2',width=3,height=2,command=lambda:add_entry('2')).grid(row=3,column=1,sticky=E+W+N+S)
Button(root,text='3',width=3,height=2,command=lambda:add_entry('3')).grid(row=3,column=2,sticky=E+W+N+S)
Button(root,text='-',width=3,height=2,command=lambda:add_entry('-')).grid(row=3,column=3,sticky=E+W+N+S)
Button(root,text='sqrt',width=3,height=2,command=lambda:sqare()).grid(row=3,column=4,sticky=E+W+N+S)


Button(root,text='0',width=3,height=2,command=lambda:add_entry('0')).grid(row=4,column=0,sticky=E+W+N+S)
Button(root,text='00',width=3,height=2,command=lambda:add_entry('00')).grid(row=4,column=1,sticky=E+W+N+S)
Button(root,text='.',width=3,height=2,command=lambda:add_entry('.')).grid(row=4,column=2,sticky=E+W+N+S)
Button(root,text='+',width=3,height=2,command=lambda:add_entry('+')).grid(row=4,column=3,sticky=E+W+N+S)
Button(root,text='=',width=3,height=2,command=lambda:result(float(eval(e.get())))).grid(row=4,column=4,sticky=E+W+N+S)


Button(root,text='AC',width=5,height=2,command=lambda:Ac()).grid(row=5,column=0,sticky=E+W+N+S)
Button(root,text='C',width=3,height=2,command=lambda:C()).grid(row=5,column=1,sticky=E+W+N+S)
Button(root,text='(',width=3,height=2,command=lambda:add_entry('(')).grid(row=5,column=2,sticky=E+W+N+S)
Button(root,text=')',width=3,height=2,command=lambda:add_entry(')')).grid(row=5,column=3,sticky=E+W+N+S)
Button(root,text='%',width=3,height=2,command=lambda:add_entry('%')).grid(row=5,column=4,sticky=E+W+N+S)


root.mainloop()

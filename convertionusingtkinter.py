from tkinter import *
w=Tk()

def convert():
   r1.delete("1.0","end")
   v=float(x.get())*1000
   r1.insert(END,v)

def g_to_kg():
   r1.delete("1.0","end")
   v=float(x.get())/1000
   r1.insert(END,v)

def m_to_cm():
   r1.delete("1.0","end")
   v=float(x.get())/100
   r1.insert(END,v)
def cm_to_m():
   r1.delete("1.0","end")
   v=float(x.get())*100
   r1.insert(END,v)
def km_to_m():
   r1.delete("1.0","end")
   v=float(x.get())/1000
   r1.insert(END,v)
def m_to_km():
   r1.delete("1.0","end")
   v=float(x.get())*1000
   r1.insert(END,v)
def clear():
   
   x.set("")
   r1.delete("1.0","end")


w.geometry("200x200")
x=StringVar()
e1=Entry(w,textvariable=x)
e1.grid(row=0,column=0)
r1=Text(w,height=1,width=15)
r1.grid(row=1,column=0)

b1=Button(w,text="kg to g",command=convert)
b1.grid(row=2,column=0)
b2=Button(w,text="g to kg",command=g_to_kg)
b2.grid(row=2,column=1)
b3=Button(w,text="m to cm ",command=m_to_cm)
b3.grid(row=3,column=0)
b4=Button(w,text="cm to m",command=cm_to_m)
b4.grid(row=3,column=1)        
b5=Button(w,text="km to m",command=km_to_m)
b5.grid(row=4,column=0)
b6=Button(w,text="m to km",command=m_to_km)
b6.grid(row=4,column=1)        
b7=Button(w,text="clear",command=clear)
b7.grid(row=5,column=0)        

w.mainloop()

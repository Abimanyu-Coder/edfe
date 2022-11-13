from tkinter import *

root=Tk()
root.title("Dictionary")
root.geometry("600x400")
root.configure(background='yellow')

LOM = Label(root, bg='orange', fg='yellow')
LOI = Label(root, bg='orange', fg='yellow')
LOTk = Label(root, bg='orange', fg='yellow')

dictionary = {'Mutable' : 'Values can be changed just like a list',
              'Immutable' : 'Values cannot be changed just like a tuple',
              'Tkinter' : 'It is the GUI library of python'
              }

def mutable():   
    LOM["text"] = dictionary['Mutable']
    
def immutable():   
    LOI["text"] = dictionary['Immutable']
    
def tkinter():   
    LOTk["text"] = dictionary['Tkinter']
    
lom = Button(root, text="Meaning Of Mutable", command = mutable, bg='orange', fg='yellow' )
lom.place(relx=0.5, rely=0.2, anchor=CENTER)
LOM.place(relx=0.5, rely=0.3, anchor=CENTER)

loi = Button(root, text="Meaning Of Immutable", command = immutable, bg='orange', fg='yellow' )
loi.place(relx=0.5, rely=0.4, anchor=CENTER)
LOI.place(relx=0.5, rely=0.5, anchor=CENTER)

lotk = Button(root, text="Meaning Of Tkinter", command = tkinter, bg='orange', fg='yellow' )
lotk.place(relx=0.5, rely=0.6, anchor=CENTER)
LOTk.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
 
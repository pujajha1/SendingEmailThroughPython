# This is a cool Python Program to create text editor.
#you can write in the file and even save it with its name.
#its work in progress, will add some more features here.

'''Tkinter is a Python binding to the Tk GUI toolkit. 
It is the standard Python interface to the Tk GUI toolkit, 
and is Python's de facto standard GUI. '''

from Tkinter import *
import tkFileDialog
root=Tk("Text Editor")

# In able to write in the text editor
text=Text(root)
text.grid()

# In order to save the file
def saveas():
    global text 
    t = text.get("1.0", "end-1c")
    savelocation=tkFileDialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
button=Button(root, text="Save", command=saveas) 
button.grid()

root.mainloop()

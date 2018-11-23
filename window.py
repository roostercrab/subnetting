from tkinter import *

root = Tk()

the_label = Label(root, text="Please enter the IP address")
the_label.pack()

e = Entry(root)
e.pack()

e.delete(0, END)
e.insert(0, "Please enter IP address")

def removeValue(event):
    self.entry.delete(0, 'end')
    return None

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

button1 = Button(top_frame, text="Calculate Subnet", fg="red")

button1.pack(side=RIGHT)

root.mainloop()

from tkinter import *

root = Tk()

the_label = Label(root, text="Please enter the IP address")
the_label.pack()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

button1 = Button(top_frame, text="Calculate Subnet", fg="red")

button1.pack(side=RIGHT)

root.mainloop()

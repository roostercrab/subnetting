import tkinter as tk
from ipaddress import ip_address
from ip_sanity_check import check_ip
from mask_sanity_check import check_mask
from guizero import *

root = tk.Tk()

entry_label = tk.Label(root, text = "Please enter the IP address")
entry_label.grid(row = 0, column = 0)

ip_entry = tk.Entry(root)
ip_entry.grid(row = 0, column = 1)

entry_label = tk.Label(root, text = "Please enter the subnet mask")
entry_label.grid(row = 1, column = 0)

mask_entry = tk.Entry(root)
mask_entry.grid(row = 1, column = 1)

ip_text_box = tk.Text(root, width = 25, height = 2)
ip_text_box.grid(row = 2, column = 0, columnspan = 2)

mask_text_box = tk.Text(root, width = 25, height = 2)
mask_text_box.grid(row = 3, column = 0, columnspan = 2)

text_box = tk.Text(root, width = 25, height = 2)
text_box.grid(row = 4, column = 0, columnspan = 2)

text_box.insert("end-1c", "Subnet Teacher")

def ip_calc(event):
    #Get the string of the ip_entry widget
    ip = ip_entry.get() 
    ip_sanity = check_ip(ip)
    if ip_sanity == True:
        text_box.delete(1.0, "end-1c") # Clears the text box of data
        text_box.insert("end-1c", "Please enter the subnet mask") # adds text to text box
        ip_text_box.insert("end-1c", ip)
    else:
        text_box.delete(1.0, "end-1c")
        text_box.insert("end-1c", "Try again!")
        ip_entry.delete(0, "end")

def mask_calc(event):
    #Get the string of the mask_entry widget
    mask = mask_entry.get() 
    mask_sanity = check_mask(mask)
    if mask_sanity == True:
        text_box.delete(1.0, "end-1c") # Clears the text box of data
        text_box.insert("end-1c", "Cool") # adds text to text box
        mask_text_box.insert("end-1c", mask)
    else:
        text_box.delete(1.0, "end-1c")
        text_box.insert("end-1c", "Try again!")
        mask_entry.delete(0, "end")

good_ip = ip_entry.bind("<Return>", ip_calc) 

good_mask = mask_entry.bind("<Return>", mask_calc)

root.mainloop()
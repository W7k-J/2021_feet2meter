# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 23:21:42 2021

@author: w7k
@https://github.com/W7k-J

"""

from tkinter import Tk, Button, Label, DoubleVar, Entry


# create window

window = Tk()
window.title("Conversion App")
window.configure(background="light grey")
window.geometry("300x200")
window.resizable(width=False, height=False)

# functions

def convertToMeter():
    try:
        value = float(ft_entry.get())
        meter = value * 0.3048
        print(meter)
        mt_value.set("%.4f" % meter)
    except:
        print("string!")


def convertToFeet():
    try:
        value = float(mt_entry.get())
        feet = value * 3.28
        print(feet)
        ft_value.set("%.4f" % feet)
    except:
        print("string!")


def clear():
    ft_value.set("")
    mt_value.set("")


# buttons

ft_lbl = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=10)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0, padx=15)
ft_entry.delete(0, "end")


mt_lbl = Label(window, text="Meter", bg="purple", fg="white", width=14)
mt_lbl.grid(column=0, row=1)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=1, row=1, pady=10)
mt_entry.delete(0, "end")

convert_btnM = Button(window, text="Feet to Meters", bg="blue", fg="white", width=14, command=convertToMeter)
convert_btnM.grid(column=0, row=3, padx=15, pady=15)

convert_btnF = Button(window, text="Meters to Feet", bg="blue", fg="white", width=14, command=convertToFeet)
convert_btnF.grid(column=0, row=4, padx=15)


clear_btn = Button(window, text="Clear", bg="red", fg="white", width=14, command=clear)
clear_btn.grid(column=1, row=3)

window.mainloop()
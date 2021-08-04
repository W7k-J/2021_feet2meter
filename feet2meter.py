# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 23:21:42 2021

@author: w7k
@https://github.com/W7k-J

"""

from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Feet to Meter Conversion App")
window.configure(background="light green")
window.geometry("320x220")
window.resizable(width=False, height=False)

ft_lbl = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, "end")


mt_lbl = Label(window, text="Meter", bg="purple", fg="white", width=14)
mt_lbl.grid(column=0, row=1, padx=15, pady=15)

mt_value = DoubleVar()
mt_value = Entry(window, textvariable=ft_value, width=14)
mt_value.grid(column=1, row=1, pady=30)
mt_value.delete(0, "end")

convert_btn = Button(window, text="Convert", bg="blue", fg="white", width=14, command="")
convert_btn.grid(column=0, row=3, padx=15)

clear_btn = Button(window, text="Clear", bg="blue", fg="white", width=14, command="")
clear_btn.grid(column=1, row=3, padx=15)



window.mainloop()



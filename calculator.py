#Simple calculator using Tkinter
from tkinter import *

root = Tk()
root.title("Calculator")

ent = Entry(root, width = 52, borderwidth=10)
ent.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

#button functions
def button_click(number):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(number))

def button_clear():
    ent.delete(0, END)

def button_add():
    global f_num
    global operation
    first_num = ent.get()
    operation = "add"
    f_num = int(first_num)
    ent.delete(0, END)

def button_sub():
    global f_num
    global operation
    first_num = ent.get()
    operation = "sub"
    f_num = int(first_num)
    ent.delete(0, END)

def button_multiply():
    global f_num
    global operation
    first_num = ent.get()
    operation = "multiply"
    f_num = int(first_num)
    ent.delete(0, END)

def button_divide():
    global f_num
    global operation
    first_num = ent.get()
    operation = "divide"
    f_num = int(first_num)
    ent.delete(0, END)

def button_equal():
    sec_num = ent.get()
    ent.delete(0, END)
    
    if operation == "add":
        ent.insert(0, f_num + int(sec_num))
    if operation == "sub":
        ent.insert(0, f_num - int(sec_num))
    if operation == "multiply":
        ent.insert(0, f_num * int(sec_num))
    if operation == "divide":
        ent.insert(0, f_num / int(sec_num))

#defining the buttons
button_0 = Button(root, text = "0", padx = 39, pady = 13, command = lambda: button_click(0))
button_1 = Button(root, text = "1", padx = 13, pady = 13, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 13, pady = 13, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 13, pady = 13, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 13, pady = 13, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 13, pady = 13, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 13, pady = 13, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 13, pady = 13, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 13, pady = 13, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 13, pady = 13, command = lambda: button_click(9))

button_clear = Button(root, text = "CLEAR", padx = 39, pady = 13, command = button_clear)
button_add = Button(root, text = "+", padx = 13, pady = 13, command = button_add)
button_sub = Button(root, text = "-", padx = 13, pady = 13, command = button_sub)
button_multiply = Button(root, text = "*", padx = 13, pady = 13, command = button_multiply)
button_divide = Button(root, text = "/", padx = 13, pady = 13, command = button_divide)
button_equal = Button(root, text = "=", padx = 13, pady = 13, command = button_equal)

#putting the buttons on the screen
button_0.grid(row = 5, column = 0, columnspan = 3)
button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)
button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)
button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)

button_clear.grid(row = 1, column = 0, columnspan = 3)
button_add.grid(row = 4, column = 3)
button_sub.grid(row = 3, column = 3)
button_multiply.grid(row = 2, column = 3)
button_divide.grid(row = 1, column = 3)
button_equal.grid(row = 5, column = 3)

root.mainloop()

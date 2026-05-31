from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("350x450")

# Display
entry = Entry(root, width=20, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button click
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))

# Clear
def clear():
    entry.delete(0, END)

# Equal
def calculate():
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(0, result)

# Buttons
Button(root, text="7", width=8, height=3,
       command=lambda: click(7)).grid(row=1, column=0)

Button(root, text="8", width=8, height=3,
       command=lambda: click(8)).grid(row=1, column=1)

Button(root, text="9", width=8, height=3,
       command=lambda: click(9)).grid(row=1, column=2)

Button(root, text="/", width=8, height=3,
       command=lambda: click("/")).grid(row=1, column=3)

Button(root, text="4", width=8, height=3,
       command=lambda: click(4)).grid(row=2, column=0)

Button(root, text="5", width=8, height=3,
       command=lambda: click(5)).grid(row=2, column=1)

Button(root, text="6", width=8, height=3,
       command=lambda: click(6)).grid(row=2, column=2)

Button(root, text="*", width=8, height=3,
       command=lambda: click("*")).grid(row=2, column=3)

Button(root, text="1", width=8, height=3,
       command=lambda: click(1)).grid(row=3, column=0)

Button(root, text="2", width=8, height=3,
       command=lambda: click(2)).grid(row=3, column=1)

Button(root, text="3", width=8, height=3,
       command=lambda: click(3)).grid(row=3, column=2)

Button(root, text="-", width=8, height=3,
       command=lambda: click("-")).grid(row=3, column=3)

Button(root, text="0", width=8, height=3,
       command=lambda: click(0)).grid(row=4, column=0)

Button(root, text="C", width=8, height=3,
       command=clear).grid(row=4, column=1)

Button(root, text="=", width=8, height=3,
       command=calculate).grid(row=4, column=2)

Button(root, text="+", width=8, height=3,
       command=lambda: click("+")).grid(row=4, column=3)

root.mainloop()
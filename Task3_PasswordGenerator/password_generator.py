from tkinter import *
import random
import string

root = Tk()
root.title("Password Generator")
root.geometry("400x300")

# Heading
title = Label(root,
              text="Password Generator",
              font=("Arial", 18, "bold"))
title.pack(pady=10)

# Length Input
Label(root,
      text="Enter Password Length:",
      font=("Arial", 12)).pack()

length_entry = Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

# Result Box
password_entry = Entry(root,
                       width=30,
                       font=("Arial", 12))
password_entry.pack(pady=10)

# Generate Function
def generate_password():

    length = int(length_entry.get())

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# Button
Button(root,
       text="Generate Password",
       command=generate_password).pack(pady=10)

root.mainloop()
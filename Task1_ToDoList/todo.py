from tkinter import *

root = Tk()
root.title("To Do List")
root.geometry("600x600")

title = Label(root, text="TO DO LIST", font=("Arial", 20, "bold"))
title.pack(pady=10)

task_entry = Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=10)

task_listbox = Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected = task_listbox.curselection()

    if selected:
        task_listbox.delete(selected)

add_button = Button(root, text="Add Task",width=15, command=add_task)
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task",width=15, command=delete_task)
delete_button.pack(pady=5)

def mark_complete():
    selected = task_listbox.curselection()

    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(END, "✓ " + task)

complete_button = Button(root,
                         text="Mark Complete",width=15,
                         command=mark_complete)

complete_button.pack(pady=5)

root.mainloop()
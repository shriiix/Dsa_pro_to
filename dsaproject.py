import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

def mark_as_completed():
    try:
        index = listbox.curselection()
        listbox.itemconfig(index, fg="gray")
    except:
        pass


window = tk.Tk()
window.title("To-Do List")


listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)


entry = tk.Entry(window, width=50)
entry.pack(pady=5)


add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(window, text="Mark as Completed", command=mark_as_completed)
complete_button.pack(pady=5)

window.mainloop()

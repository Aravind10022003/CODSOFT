import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def delete_all_tasks():
    task_listbox.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Colorful To-Do List App")

# Entry widget to add new tasks
entry = tk.Entry(app, width=30, bg="lightblue", font=("Arial", 12))
entry.pack(pady=10)

# Button to add tasks
add_button = tk.Button(app, text="Add Task", command=add_task, bg="green", fg="white", font=("Arial", 12))
add_button.pack()

# Listbox to display the to-do tasks
task_listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=30, bg="lightyellow", font=("Arial", 12))
task_listbox.pack()

# Button to delete selected task
delete_button = tk.Button(app, text="Delete Task", command=delete_task, bg="red", fg="white", font=("Arial", 12))
delete_button.pack()

# Button to delete all tasks
delete_all_button = tk.Button(app, text="Delete All Tasks", command=delete_all_tasks, bg="orange", fg="white", font=("Arial", 12))
delete_all_button.pack()

app.mainloop()

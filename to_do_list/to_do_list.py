# ------------------------------------------------------------
# 📝 ADVANCED TO-DO LIST APP
# Features: File Handling + Date/Time + Threading + Tkinter UI
# ------------------------------------------------------------
import tkinter as tk 
from tkinter import messagebox
from datetime import datetime
import threading
import os 
import time 

# ------------------------------------------------------------
# STEP 1: Create Main Window
# ------------------------------------------------------------
root = tk.Tk()
root.title("Smart To-Do List with remainders")
root.geometry("500x550")
root.resizable(False,False)


# ------------------------------------------------------------
# STEP 2: Create UI Components
# ------------------------------------------------------------
tk.Label(root,text='Smart To-Do List',font=('Arial',20,'bold')).pack(pady=10)

#listbox to show tasks
listbox = tk.Listbox(root,width=60,height=12,font=('Arial',12),selectbackground='lightblue')
listbox.pack(pady=10)

#entry for task name
tk.Label(root,text='Task Name:',font=('Arial',12)).pack()
task_entry = tk.Entry(root,width=40,font=('Arial',13))
task_entry.pack(pady=5)

#datatime entry 
tk.Label(root, text="Due Date & Time (YYYY-MM-DD HH:MM):", font=('Arial', 12)).pack()
datetime_entry = tk.Entry(root,width=40,font=('Arial', 12))
datetime_entry.pack(pady=5)

# ------------------------------------------------------------
# STEP 3: File Handling
# ------------------------------------------------------------

file_name = r"E:\linkedinProjects\BankManagementProject\PythonMiniProjects\to_do_list\tasks.txt"


def load_tasks():
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            for line in file:
                listbox.insert(tk.END,line.strip())

def save_tasks():
    with open(file_name,'w') as file:
        for i in range(listbox.size()):
            file.write(listbox.get(i)+"\n")


  # ------------------------------------------------------------
# STEP 4: Core Functions
# ------------------------------------------------------------

def add_task():
    """Add new task with optional deadline."""
    task = task_entry.get().strip()
    due = datetime_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task name!")
        return

    if due:  # If user entered a date/time
        try:
            datetime.strptime(due, "%Y-%m-%d %H:%M")  # Validate format
            task_line = f"{task} | Due: {due}"
        except ValueError:
            messagebox.showerror("Invalid Format", "Enter time as YYYY-MM-DD HH:MM")
            return
    else:
        task_line = task

    listbox.insert(tk.END, task_line)
    save_tasks()
    task_entry.delete(0, tk.END)
    datetime_entry.delete(0, tk.END)

def delete_task():
    """Delete selected task."""
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except IndexError:
        messagebox.showinfo("Info", "Please select a task to delete!")

def mark_completed():
    """Mark selected task as done."""
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        if not task.startswith("✔️ "):
            listbox.delete(index)
            listbox.insert(index, "✔️ " + task)
            save_tasks()
    except IndexError:
        messagebox.showinfo("Info", "Select a task to mark as completed!")

def show_reminder():
    """Show pending tasks immediately."""
    tasks = listbox.get(0, tk.END)
    pending = [t for t in tasks if not t.startswith("✔️ ")]
    if pending:
        msg = "\n".join(pending)
        messagebox.showinfo("⏰ Pending Tasks", f"Don't forget:\n\n{msg}")
    else:
        messagebox.showinfo("All Done!", "🎉 You have completed all tasks!")

# ------------------------------------------------------------
# STEP 5: Background Reminder Thread
# ------------------------------------------------------------

def reminder_thread():
    """Continuously check for due tasks in the background."""
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")  # Current time
        tasks = listbox.get(0, tk.END)

        for t in tasks:
            # Skip completed ones
            if t.startswith("✔️ "):
                continue
            if "| Due:" in t:
                try:
                    task_name, due_str = t.split("| Due:")
                    due_time = due_str.strip()

                    # If time matches, alert the user
                    if due_time == now:
                        messagebox.showinfo("⏰ Reminder", f"Task '{task_name.strip()}' is due now!")
                except Exception:
                    pass
        time.sleep(60)  # Check every 60 seconds

# Run the reminder thread in background
thread = threading.Thread(target=reminder_thread, daemon=True)
thread.start()

# ------------------------------------------------------------
# STEP 6: Add Buttons
# ------------------------------------------------------------
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Add Task", width=14, font=('Arial', 12), command=add_task).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Delete Task", width=14, font=('Arial', 12), command=delete_task).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Mark Completed", width=14, font=('Arial', 12), command=mark_completed).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Show Reminder", width=14, font=('Arial', 12), command=show_reminder).grid(row=1, column=1, padx=5, pady=5)

# ------------------------------------------------------------
# STEP 7: Load Tasks and Start Main Loop
# ------------------------------------------------------------
load_tasks()
root.mainloop()          

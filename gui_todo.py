import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def refresh_list():
    listbox.delete(0, tk.END)
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        listbox.insert(tk.END, f"{i+1}. {task['title']} [{status}]")

def add_task():
    title = entry.get()
    if title == "":
        messagebox.showwarning("Peringatan", "Tugas tidak boleh kosong!")
        return

    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

    entry.delete(0, tk.END)
    refresh_list()

def complete_task():
    try:
        index = listbox.curselection()[0]
        tasks = load_tasks()
        tasks[index]["done"] = True
        save_tasks(tasks)
        refresh_list()
    except:
        messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks = load_tasks()
        tasks.pop(index)
        save_tasks(tasks)
        refresh_list()
    except:
        messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")

# ================= GUI ==================

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

label = tk.Label(root, text="📝 TO DO LIST", font=("Arial", 16, "bold"))
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

btn_add = tk.Button(root, text="Tambah Tugas", width=20, command=add_task)
btn_add.pack(pady=5)

listbox = tk.Listbox(root, width=45)
listbox.pack(pady=10)

btn_done = tk.Button(root, text="Tandai Selesai", command=complete_task)
btn_done.pack(pady=5)

btn_delete = tk.Button(root, text="Hapus Tugas", command=delete_task)
btn_delete.pack(pady=5)

refresh_list()
root.mainloop()





#Caeser Cipher Algorithm
import tkinter as tk
from tkinter import messagebox

def perform_task():
    task = task_var.get()
    shift_val = shift_entry.get()
    text_val = text_entry.get()

    if not shift_val.isdigit():
        messagebox.showerror("Invalid Input", "Shift must be a number.")
        return

    shift = int(shift_val)
    result = ""

    if task == "E":
        for char in text_val:
            result += chr(ord(char) + shift)
        output_label.config(text="Cipher Text: " + result)
    elif task == "D":
        for char in text_val:
            result += chr(ord(char) - shift)
        output_label.config(text="Plain Text: " + result)
    else:
        messagebox.showerror("Invalid Option", "Please select E (Encrypt) or D (Decrypt).")

# GUI window
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x300")

# Task selection
tk.Label(root, text="Select Task (E for Encrypt, D for Decrypt):").pack(pady=5)
task_var = tk.StringVar()
task_entry = tk.Entry(root, textvariable=task_var)
task_entry.pack()

# Shift input
tk.Label(root, text="Enter Shift Value:").pack(pady=5)
shift_entry = tk.Entry(root)
shift_entry.pack()

# Text input
tk.Label(root, text="Enter Text:").pack(pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.pack()

# Action button
tk.Button(root, text="Execute", command=perform_task).pack(pady=10)

# Output label
output_label = tk.Label(root, text="", wraplength=350)
output_label.pack(pady=10)

# Start the GUI loop
root.mainloop()

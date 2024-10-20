import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os

# Create the main window
root = tk.Tk()
root.title("Run EXE File")
root.geometry("400x300")
root.configure(bg="#282c34")  # Set background color

# Function to run the exe file
def run_exe():
    exe_path = r"D:\unity games\trial 2\Miner\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe"  # Specify the path to your .exe file
    if os.path.exists(exe_path):
        result_label.config(text="Running executable...", fg="lightgreen")
        progress_bar.start(10)  # Start progress bar animation
        try:
            subprocess.Popen(exe_path)
            messagebox.showinfo("Success", "Executable has been started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        result_label.config(text="Executable not found!", fg="red")
        messagebox.showwarning("Warning", "The executable file was not found.")
    progress_bar.stop()  # Stop the progress bar animation

# Create and style a label and button in the window
title_label = tk.Label(root, text="Run EXE File", font=("Helvetica", 16, "bold"), fg="white", bg="#282c34")
title_label.pack(pady=10)

run_button = tk.Button(root, text="Run EXE", command=run_exe, font=("Helvetica", 14), bg="#61afef", fg="white", relief="raised", bd=5)
run_button.pack(pady=20)

# Progress bar for visual feedback
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=280)
progress_bar.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="lightgreen", bg="#282c34")
result_label.pack(pady=10)

# Run the application
root.mainloop()

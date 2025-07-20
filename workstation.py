import os
import webbrowser as wb
import tkinter as tk
from tkinter import messagebox


project_folder = r"C:\Users\Lenovo\Downloads\Work-Setup-Automation-20250720T084701Z-1-001\Work-Setup-Automation"
notion_path = r"C:\Users\Lenovo\AppData\Local\Programs\Notion\Notion.exe"  # Example path
zoom_path = r"C:\Users\Lenovo\AppData\Roaming\Zoom\bin\Zoom.exe"           # Example path


def open_folder(path):
    if os.path.exists(path):
        os.startfile(path)
    else:
        messagebox.showerror("Error", f"Path not found:\n{path}")
import time 

def open_websites(urls):
    for url in urls:
        wb.open(url)
        time.sleep(2) 


def open_app(path):
    if os.path.exists(path):
        os.startfile(path)

# === MODES ===
def coding_mode():
    open_folder(project_folder)
    open_websites([
        "https://stackoverflow.com",
        "https://github.com/shreyal-bangera",
        "https://www.linkedin.com/in/shreyal-y-bangera/"
    ])


    

def meeting_mode():
    open_websites([
        "https://gmail.com",
        "https://meet.google.com"
    ])
    open_app(zoom_path)

def chill_mode():
    open_websites([
        "https://youtube.com",
        "https://open.spotify.com"
    ])
    open_app(notion_path)

# === GUI ===
def launch_gui():
    root = tk.Tk()
    root.title("Workstation Auto-Launcher")
    root.geometry("300x250")
    root.resizable(False, False)

    tk.Label(root, text="Choose your mode", font=("Helvetica", 14)).pack(pady=20)

    tk.Button(root, text="🛠 Coding Mode", width=20, command=coding_mode).pack(pady=5)
    tk.Button(root, text="📞 Meeting Mode", width=20, command=meeting_mode).pack(pady=5)
    tk.Button(root, text="🎵 Chill Mode", width=20, command=chill_mode).pack(pady=5)

    tk.Button(root, text="❌ Exit", width=10, command=root.quit).pack(pady=20)

    root.mainloop()

launch_gui()

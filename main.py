
# main.py
import tkinter as tk
from ui.app import WebsiteBuilderApp

if __name__ == "__main__":
    root = tk.Tk()
    # Configure root background to match load sequence if needed
    
    app = WebsiteBuilderApp(root)
    root.mainloop()

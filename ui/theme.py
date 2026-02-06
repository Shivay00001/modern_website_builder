
# ui/theme.py
import tkinter as tk
from tkinter import ttk
from config import COLORS

class ThemeManager:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.style = ttk.Style(root)
        self.current_mode = "light"
        self.apply_theme()

    def toggle_mode(self):
        self.current_mode = "dark" if self.current_mode == "light" else "light"
        self.apply_theme()

    def get_color(self, name: str) -> str:
        if name == "bg":
            return COLORS["dark_bg"] if self.current_mode == "dark" else COLORS["light_bg"]
        if name == "surface":
            return COLORS["dark_surface"] if self.current_mode == "dark" else COLORS["light_surface"]
        if name == "text":
            return COLORS["text_dark"] if self.current_mode == "dark" else COLORS["text_light"]
        return COLORS.get(name, "#000000")

    def apply_theme(self):
        bg = self.get_color("bg")
        surface = self.get_color("surface")
        text = self.get_color("text")
        primary = COLORS["primary"]

        self.root.configure(bg=bg)
        self.style.theme_use('clam') # Use 'clam' as base for better customizability

        # Global Config
        self.style.configure(".", 
                             background=bg, 
                             foreground=text, 
                             font=("Segoe UI", 10),
                             borderwidth=0)

        # Frames
        self.style.configure("TFrame", background=bg)
        self.style.configure("Surface.TFrame", background=surface)
        
        # Labels
        self.style.configure("TLabel", background=bg, foreground=text)
        self.style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), background=bg, foreground=primary)
        self.style.configure("SubHeader.TLabel", font=("Segoe UI", 12, "bold"), background=bg, foreground=text)
        self.style.configure("Surface.TLabel", background=surface, foreground=text)

        # Buttons
        self.style.configure("TButton", 
                             background=surface, 
                             foreground=text, 
                             borderwidth=1, 
                             bordercolor=COLORS["grey"],  # Added bordercolor
                             focuscolor="none",
                             padding=6)
        
        self.style.map("TButton",
                       background=[("active", COLORS["primary"])],
                       foreground=[("active", "white")])

        self.style.configure("Primary.TButton", 
                             background=primary, 
                             foreground="white", 
                             borderwidth=0)
        
        self.style.map("Primary.TButton",
                       background=[("active", COLORS["primary_hover"])]) # fixed: button hover color

        # Inputs
        self.style.configure("TEntry", 
                             fieldbackground=surface, 
                             foreground=text, 
                             insertcolor=text,
                             borderwidth=1,
                             relief="flat",
                             padding=5)
        
        self.style.configure("TCombobox",
                             fieldbackground=surface,
                             background=surface,
                             foreground=text,
                             arrowcolor=text)

        # Labelframes
        self.style.configure("TLabelframe", background=bg, foreground=text, bordercolor=COLORS["grey"])
        self.style.configure("TLabelframe.Label", background=bg, foreground=text)


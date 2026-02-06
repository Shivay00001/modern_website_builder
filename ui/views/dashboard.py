
# ui/views/dashboard.py
import tkinter as tk
from tkinter import ttk
from ui.theme import ThemeManager

class DashboardView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header_frame = ttk.Frame(self, padding=40)
        header_frame.pack(fill=tk.X)
        
        ttk.Label(header_frame, text="Welcome back, Creator!", style="Header.TLabel", font=("Segoe UI", 24, "bold")).pack(anchor=tk.W)
        ttk.Label(header_frame, text="What would you like to build today?", style="TLabel", font=("Segoe UI", 12)).pack(anchor=tk.W, pady=(5,0))
        
        # Actions
        actions_frame = ttk.Frame(self, padding=40)
        actions_frame.pack(fill=tk.X)
        
        create_btn = ttk.Button(actions_frame, text="+ Create New Site", style="Primary.TButton", command=lambda: self.controller.show_view("Templates"))
        create_btn.pack(side=tk.LEFT, padx=(0, 20), ipadx=20, ipady=10)
        
        open_btn = ttk.Button(actions_frame, text="📂 Open Project", command=self.open_project)
        open_btn.pack(side=tk.LEFT, ipadx=20, ipady=10)
        
        # Recent Projects
        recent_frame = ttk.Frame(self, padding=40)
        recent_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(recent_frame, text="Recent Projects", style="SubHeader.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Placeholder for recent list
        list_frame = ttk.Frame(recent_frame, style="Surface.TFrame", padding=2)
        list_frame.pack(fill=tk.X)
        
        # Mock Item
        item = ttk.Frame(list_frame, style="Surface.TFrame", padding=15)
        item.pack(fill=tk.X, pady=1)
        ttk.Label(item, text="My Tech Startup", style="Surface.TLabel", font=("Segoe UI", 11, "bold")).pack(side=tk.LEFT)
        ttk.Label(item, text="Last edited: 2 hours ago", style="Surface.TLabel").pack(side=tk.RIGHT)
        
    def open_project(self):
        print("Open Project Clicked")

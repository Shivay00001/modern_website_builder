
# ui/app.py
import tkinter as tk
from tkinter import ttk, messagebox
from ui.theme import ThemeManager
from core.state import state
from config import APP_NAME, VERSION

class WebsiteBuilderApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(f"{APP_NAME} v{VERSION}")
        self.root.geometry("1400x900")
        self.root.minsize(1000, 700)
        
        # Initialize Theme
        self.theme = ThemeManager(self.root)
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        # 1. Main Container
        self.container = ttk.Frame(self.root)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        # 2. Configure Grid
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # 3. Initialize Views
        self.frames = {}
        from ui.views.dashboard import DashboardView
        from ui.views.templates import TemplatesView
        from ui.views.editor import EditorView
        
        for F in (DashboardView, TemplatesView, EditorView):
            page_name = F.__name__.replace("View", "")
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_view("Dashboard")
        
    def show_view(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

            
    def setup_toolbar(self):
        # Left side: Breadcrumb / Title
        ttk.Label(self.toolbar, text="  New Project - Untitled", style="SubHeader.TLabel").pack(side=tk.LEFT, padx=20, pady=15)
        
        # Right side: Actions
        actions_frame = ttk.Frame(self.toolbar, style="Surface.TFrame")
        actions_frame.pack(side=tk.RIGHT, padx=20)
        
        ttk.Button(actions_frame, text="Theme: 🌓", command=self.theme.toggle_mode, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="Save", width=10).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="Export Website", style="Primary.TButton").pack(side=tk.LEFT, padx=5)
        
    def on_nav_click(self, section):
        print(f"Navigating to {section}")
        # In future, switch views here

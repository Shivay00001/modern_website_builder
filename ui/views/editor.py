
# ui/views/editor.py
import tkinter as tk
from tkinter import ttk

class EditorView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
        # 1. Editor Toolbar
        toolbar = ttk.Frame(self, style="Surface.TFrame", height=50)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        ttk.Button(toolbar, text="← Back", command=lambda: self.controller.show_view("Dashboard")).pack(side=tk.LEFT, padx=10, pady=5)
        ttk.Label(toolbar, text="Editing: Home Page", style="Surface.TLabel").pack(side=tk.LEFT, padx=10)
        
        # 2. Main Workspace (Sidebar + Canvas)
        workspace = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        workspace.pack(fill=tk.BOTH, expand=True)
        
        # Tools Panel (Left)
        tools_frame = ttk.Frame(workspace, style="Surface.TFrame", width=250)
        workspace.add(tools_frame, weight=1)
        
        ttk.Label(tools_frame, text="Components", style="SubHeader.TLabel").pack(pady=10)
        
        # Draggable Blocks List
        blocks = ["Hero Section", "Features Grid", "Testimonials", "Call to Action", "Image Gallery", "Contact Form"]
        for block in blocks:
            b = ttk.Label(tools_frame, text=f" :: {block}", style="Surface.TLabel", relief="solid", borderwidth=1, padding=10)
            b.pack(fill=tk.X, padx=10, pady=5)
            # Bind drag events here later
            
        # Canvas Area (Right)
        canvas_area = ttk.Frame(workspace, style="TFrame")
        workspace.add(canvas_area, weight=4)
        
        # Scrollable Preview
        self.canvas = tk.Canvas(canvas_area, bg="white")
        self.scrollbar = ttk.Scrollbar(canvas_area, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Draw placeholder website
        self.draw_placeholder_site()
        
    def tkraise(self, aboveThis=None):
        super().tkraise(aboveThis)
        self.refresh_preview()

    def refresh_preview(self):
        self.canvas.delete("all")
        from core.state import state
        from core.engine import Block
        
        blocks = state.current_project.get("content", [])
        y_offset = 20
        
        for block in blocks:
            # Draw Block Container
            if isinstance(block, dict): block = Block.from_dict(block) # Handle dict vs obj
            
            self.canvas.create_rectangle(20, y_offset, 800, y_offset + 150, fill="#ffffff", outline="#e5e7eb")
            
            # Draw Label
            label_text = f"Block: {block.type.upper()}"
            self.canvas.create_text(40, y_offset + 30, text=label_text, anchor="nw", font=("Segoe UI", 10, "bold"), fill="#6366f1")
            
            # Draw Content Preview (Simplified)
            content_desc = str(block.content)[:100] + "..."
            self.canvas.create_text(40, y_offset + 60, text=content_desc, anchor="nw", width=700, font=("Segoe UI", 9), fill="#4b5563")
            
            y_offset += 170
            
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def draw_placeholder_site(self):
        # Kept for initial init, but mostly unused now
        pass


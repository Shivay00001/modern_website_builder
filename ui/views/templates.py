
# ui/views/templates.py
import tkinter as tk
from tkinter import ttk

class TemplatesView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header = ttk.Frame(self, padding=30)
        header.pack(fill=tk.X)
        ttk.Label(header, text="Choose a Template", style="Header.TLabel").pack(side=tk.LEFT)
        
        # Filter Bar
        filter_frame = ttk.Frame(self, padding=(30, 0))
        filter_frame.pack(fill=tk.X)
        categories = ["All", "Business", "Portfolio", "E-commerce", "Blog", "Restaurant", "SaaS"]
        
        for cat in categories:
            btn = ttk.Button(filter_frame, text=cat, width=12) # Simplified for now
            btn.pack(side=tk.LEFT, padx=(0, 10))
            
        # Grid Container
        bg_color = self.controller.theme.get_color("bg")
        self.canvas = tk.Canvas(self, bg=bg_color, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="TFrame")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True, padx=30, pady=20)
        self.scrollbar.pack(side="right", fill="y")
        
        # Load Templates (Mock)
        self.load_templates()
        
    def load_templates(self):
        # Grid Layout
        columns = 3
        templates = [
            {"name": "Modern Business", "cat": "Business", "color": "#4f46e5"},
            {"name": "Creative Portfolio", "cat": "Portfolio", "color": "#ec4899"},
            {"name": "SaaS Starter", "cat": "SaaS", "color": "#10b981"},
            {"name": "Online Store", "cat": "E-commerce", "color": "#f59e0b"},
            {"name": "Foodie Heaven", "cat": "Restaurant", "color": "#ef4444"},
            {"name": "Tech Blog", "cat": "Blog", "color": "#3b82f6"},
        ]
        
        for i, tmpl in enumerate(templates):
            row = i // columns
            col = i % columns
            self.create_template_card(tmpl, row, col)
            
    def create_template_card(self, tmpl, row, col):
        card = ttk.Frame(self.scrollable_frame, style="Surface.TFrame", padding=15, width=250, height=200)
        card.grid(row=row, column=col, padx=15, pady=15)
        card.grid_propagate(False)
        
        # Preview Box (Color placeholder)
        preview = tk.Frame(card, bg=tmpl["color"], height=100)
        preview.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(card, text=tmpl["name"], style="Surface.TLabel", font=("Segoe UI", 11, "bold")).pack(anchor=tk.W)
        ttk.Label(card, text=tmpl["cat"], style="Surface.TLabel", font=("Segoe UI", 9)).pack(anchor=tk.W)
        
        btn = ttk.Button(card, text="Select", command=lambda: self.select_template(tmpl))
        btn.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
    def select_template(self, tmpl_def):
        from core.state import state
        from templates.registry import get_template, REGISTRY
        from core.engine import Block
        
        # In a real app, 'tmpl_def' from the grid might just be metadata
        # We find the full template definition
        # For this mock, we assume tmpl_def IS the metadata dict from load_templates
        # We need to map grid items to registry items.
        # Shortcuts for demo:
        
        selected_id = "business_modern" # Defaulting for demo
        if tmpl_def['cat'] == "Portfolio": selected_id = "portfolio_dark"
        
        full_template = get_template(selected_id)
        if full_template:
            # Initialize State
            state.new_project()
            state.update_field("template", full_template.name)
            
            # Convert dict definitions to Block objects
            blocks = [Block(b['type'], b['content']) for b in full_template.default_blocks]
            state.update_field("content", blocks) # storing raw list for now, but usually Website object
            
            print(f"Project Initialized with {len(blocks)} blocks")
            self.controller.show_view("Editor")


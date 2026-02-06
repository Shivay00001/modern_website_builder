
# config.py
import os

APP_NAME = "Professional Website Builder"
VERSION = "1.0.0"
COMPANY_NAME = "ModernTech"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Colors (Flat UI Palette)
COLORS = {
    "primary": "#6366f1",         # Indigo 500
    "primary_hover": "#4f46e5",   # Indigo 600
    "secondary": "#ec4899",       # Pink 500
    "dark_bg": "#1e293b",         # Slate 800
    "dark_surface": "#334155",    # Slate 700
    "light_bg": "#f8fafc",        # Slate 50
    "light_surface": "#ffffff",   # White
    "text_dark": "#f8fafc",       # Slate 50 (for dark mode)
    "text_light": "#0f172a",      # Slate 900 (for light mode)
    "grey": "#94a3b8",            # Slate 400
    "success": "#22c55e",         # Green 500
    "error": "#ef4444",           # Red 500
    "warning": "#f59e0b"          # Amber 500
}

# License Features
FREE_TEMPLATE_LIMIT = 0.3 # 30% available
FREE_EXPORT_LIMIT = True  # Can export but with branding

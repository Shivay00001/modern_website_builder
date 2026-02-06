
# core/state.py
import json
import os
from typing import Dict, Any

class ProjectState:
    def __init__(self):
        self.current_project = {
            "name": "Untitled Project",
            "template": "Business",
            "theme": "light",
            "primary_color": "#6366f1",
            "content": [], # List of blocks
            "branding": {
                "logo_text": "MyBrand",
                "tagline": "Innovation first"
            },
            "seo": {
                "title": "",
                "description": "",
                "keywords": []
            }
        }
        self.file_path = None
    
    def new_project(self):
        self.__init__()
        
    def load_project(self, filepath: str):
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                self.current_project = json.load(f)
            self.file_path = filepath
            return True
        return False
        
    def save_project(self, filepath: str = None):
        target = filepath or self.file_path
        if target:
            with open(target, 'w', encoding='utf-8') as f:
                json.dump(self.current_project, f, indent=4)
            self.file_path = target
            return True
        return False

    def update_field(self, key: str, value: Any):
        self.current_project[key] = value

    def update_nested(self, parent: str, key: str, value: Any):
        if parent in self.current_project:
            self.current_project[parent][key] = value

# Global State Instance
state = ProjectState()

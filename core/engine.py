
# core/engine.py
from typing import List, Dict, Any
import uuid

class Block:
    def __init__(self, type: str, content: Dict[str, Any] = None):
        self.id = str(uuid.uuid4())
        self.type = type # e.g., 'hero', 'features', 'cta'
        self.content = content or {}
        
    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "content": self.content
        }
    
    @classmethod
    def from_dict(cls, data):
        obj = cls(data['type'], data['content'])
        obj.id = data['id']
        return obj

class Website:
    def __init__(self, name: str, template: str):
        self.name = name
        self.template = template
        self.blocks: List[Block] = []
        self.branding = {
            "primary_color": "#6366f1",
            "font_header": "Inter",
            "font_body": "Inter"
        }
        self.meta = {"title": "My Website", "description": ""}
        
    def add_block(self, block: Block, index: int = -1):
        if index == -1:
            self.blocks.append(block)
        else:
            self.blocks.insert(index, block)
            
    def remove_block(self, block_id: str):
        self.blocks = [b for b in self.blocks if b.id != block_id]
        
    def to_dict(self):
        return {
            "name": self.name,
            "template": self.template,
            "blocks": [b.to_dict() for b in self.blocks],
            "branding": self.branding,
            "meta": self.meta
        }

class TemplateManager:
    # Logic to load template definitions
    pass

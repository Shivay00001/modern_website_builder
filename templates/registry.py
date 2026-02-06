
# templates/registry.py

class Template:
    def __init__(self, id, name, category, default_blocks):
        self.id = id
        self.name = name
        self.category = category
        self.default_blocks = default_blocks # List of block definitions

REGISTRY = [
    Template("business_modern", "Modern Business", "Business", [
        {"type": "hero", "content": {"title": "Grow Your Business", "subtitle": "We help you scale."}},
        {"type": "features", "content": {}},
        {"type": "cta", "content": {"title": "Ready to start?"}}
    ]),
    Template("portfolio_dark", "Creative Portfolio", "Portfolio", [
        {"type": "hero", "content": {"title": "Hi, I'm Creator", "subtitle": "I design things."}},
        {"type": "gallery", "content": {}}
    ])
]

def get_template(id):
    for t in REGISTRY:
        if t.id == id:
            return t
    return None

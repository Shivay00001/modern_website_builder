
# generators/renderer.py
from core.engine import Website, Block

class HTMLRenderer:
    def render(self, website: Website) -> str:
        head = self._render_head(website)
        body = self._render_body(website)
        return f"""<!DOCTYPE html>
<html lang="en">
{head}
{body}
</html>"""

    def _render_head(self, website: Website) -> str:
        return f"""
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{website.meta.get('title', 'My Website')}</title>
    <meta name="description" content="{website.meta.get('description', '')}">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        :root {{
            --primary: {website.branding['primary_color']};
        }}
    </style>
</head>"""

    def _render_body(self, website: Website) -> str:
        content = ""
        for block in website.blocks:
            content += self._render_block(block)
        
        return f"""
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">{website.name}</div>
        </div>
    </nav>
    <main>
        {content}
    </main>
    <footer>
        <p>&copy; 2024 {website.name}</p>
    </footer>
</body>"""

    def _render_block(self, block: Block) -> str:
        if block.type == "hero":
            return f"""
            <section class="hero">
                <div class="container">
                    <h1>{block.content.get('title', 'Hero Title')}</h1>
                    <p>{block.content.get('subtitle', 'Hero Subtitle')}</p>
                    <a href="#" class="btn btn-primary">{block.content.get('cta_text', 'Learn More')}</a>
                </div>
            </section>"""
        elif block.type == "features":
            return f"""
            <section class="features">
                <div class="container">
                    <h2>Features</h2>
                    <div class="grid">
                        <!-- Dynamic features would go here -->
                        <div class="card">Feature 1</div>
                        <div class="card">Feature 2</div>
                        <div class="card">Feature 3</div>
                    </div>
                </div>
            </section>"""
        return f"<!-- Unknown Block: {block.type} -->"

class CSSGenerator:
    def generate(self, website: Website) -> str:
        return """
        /* Base Styles */
        body { font-family: 'Inter', sans-serif; margin: 0; line-height: 1.6; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 1rem; }
        
        /* Components */
        .btn { padding: 0.75rem 1.5rem; border-radius: 99px; text-decoration: none; display: inline-block; font-weight: 600; }
        .btn-primary { background: var(--primary); color: white; }
        
        /* Sections */
        .hero { padding: 8rem 0; text-align: center; background: #f9fafb; }
        .hero h1 { font-size: 3rem; margin-bottom: 1rem; color: #111827; }
        .features { padding: 6rem 0; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
        .card { padding: 2rem; border: 1px solid #e5e7eb; border-radius: 0.5rem; }
        """

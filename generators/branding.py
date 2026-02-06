
# generators/branding.py
import random

class BrandingGenerator:
    def generate_palette(self, base_color: str = None):
        """
        Generates a color palette. If base_color is provided, generates harmony.
        Otherwise random.
        """
        if not base_color:
            base_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            
        return {
            "primary": base_color,
            "secondary": self._adjust_hue(base_color, 30),
            "accent": self._adjust_hue(base_color, 180),
            "bg": "#f9fafb" 
        }
    
    def _adjust_hue(self, hex_color, degree):
        # Simplified hue shift (placeholder for real logic)
        return hex_color 

branding_gen = BrandingGenerator()

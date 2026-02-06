import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox, colorchooser
import os
import json
import webbrowser
from datetime import datetime

class WebsiteBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Professional Website Builder")
        self.root.geometry("1000x700")
        
        # Color scheme
        self.primary_color = "#6366f1"
        self.secondary_color = "#8b5cf6"
        
        # Templates
        self.templates = {
            "Business": self.generate_business_template,
            "Portfolio": self.generate_portfolio_template,
            "E-commerce": self.generate_ecommerce_template,
            "Blog": self.generate_blog_template,
            "Landing Page": self.generate_landing_template,
            "Restaurant": self.generate_restaurant_template
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = tk.Label(main_frame, text="🌐 Modern Website Builder", 
                              font=("Arial", 20, "bold"), fg=self.primary_color)
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Left Panel - Inputs
        input_frame = ttk.LabelFrame(main_frame, text="Website Configuration", padding="10")
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        # Website Name
        ttk.Label(input_frame, text="Website Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.website_name = ttk.Entry(input_frame, width=30)
        self.website_name.grid(row=0, column=1, pady=5)
        self.website_name.insert(0, "InnovateTech")
        
        # Template Selection
        ttk.Label(input_frame, text="Template:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.template_var = tk.StringVar(value="Business")
        template_combo = ttk.Combobox(input_frame, textvariable=self.template_var, 
                                     values=list(self.templates.keys()), state="readonly", width=28)
        template_combo.grid(row=1, column=1, pady=5)
        
        # Business Description
        ttk.Label(input_frame, text="Description:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.description = scrolledtext.ScrolledText(input_frame, width=30, height=4)
        self.description.grid(row=2, column=1, pady=5)
        self.description.insert(1.0, "Transform your business with cutting-edge solutions designed for the modern world.")
        
        # Contact Email
        ttk.Label(input_frame, text="Contact Email:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.email = ttk.Entry(input_frame, width=30)
        self.email.grid(row=3, column=1, pady=5)
        self.email.insert(0, "hello@innovatetech.com")
        
        # Phone
        ttk.Label(input_frame, text="Phone:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.phone = ttk.Entry(input_frame, width=30)
        self.phone.grid(row=4, column=1, pady=5)
        self.phone.insert(0, "+1 (555) 123-4567")
        
        # Primary Color
        ttk.Label(input_frame, text="Primary Color:").grid(row=5, column=0, sticky=tk.W, pady=5)
        color_frame = ttk.Frame(input_frame)
        color_frame.grid(row=5, column=1, pady=5, sticky=tk.W)
        self.color_display = tk.Label(color_frame, bg=self.primary_color, width=10, relief="solid")
        self.color_display.pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(color_frame, text="Choose Color", command=self.choose_color).pack(side=tk.LEFT)
        
        # Features
        ttk.Label(input_frame, text="Features (comma separated):").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.features = scrolledtext.ScrolledText(input_frame, width=30, height=3)
        self.features.grid(row=6, column=1, pady=5)
        self.features.insert(1.0, "AI-Powered Analytics, 24/7 Support, Cloud Integration, Advanced Security")
        
        # Social Media
        ttk.Label(input_frame, text="Social Links:").grid(row=7, column=0, sticky=tk.W, pady=5)
        social_frame = ttk.Frame(input_frame)
        social_frame.grid(row=7, column=1, sticky=tk.W)
        
        ttk.Label(social_frame, text="Facebook:").pack(anchor=tk.W)
        self.facebook = ttk.Entry(social_frame, width=30)
        self.facebook.pack(anchor=tk.W)
        
        ttk.Label(social_frame, text="Twitter:").pack(anchor=tk.W)
        self.twitter = ttk.Entry(social_frame, width=30)
        self.twitter.pack(anchor=tk.W)
        
        ttk.Label(social_frame, text="LinkedIn:").pack(anchor=tk.W)
        self.linkedin = ttk.Entry(social_frame, width=30)
        self.linkedin.pack(anchor=tk.W)
        
        # Right Panel - Preview & Actions
        right_frame = ttk.Frame(main_frame)
        right_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)
        
        # Preview
        preview_frame = ttk.LabelFrame(right_frame, text="HTML Preview", padding="10")
        preview_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        preview_frame.rowconfigure(0, weight=1)
        preview_frame.columnconfigure(0, weight=1)
        
        self.preview = scrolledtext.ScrolledText(preview_frame, wrap=tk.WORD, width=50, height=20)
        self.preview.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Buttons
        button_frame = ttk.Frame(right_frame)
        button_frame.grid(row=1, column=0, pady=10)
        
        ttk.Button(button_frame, text="🔨 Generate Website", 
                  command=self.generate_website).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="💾 Save to File", 
                  command=self.save_website).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🌐 Preview in Browser", 
                  command=self.preview_in_browser).pack(side=tk.LEFT, padx=5)
        
        # Status Bar
        self.status = tk.Label(main_frame, text="Ready to build your modern website", 
                             bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Primary Color")
        if color[1]:
            self.primary_color = color[1]
            self.color_display.config(bg=self.primary_color)
            
    def get_user_data(self):
        return {
            "name": self.website_name.get(),
            "description": self.description.get(1.0, tk.END).strip(),
            "email": self.email.get(),
            "phone": self.phone.get(),
            "color": self.primary_color,
            "features": [f.strip() for f in self.features.get(1.0, tk.END).strip().split(",")],
            "social": {
                "facebook": self.facebook.get(),
                "twitter": self.twitter.get(),
                "linkedin": self.linkedin.get()
            }
        }
    
    def generate_website(self):
        template = self.template_var.get()
        data = self.get_user_data()
        
        if template in self.templates:
            html_content = self.templates[template](data)
            self.preview.delete(1.0, tk.END)
            self.preview.insert(1.0, html_content)
            self.status.config(text=f"✓ {template} website generated successfully!")
            self.current_html = html_content
        else:
            messagebox.showerror("Error", "Invalid template selected")
    
    def save_website(self):
        if not hasattr(self, 'current_html'):
            messagebox.showwarning("Warning", "Please generate a website first!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML files", "*.html"), ("All files", "*.*")],
            initialfile=f"{self.website_name.get().replace(' ', '_').lower()}.html"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.current_html)
                self.status.config(text=f"✓ Website saved to {file_path}")
                messagebox.showinfo("Success", f"Website saved successfully!\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    
    def preview_in_browser(self):
        if not hasattr(self, 'current_html'):
            messagebox.showwarning("Warning", "Please generate a website first!")
            return
        
        temp_file = "temp_preview.html"
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(self.current_html)
        
        webbrowser.open('file://' + os.path.abspath(temp_file))
        self.status.config(text="✓ Website opened in browser")
    
    def generate_business_template(self, data):
        features_html = "\n".join([f'''
            <div class="feature-card">
                <div class="feature-icon">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                    </svg>
                </div>
                <h3>{feature}</h3>
                <p>Experience excellence with our innovative approach to delivering results.</p>
            </div>''' for feature in data['features']])
        
        social_html = ""
        if data['social']['facebook']:
            social_html += f'<a href="{data["social"]["facebook"]}" class="social-icon"><svg width="24" height="24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>'
        if data['social']['twitter']:
            social_html += f'<a href="{data["social"]["twitter"]}" class="social-icon"><svg width="24" height="24" fill="currentColor"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg></a>'
        if data['social']['linkedin']:
            social_html += f'<a href="{data["social"]["linkedin"]}" class="social-icon"><svg width="24" height="24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>'
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['name']} - Modern Business Solutions</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        :root {{
            --primary: {data['color']};
            --primary-dark: {data['color']}dd;
            --text-dark: #1a1a1a;
            --text-light: #6b7280;
            --bg-light: #f9fafb;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-dark);
            overflow-x: hidden;
        }}
        
        /* Navigation */
        .navbar {{
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            z-index: 1000;
            transition: all 0.3s ease;
        }}
        
        .nav-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .nav-links {{
            display: flex;
            gap: 2rem;
            list-style: none;
        }}
        
        .nav-links a {{
            color: var(--text-dark);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
            position: relative;
        }}
        
        .nav-links a::after {{
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--primary);
            transition: width 0.3s ease;
        }}
        
        .nav-links a:hover::after {{
            width: 100%;
        }}
        
        /* Hero Section */
        .hero {{
            margin-top: 80px;
            min-height: 90vh;
            background: linear-gradient(135deg, {data['color']}15 0%, {data['color']}05 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }}
        
        .hero::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, {data['color']}20 0%, transparent 70%);
            animation: float 20s ease-in-out infinite;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translate(0, 0) rotate(0deg); }}
            33% {{ transform: translate(30px, -30px) rotate(120deg); }}
            66% {{ transform: translate(-20px, 20px) rotate(240deg); }}
        }}
        
        .hero-content {{
            max-width: 1200px;
            padding: 0 2rem;
            text-align: center;
            position: relative;
            z-index: 1;
        }}
        
        .hero h1 {{
            font-size: clamp(2.5rem, 6vw, 4.5rem);
            font-weight: 800;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, var(--text-dark), var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: fadeInUp 0.8s ease;
        }}
        
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .hero p {{
            font-size: 1.25rem;
            color: var(--text-light);
            max-width: 700px;
            margin: 0 auto 2.5rem;
            animation: fadeInUp 0.8s ease 0.2s both;
        }}
        
        .cta-buttons {{
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            animation: fadeInUp 0.8s ease 0.4s both;
        }}
        
        .btn {{
            padding: 1rem 2.5rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            display: inline-block;
        }}
        
        .btn-primary {{
            background: var(--primary);
            color: white;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
        }}
        
        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 15px 40px rgba(99, 102, 241, 0.4);
        }}
        
        .btn-secondary {{
            background: white;
            color: var(--primary);
            border: 2px solid var(--primary);
        }}
        
        .btn-secondary:hover {{
            background: var(--primary);
            color: white;
        }}
        
        /* Features Section */
        .features {{
            padding: 6rem 2rem;
            background: white;
        }}
        
        .features-container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .section-header {{
            text-align: center;
            margin-bottom: 4rem;
        }}
        
        .section-header h2 {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }}
        
        .section-header p {{
            font-size: 1.1rem;
            color: var(--text-light);
            max-width: 600px;
            margin: 0 auto;
        }}
        
        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }}
        
        .feature-card {{
            padding: 2.5rem;
            background: white;
            border-radius: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            border: 1px solid #f0f0f0;
        }}
        
        .feature-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            border-color: var(--primary);
        }}
        
        .feature-icon {{
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, {data['color']}20, {data['color']}10);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
            color: var(--primary);
        }}
        
        .feature-card h3 {{
            font-size: 1.3rem;
            margin-bottom: 0.75rem;
            color: var(--text-dark);
        }}
        
        .feature-card p {{
            color: var(--text-light);
            line-height: 1.7;
        }}
        
        /* Stats Section */
        .stats {{
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            padding: 5rem 2rem;
            color: white;
        }}
        
        .stats-container {{
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 3rem;
            text-align: center;
        }}
        
        .stat-item h3 {{
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }}
        
        .stat-item p {{
            font-size: 1.1rem;
            opacity: 0.9;
        }}
        
        /* Contact Section */
        .contact {{
            padding: 6rem 2rem;
            background: var(--bg-light);
        }}
        
        .contact-container {{
            max-width: 600px;
            margin: 0 auto;
        }}
        
        .contact-card {{
            background: white;
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }}
        
        .contact-item {{
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            background: var(--bg-light);
            border-radius: 15px;
            transition: all 0.3s ease;
        }}
        
        .contact-item:hover {{
            background: {data['color']}15;
            transform: translateX(5px);
        }}
        
        .contact-icon {{
            width: 50px;
            height: 50px;
            background: var(--primary);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }}
        
        /* Footer */
        .footer {{
            background: #1a1a1a;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }}
        
        .footer-content {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .social-links {{
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin-bottom: 2rem;
        }}
        
        .social-icon {{
            width: 45px;
            height: 45px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            transition: all 0.3s ease;
        }}
        
        .social-icon:hover {{
            background: var(--primary);
            transform: translateY(-3px);
        }}
        
        @media (max-width: 768px) {{
            .nav-links {{ display: none; }}
            .hero {{ min-height: 70vh; }}
            .hero h1 {{ font-size: 2rem; }}
            .cta-buttons {{ flex-direction: column; }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">{data['name']}</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section id="home" class="hero">
        <div class="hero-content">
            <h1>{data['name']}</h1>
            <p>{data['description']}</p>
            <div class="cta-buttons">
                <a href="#contact" class="btn btn-primary">Get Started</a>
                <a href="#features" class="btn btn-secondary">Learn More</a>
            </div>
        </div>
    </section>

    <section id="features" class="features">
        <div class="features-container">
            <div class="section-header">
                <h2>Why Choose Us</h2>
                <p>Discover the features that make us the best choice for your business needs</p>
            </div>
            <div class="features-grid">
                {features_html}
            </div>
        </div>
    </section>

    <section class="stats">
        <div class="stats-container">
            <div class="stat-item">
                <h3>500+</h3>
                <p>Happy Clients</p>
            </div>
            <div class="stat-item">
                <h3>98%</h3>
                <p>Success Rate</p>
            </div>
            <div class="stat-item">
                <h3>24/7</h3>
                <p>Support Available</p>
            </div>
            <div class="stat-item">
                <h3>10+</h3>
                <p>Years Experience</p>
            </div>
        </div>
    </section>

    <section id="contact" class="contact">
        <div class="contact-container">
            <div class="section-header">
                <h2>Get In Touch</h2>
                <p>Ready to start your journey? Contact us today</p>
            </div>
            <div class="contact-card">
                <div class="contact-item">
                    <div class="contact-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                            <polyline points="22,6 12,13 2,6"></polyline>
                        </svg>
                    </div>
                    <div>
                        <h3>Email Us</h3>
                        <p>{data['email']}</p>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                        </svg>
                    </div>
                    <div>
                        <h3>Call Us</h3>
                        <p>{data['phone']}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="footer-content">
            <div class="social-links">
                {social_html}
            </div>
            <p>&copy; {datetime.now().year} {data['name']}. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>'''

if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteBuilder(root)
    root.mainloop()

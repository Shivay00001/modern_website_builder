# Modern Website Builder

A sleek, intuitive desktop application built with Python and Tkinter for generating beautiful, responsive HTML websites without writing any code. Perfect for quickly scaffolding landing pages, business profiles, and portfolios.

## 🚀 Key Features

- **No-Code Interface**: An easy-to-use GUI allowing you to input your website's name, description, contact details, features, and social links.
- **Multiple Templates**: Choose from built-in responsive templates including Business, Portfolio, E-commerce, Blog, Landing Page, and Restaurant.
- **Color Customization**: Integrated color picker to perfectly match your brand's primary color scheme.
- **Live HTML Preview**: View the generated raw HTML directly within the app before saving.
- **Browser Preview**: One-click preview of the generated website in your default web browser.

## ⚙️ Prerequisites

- Python 3.8 or higher
- The built-in `tkinter` module (usually included with standard Python installations)
- Optional: `pyinstaller` (if you wish to build a standalone executable)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shivay00001/modern_website_builder.git
   cd modern_website_builder
   ```

2. (Optional) Install `pyinstaller` for building executables:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the main application script directly:
```bash
python website_builder.py
```

1. Fill out the **Website Configuration** form on the left panel (Name, Description, Email, Phone, Features, etc.).
2. Click **Choose Color** to pick your brand's primary accent color.
3. Click **🔨 Generate Website** to create the raw HTML.
4. Click **🌐 Preview in Browser** to view the live result.
5. Click **💾 Save to File** to export the `.html` file to your computer.

### Building a Standalone Executable
If you want to package this app into a `.exe` for Windows, run the provided build script:
```bash
python build_exe.py
```
The compiled application will be placed in the `dist/` directory.

## License
This project is licensed under the terms provided in the LICENSE file.

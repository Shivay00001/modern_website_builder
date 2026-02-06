
import os
import subprocess
import sys

def build():
    print("🚀 Starting Build Process...")
    
    # Check if pyinstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller found")
    except ImportError:
        print("x PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        
    # Run Build
    print("🔨 Building EXE...")
    subprocess.check_call(["pyinstaller", "builder.spec", "--noconfirm", "--clean"])
    
    print("✅ Build Complete!")
    print(f"Output located at: {os.path.abspath('dist/ModernWebsiteBuilder')}")

if __name__ == "__main__":
    build()

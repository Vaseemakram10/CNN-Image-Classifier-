#!/usr/bin/env python3
"""
Setup Verification Script
Run this to check if your environment is properly configured.
"""

import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 8:
        print("  ✓ Python version is compatible (3.8+)")
        return True
    else:
        print("  ✗ Python version must be 3.8 or higher")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    print("\nChecking dependencies...")
    required = {
        'flask': 'Flask',
        'tensorflow': 'TensorFlow',
        'numpy': 'NumPy',
        'PIL': 'Pillow'
    }
    
    all_installed = True
    for module, name in required.items():
        try:
            __import__(module)
            print(f"  ✓ {name} is installed")
        except ImportError:
            print(f"  ✗ {name} is NOT installed")
            all_installed = False
    
    return all_installed

def check_directory_structure():
    """Check if all required directories and files exist"""
    print("\nChecking directory structure...")
    required_items = [
        ('templates', True),
        ('static', True),
        ('models', True),
        ('templates/index.html', False),
        ('static/style.css', False),
        ('app.py', False),
        ('requirements.txt', False)
    ]
    
    all_exist = True
    for item, is_dir in required_items:
        path = os.path.join('.', item)
        exists = os.path.isdir(path) if is_dir else os.path.isfile(path)
        status = "✓" if exists else "✗"
        item_type = "Directory" if is_dir else "File"
        print(f"  {status} {item_type}: {item}")
        if not exists:
            all_exist = False
    
    return all_exist

def check_model_file():
    """Check if the trained model exists"""
    print("\nChecking for trained model...")
    model_path = os.path.join('models', 'improved_model.h5')
    if os.path.isfile(model_path):
        size_mb = os.path.getsize(model_path) / (1024 * 1024)
        print(f"  ✓ Model file found: improved_model.h5 ({size_mb:.2f} MB)")
        return True
    else:
        print("  ✗ Model file NOT found: models/improved_model.h5")
        print("    Please train the model using cnn-web-app.ipynb")
        return False

def main():
    print("=" * 60)
    print("CNN Web App - Setup Verification")
    print("=" * 60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Directory Structure", check_directory_structure),
        ("Model File", check_model_file)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            results.append(check_func())
        except Exception as e:
            print(f"\n  Error checking {name}: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    if all(results):
        print("✓ All checks passed! You're ready to run the app.")
        print("\nNext steps:")
        print("  1. Run: python app.py")
        print("  2. Open: http://localhost:5000")
    else:
        print("✗ Some checks failed. Please review the issues above.")
        print("\nTo fix:")
        if not results[1]:  # Dependencies
            print("  - Install dependencies: pip install -r requirements.txt")
        if not results[3]:  # Model
            print("  - Train model: jupyter notebook cnn-web-app.ipynb")
    
    print("=" * 60)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Setup script for Digital Divide Nepal Dashboard
This script helps install dependencies and provides instructions for running the dashboard.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("🔧 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def check_data_files():
    """Check if required data files exist"""
    print("📁 Checking for required data files...")
    
    required_files = [
        "data_processed/df_2001.csv",
        "data_processed/df_2011.csv", 
        "data_processed/df_2021.csv",
        "data_processed/df_combined.csv"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required data files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ All required data files found!")
        return True

def main():
    print("🇳🇵 Digital Divide Nepal Dashboard Setup")
    print("=" * 50)
    
    # Check data files
    data_ok = check_data_files()
    
    if not data_ok:
        print("\n⚠️  Please ensure all CSV files are in the data_processed/ folder before proceeding.")
        return
    
    # Install requirements
    install_ok = install_requirements()
    
    if install_ok:
        print("\n🎉 Setup completed successfully!")
        print("\n📋 To run the dashboard, use one of these commands:")
        print("   streamlit run digital_divide_dashboard.py")
        print("   python -m streamlit run digital_divide_dashboard.py")
        print("\n🌐 The dashboard will open in your web browser automatically.")
        print("   Default URL: http://localhost:8501")
    else:
        print("\n❌ Setup failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
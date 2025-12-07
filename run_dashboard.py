#!/usr/bin/env python3
"""
Simple launcher script for Digital Divide Nepal Dashboard
"""

import subprocess
import sys
import os
import webbrowser
import time

def main():
    print("🇳🇵 Starting Digital Divide Nepal Dashboard...")
    print("=" * 50)
    
    # Check if required files exist
    required_files = [
        "digital_divide_dashboard.py",
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
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease ensure all files are present before running the dashboard.")
        return
    
    print("✅ All required files found!")
    print("🚀 Starting Streamlit dashboard...")
    
    try:
        # Start the dashboard
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", 
            "digital_divide_dashboard.py", 
            "--server.port", "8501"
        ])
        
        print("🌐 Dashboard starting...")
        print("📱 URL: http://localhost:8501")
        print("⏳ Please wait a moment for the dashboard to load...")
        
        # Wait a bit then try to open browser
        time.sleep(3)
        try:
            webbrowser.open("http://localhost:8501")
            print("🎉 Dashboard opened in your browser!")
        except:
            print("💡 Please manually open http://localhost:8501 in your browser")
        
        print("\n" + "="*50)
        print("📋 Dashboard Controls:")
        print("   - Use the sidebar to select districts and analysis options")
        print("   - Choose between Overview, Comparative, Predictive, and Prescriptive analysis")
        print("   - Select different metrics to visualize")
        print("\n🛑 To stop the dashboard, press Ctrl+C in this terminal")
        print("="*50)
        
        # Wait for the process
        process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped by user")
        process.terminate()
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")
        print("💡 Try running manually: streamlit run digital_divide_dashboard.py")

if __name__ == "__main__":
    main()
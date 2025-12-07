"""
Master script to generate all district Internet Access Rate charts.
Calls all 8 district scripts sequentially to generate visualizations.
"""

import os
import sys
import subprocess

# List of all districts
districts = [
    "Dhanusha",
    "Mahottari",
    "Sarlahi",
    "Bara",
    "Parsa",
    "Rautahat",
    "Siraha",
    "Saptari"
]

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
codes_dir = os.path.join(script_dir, "codes", "internet_rise_plots")

# Change to the codes directory so relative paths work correctly
original_dir = os.getcwd()

print("=" * 60)
print("Generating Internet Access Rate Charts for All Districts")
print("=" * 60)
print()

# Ensure the output directory exists
output_dir = os.path.join(script_dir, "data_processed", "internet_rise_all_districts")
os.makedirs(output_dir, exist_ok=True)

# Run each district script
success_count = 0
failed_districts = []

for district in districts:
    script_name = f"{district.lower()}_internet_plot.py"
    script_path = os.path.join(codes_dir, script_name)
    
    if not os.path.exists(script_path):
        print(f"ERROR: Script not found: {script_path}")
        failed_districts.append(district)
        continue
    
    print(f"Processing {district}...")
    print("-" * 60)
    
    try:
        # Change to the script directory so relative paths work
        os.chdir(codes_dir)
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            cwd=codes_dir
        )
        
        if result.returncode == 0:
            print(result.stdout)
            print(f"SUCCESS: {district} chart generated")
            success_count += 1
        else:
            print(f"ERROR in {district}:")
            print(result.stderr)
            failed_districts.append(district)
    
    except Exception as e:
        print(f"ERROR processing {district}: {str(e)}")
        failed_districts.append(district)
    
    print()

# Change back to original directory
os.chdir(original_dir)

# Summary
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Total districts: {len(districts)}")
print(f"Successfully processed: {success_count}")
print(f"Failed: {len(failed_districts)}")

if failed_districts:
    print(f"Failed districts: {', '.join(failed_districts)}")
else:
    print("All charts generated successfully!")

print()
print(f"Charts saved to: {output_dir}")
print("=" * 60)


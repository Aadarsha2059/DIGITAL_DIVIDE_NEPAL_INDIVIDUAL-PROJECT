"""
Script to merge all three CSV files (2001, 2011, 2021) into a single DataFrame.
Adds a Year column and merges by District and Urban_Rural.
"""

import pandas as pd
import os

# Define file paths
data_dir = "data_processed"
files = {
    2001: os.path.join(data_dir, "df_2001.csv"),
    2011: os.path.join(data_dir, "df_2011.csv"),
    2021: os.path.join(data_dir, "df_2021.csv")
}

# Load and merge all datasets
dataframes = []

for year, file_path in files.items():
    print(f"Loading {year} data from {file_path}...")
    df = pd.read_csv(file_path)
    
    # Add Year column
    df['Year'] = year
    
    # If Internet_Access_Rate column doesn't exist (2001), add it with 0 values
    if 'Internet_Access_Rate' not in df.columns:
        df['Internet_Access_Rate'] = 0
        print(f"  Added Internet_Access_Rate column with 0 for {year}")
    
    dataframes.append(df)
    print(f"  Loaded {len(df)} rows")

# Combine all dataframes
df_combined = pd.concat(dataframes, ignore_index=True)

# Sort by District, Urban_Rural, and Year
df_combined = df_combined.sort_values(['District', 'Urban_Rural', 'Year']).reset_index(drop=True)

# Save merged CSV
output_path = os.path.join(data_dir, "df_combined.csv")
df_combined.to_csv(output_path, index=False)

print(f"\nMerged data saved to: {output_path}")
print(f"  Total rows: {len(df_combined)}")
print(f"  Columns: {list(df_combined.columns)}")
print(f"  Years: {sorted(df_combined['Year'].unique())}")
print(f"  Districts: {sorted(df_combined['District'].unique())}")


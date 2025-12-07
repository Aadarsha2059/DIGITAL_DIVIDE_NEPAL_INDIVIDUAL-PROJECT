"""
Generate Internet Access Rate trend chart for Mahottari District (2001-2021)
Shows Urban vs Rural comparison with smooth trend lines.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the base directory (project root)
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(script_dir, "..", "..")
base_dir = os.path.abspath(base_dir)

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 11

# Load merged data
data_path = os.path.join(base_dir, "data_processed", "df_combined.csv")
df = pd.read_csv(data_path)

# Filter for Mahottari district
district = "Mahottari"
df_district = df[df['District'] == district].copy()

# Prepare data for plotting
urban_data = df_district[df_district['Urban_Rural'] == 'Urban'].sort_values('Year')
rural_data = df_district[df_district['Urban_Rural'] == 'Rural'].sort_values('Year')

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot Urban line
ax.plot(urban_data['Year'], urban_data['Internet_Access_Rate'], 
        marker='o', linewidth=3, markersize=10, label='Urban', color='#2E86AB', linestyle='-')

# Plot Rural line
ax.plot(rural_data['Year'], rural_data['Internet_Access_Rate'], 
        marker='s', linewidth=3, markersize=10, label='Rural', color='#A23B72', linestyle='-')

# Add smooth trend lines using seaborn
sns.lineplot(data=urban_data, x='Year', y='Internet_Access_Rate', 
             ax=ax, color='#2E86AB', linestyle='--', alpha=0.5, linewidth=2)
sns.lineplot(data=rural_data, x='Year', y='Internet_Access_Rate', 
             ax=ax, color='#A23B72', linestyle='--', alpha=0.5, linewidth=2)

# Customize the plot
ax.set_xlabel('Year', fontsize=13, fontweight='bold')
ax.set_ylabel('Internet Access Rate (%)', fontsize=13, fontweight='bold')
ax.set_title(f'Internet Access Rise in {district} (2001–2021)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks([2001, 2011, 2021])
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(loc='best', fontsize=12, framealpha=0.9)

# Set y-axis to start from 0
ax.set_ylim(bottom=0)

# Save the plot
output_dir = os.path.join(base_dir, "data_processed", "internet_rise_all_districts")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, f"{district.lower()}_internet_2001_2021.png")
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Chart saved to: {output_path}")
plt.close()


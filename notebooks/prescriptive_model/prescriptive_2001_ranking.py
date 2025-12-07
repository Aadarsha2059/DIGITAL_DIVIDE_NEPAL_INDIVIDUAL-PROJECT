# ------------------------------
# Prescriptive Modeling - 2001
# ------------------------------

# Step 0: Imports and append src path
import sys
import os
sys.path.append(os.path.abspath("../../src"))  # points to src folder

import pandas as pd
import matplotlib.pyplot as plt

# Import prescriptive functions
from prescriptive_model.allocate_resources import load_processed_data, allocate_by_rank, assign_colors

# Step 1: Load processed 2001 dataset
df = load_processed_data("../../data_processed/df_2001.csv")

# Step 2: Rank districts and allocate budget
budget = 3  # number of districts to prioritize
df, recommended_districts = allocate_by_rank(df, tech='Electricity_Access_Rate', budget=budget)

print("Recommended districts for investment (lowest access first):")
print(recommended_districts)

# Step 3: Assign colors based on quartiles
colors = assign_colors(df, tech='Electricity_Access_Rate')

# Step 4: Display table with ranks and recommendations
print("\nDistricts with Rank and Recommended Flags:")
print(df[['Zone', 'District', 'Electricity_Access_Rate', 'Rank', 'Recommended']])

# Step 5: Bar chart visualization
plt.figure(figsize=(12,6))
bars = plt.bar(df['District'], df['Electricity_Access_Rate'], color=colors)
plt.ylim(0, 110)
plt.ylabel("Predicted Electricity Access Rate (%)")
plt.title(f"Electricity Access Rate (2001) - Prescriptive Modeling")

# Annotate each bar with index number safely
for idx, row in df.iterrows():
    plt.text(idx, row['Electricity_Access_Rate'] + 2, f"{idx+1}", ha='center', fontsize=10)

# Highlight recommended districts with black edge
for idx, rec in enumerate(df['Recommended']):
    if rec == 1:
        bars[idx].set_edgecolor('black')
        bars[idx].set_linewidth(2)

plt.xticks(rotation=45)
plt.tight_layout()

# Step 6: Save figure for thesis/report
plt.savefig("../../reports/prescriptive_results_2001_colored_ranked.png", dpi=300)

# Show plot
plt.show()

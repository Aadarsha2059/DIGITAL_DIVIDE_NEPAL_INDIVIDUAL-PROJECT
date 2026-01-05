"""
Comprehensive verification using the ACTUAL dashboard functions to verify thesis findings.
This uses the real priority scoring and budget allocation logic from the dashboard.
"""

import pandas as pd
import numpy as np
import sys
sys.path.append('.')

# Import the actual dashboard functions
from digital_divide_dashboard import (
    calculate_advanced_budget_allocation,
    safe_mean
)

# Load data
print("Loading data...")
df_2021 = pd.read_csv('data_processed/df_2021.csv')
df_2011 = pd.read_csv('data_processed/df_2011.csv')
df_combined = pd.read_csv('data_processed/df_combined.csv')

print("="*80)
print("COMPREHENSIVE THESIS FINDINGS VERIFICATION")
print("Using ACTUAL Dashboard Functions")
print("="*80)

# Helper function to calculate weighted average
def weighted_avg(district_data, metric, pop_col='Total_Population'):
    urban = district_data[district_data['Urban_Rural'] == 'Urban']
    rural = district_data[district_data['Urban_Rural'] == 'Rural']
    
    if urban.empty or rural.empty:
        return district_data[metric].mean()
    
    urban_val = urban[metric].values[0]
    rural_val = rural[metric].values[0]
    urban_pop = urban[pop_col].values[0]
    rural_pop = rural[pop_col].values[0]
    
    return (urban_val * urban_pop + rural_val * rural_pop) / (urban_pop + rural_pop)

print("\n" + "="*80)
print("1. BASIC DATA VERIFICATION")
print("="*80)

# Parsa gap
parsa_2021 = df_2021[df_2021['District'] == 'Parsa']
parsa_urban = parsa_2021[parsa_2021['Urban_Rural'] == 'Urban']['Internet_Access_Rate'].values[0]
parsa_rural = parsa_2021[parsa_2021['Urban_Rural'] == 'Rural']['Internet_Access_Rate'].values[0]
parsa_gap = parsa_urban - parsa_rural
print(f"\n[1.1] Parsa Urban-Rural Gap: {parsa_gap}% (Thesis: 34.5%)")
status = '[MATCH]' if abs(parsa_gap - 34.5) < 0.1 else '[MISMATCH]'
print(f"      Status: {status}")

# Siraha internet
siraha_2021 = df_2021[df_2021['District'] == 'Siraha']
siraha_internet = weighted_avg(siraha_2021, 'Internet_Access_Rate')
print(f"\n[1.2] Siraha Internet Access: {siraha_internet:.2f}% (Thesis: 14.3%)")
status = '[MATCH]' if abs(siraha_internet - 14.3) < 0.1 else '[MISMATCH]'
print(f"      Status: {status}")

# Mahottari internet
mahottari_2021 = df_2021[df_2021['District'] == 'Mahottari']
mahottari_internet = weighted_avg(mahottari_2021, 'Internet_Access_Rate')
print(f"\n[1.3] Mahottari Internet Access: {mahottari_internet:.2f}% (Thesis: 18%)")
status = '[MATCH]' if abs(mahottari_internet - 18.0) < 0.1 else '[MISMATCH]'
print(f"      Status: {status}")

# Electricity for outliers
siraha_electricity = weighted_avg(siraha_2021, 'Electricity_Access_Rate')
mahottari_electricity = weighted_avg(mahottari_2021, 'Electricity_Access_Rate')
print(f"\n[1.4] Siraha Electricity: {siraha_electricity:.1f}% (Thesis: >70%)")
status = '[MATCH]' if siraha_electricity > 70 else '[MISMATCH]'
print(f"      Status: {status}")
print(f"\n[1.5] Mahottari Electricity: {mahottari_electricity:.1f}% (Thesis: >70%)")
status = '[MATCH]' if mahottari_electricity > 70 else '[MISMATCH]'
print(f"      Status: {status}")

print("\n" + "="*80)
print("2. PRIORITY RANKING (Using Actual Dashboard Function)")
print("="*80)

# Use actual dashboard function
improvement_areas = ["Internet Access", "Electricity Access", "Digital Literacy"]
all_districts = sorted(df_combined['District'].unique())

priority_scores, clusters, kmeans = calculate_advanced_budget_allocation(
    df_combined, 
    100_000_000,  # NPR 100M
    "Balanced Development",
    improvement_areas,
    all_districts
)

if priority_scores:
    print("\n[2.1] Actual Priority Ranking from Dashboard:")
    for i, item in enumerate(priority_scores[:5], 1):
        print(f"      {i}. {item['District']}: Score {item['Priority_Score']:.2f}, Internet {item['Current_Internet']:.1f}%")
    
    expected_ranking = ['Siraha', 'Mahottari', 'Sarlahi', 'Bara', 'Parsa']
    actual_ranking = [item['District'] for item in priority_scores[:5]]
    
    print(f"\n[2.2] Expected Ranking: {expected_ranking}")
    print(f"      Actual Ranking:   {actual_ranking}")
    status = '[MATCH]' if actual_ranking == expected_ranking else '[MISMATCH]'
    print(f"      Status: {status}")
    
    # Check if Siraha is #1
    siraha_rank = next((i+1 for i, item in enumerate(priority_scores) if item['District'] == 'Siraha'), None)
    print(f"\n[2.3] Siraha Rank: #{siraha_rank} (Expected: #1)")
    status = '[MATCH]' if siraha_rank == 1 else '[MISMATCH]'
    print(f"      Status: {status}")

print("\n" + "="*80)
print("3. BUDGET ALLOCATION (Using Actual Dashboard Function)")
print("="*80)

if priority_scores:
    siraha_budget = next((item for item in priority_scores if item['District'] == 'Siraha'), None)
    if siraha_budget:
        print(f"\n[3.1] Siraha Budget Allocation:")
        print(f"      Percentage: {siraha_budget['Budget_Percentage']:.2f}%")
        print(f"      Amount: NPR {siraha_budget['Allocated_Budget']/1_000_000:.2f} million")
        print(f"      Thesis: ~15.2% (NPR 15.2M)")
        diff = abs(siraha_budget['Budget_Percentage'] - 15.2)
        status = '[MATCH]' if diff < 1.0 else f'[MISMATCH - differs by {diff:.2f}%]'
        print(f"      Status: {status}")

print("\n" + "="*80)
print("4. 2031 PROJECTION & GAP WIDENING")
print("="*80)

# Calculate projections using same method as dashboard
def calculate_projection(district_name):
    dist_historical = df_combined[df_combined['District'] == district_name].copy()
    if len(dist_historical) < 2:
        return None, None, None
    
    years = sorted(dist_historical['Year'].unique())
    if len(years) < 2:
        return None, None, None
    
    internet_2001 = safe_mean(dist_historical[dist_historical['Year'] == years[0]]['Internet_Access_Rate'], 0.0)
    internet_2021 = safe_mean(dist_historical[dist_historical['Year'] == years[-1]]['Internet_Access_Rate'], 0.0)
    
    if internet_2001 > 0:
        annual_growth = ((internet_2021 / internet_2001) ** (1.0 / (years[-1] - years[0]))) - 1
    elif internet_2021 > 0:
        annual_growth = 0.15
    else:
        annual_growth = 0.0
    
    internet_2031 = internet_2021 * ((1 + annual_growth) ** 10)
    internet_2031 = min(internet_2031, 100)
    
    return internet_2021, internet_2031, annual_growth * 100

bara_2021, bara_2031, bara_growth = calculate_projection('Bara')
siraha_2021, siraha_2031, siraha_growth = calculate_projection('Siraha')

if bara_2021 is not None and siraha_2021 is not None:
    gap_2021 = bara_2021 - siraha_2021
    gap_2031 = bara_2031 - siraha_2031
    gap_change = gap_2031 - gap_2021
    
    print(f"\n[4.1] Bara-Siraha Gap Analysis:")
    print(f"      2021: Bara {bara_2021:.1f}%, Siraha {siraha_2021:.1f}%, Gap: {gap_2021:.1f}%")
    print(f"      2031: Bara {bara_2031:.1f}%, Siraha {siraha_2031:.1f}%, Gap: {gap_2031:.1f}%")
    print(f"      Gap Change: +{gap_change:.1f} percentage points")
    print(f"      Thesis: Gap increases by 5.9 points")
    gap_diff = abs(gap_change - 5.9)
    status = '[MATCH]' if gap_diff < 1.0 else f'[MISMATCH - differs by {gap_diff:.1f} points]'
    print(f"      Status: {status}")
    
    print(f"\n[4.2] Growth Rates:")
    print(f"      Bara: {bara_growth:.2f}% annual (Thesis: Strong growth)")
    print(f"      Siraha: {siraha_growth:.2f}% annual (Thesis: Slower progress)")
    status = '[MATCH]' if bara_growth > siraha_growth and bara_growth > 4 else '[CHECK]'
    print(f"      Status: {status}")

print("\n" + "="*80)
print("5. K-MEANS CLUSTERING")
print("="*80)

if clusters is not None and priority_scores:
    # Check if Siraha and Mahottari are in high-need cluster (cluster 0)
    siraha_cluster = next((item['Cluster'] for item in priority_scores if item['District'] == 'Siraha'), None)
    mahottari_cluster = next((item['Cluster'] for item in priority_scores if item['District'] == 'Mahottari'), None)
    
    print(f"\n[5.1] Cluster Assignments:")
    print(f"      Siraha: Cluster {siraha_cluster} (Expected: 0 = high-need)")
    print(f"      Mahottari: Cluster {mahottari_cluster} (Expected: 0 = high-need)")
    status = '[MATCH]' if siraha_cluster == 0 and mahottari_cluster == 0 else '[CHECK]'
    print(f"      Status: {status}")

print("\n" + "="*80)
print("6. GENDER LITERACY GAP")
print("="*80)

gap_count = 0
for district in df_2021['District'].unique():
    dist_data = df_2021[df_2021['District'] == district]
    if not dist_data.empty:
        male_lit = dist_data['Literacy_Rate_Male'].values[0]
        female_lit = dist_data['Literacy_Rate_Female'].values[0]
        gap = male_lit - female_lit
        if abs(gap - 14) < 1:
            gap_count += 1

print(f"\n[6.1] Districts with 14-point gender gap: {gap_count}/8")
status = '[MATCH]' if gap_count >= 7 else '[CHECK]'
print(f"      Status: {status}")

print("\n" + "="*80)
print("FINAL SUMMARY")
print("="*80)

matches = []
mismatches = []

# Collect all results
if abs(parsa_gap - 34.5) < 0.1:
    matches.append("Parsa 34.5% gap")
else:
    mismatches.append("Parsa gap")

if abs(siraha_internet - 14.3) < 0.1:
    matches.append("Siraha 14.3% internet")
else:
    mismatches.append("Siraha internet")

if abs(mahottari_internet - 18.0) < 0.1:
    matches.append("Mahottari 18% internet")
else:
    mismatches.append("Mahottari internet")

if siraha_electricity > 70 and mahottari_electricity > 70:
    matches.append("Electricity >70% for outliers")
else:
    mismatches.append("Electricity outliers")

if priority_scores:
    actual_ranking = [item['District'] for item in priority_scores[:5]]
    if actual_ranking == ['Siraha', 'Mahottari', 'Sarlahi', 'Bara', 'Parsa']:
        matches.append("Priority ranking")
    else:
        mismatches.append("Priority ranking")
    
    siraha_budget = next((item for item in priority_scores if item['District'] == 'Siraha'), None)
    if siraha_budget and abs(siraha_budget['Budget_Percentage'] - 15.2) < 1.0:
        matches.append("Budget allocation (15.2%)")
    else:
        mismatches.append("Budget allocation")

if bara_2021 and siraha_2021:
    gap_change = (bara_2031 - siraha_2031) - (bara_2021 - siraha_2021)
    if abs(gap_change - 5.9) < 1.0:
        matches.append("2031 gap widening (5.9 points)")
    else:
        mismatches.append("2031 gap widening")

if gap_count >= 7:
    matches.append("Gender literacy gap (14 points)")
else:
    mismatches.append("Gender literacy gap")

print(f"\n[OK] MATCHING FINDINGS ({len(matches)}):")
for match in matches:
    print(f"   - {match}")

if mismatches:
    print(f"\n[!] MISMATCHES ({len(mismatches)}):")
    for mismatch in mismatches:
        print(f"   - {mismatch}")
else:
    print(f"\n[SUCCESS] ALL FINDINGS MATCH!")

print("\n" + "="*80)
print(f"OVERALL STATUS: {len(matches)}/{len(matches) + len(mismatches)} findings match")
print("="*80)


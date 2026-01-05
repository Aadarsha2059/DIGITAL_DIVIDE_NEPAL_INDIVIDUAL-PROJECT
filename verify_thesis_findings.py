"""
Comprehensive verification script to check if thesis findings match project results.
This script calculates all key metrics mentioned in the thesis and compares them.
"""

import pandas as pd
import numpy as np

# Load data
df_2021 = pd.read_csv('data_processed/df_2021.csv')
df_2011 = pd.read_csv('data_processed/df_2011.csv')
df_combined = pd.read_csv('data_processed/df_combined.csv')

print("="*80)
print("THESIS FINDINGS VERIFICATION REPORT")
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
print("1. URBAN-RURAL GAP ANALYSIS")
print("="*80)

# Check Parsa gap (thesis: 34.5 percentage points)
parsa_2021 = df_2021[df_2021['District'] == 'Parsa']
parsa_urban = parsa_2021[parsa_2021['Urban_Rural'] == 'Urban']['Internet_Access_Rate'].values[0]
parsa_rural = parsa_2021[parsa_2021['Urban_Rural'] == 'Rural']['Internet_Access_Rate'].values[0]
parsa_gap = parsa_urban - parsa_rural

print(f"\n[OK] Parsa Urban-Rural Gap:")
print(f"  Urban: {parsa_urban}%, Rural: {parsa_rural}%, Gap: {parsa_gap}%")
print(f"  Thesis states: 34.5% gap")
print(f"  Status: {'[MATCH]' if abs(parsa_gap - 34.5) < 0.1 else '[MISMATCH]'}")

# Check Siraha gap (thesis: smaller but significant)
siraha_2021 = df_2021[df_2021['District'] == 'Siraha']
siraha_urban = siraha_2021[siraha_2021['Urban_Rural'] == 'Urban']['Internet_Access_Rate'].values[0]
siraha_rural = siraha_2021[siraha_2021['Urban_Rural'] == 'Rural']['Internet_Access_Rate'].values[0]
siraha_gap = siraha_urban - siraha_rural

print(f"\n[OK] Siraha Urban-Rural Gap:")
print(f"  Urban: {siraha_urban}%, Rural: {siraha_rural}%, Gap: {siraha_gap}%")
print(f"  Status: {'[MATCH - smaller gap as stated]' if siraha_gap < parsa_gap else '[CHECK]'}")

print("\n" + "="*80)
print("2. INTERNET ACCESS RATES (2021)")
print("="*80)

# Siraha: 14.3% overall
siraha_internet = weighted_avg(siraha_2021, 'Internet_Access_Rate')
print(f"\n[OK] Siraha Internet Access:")
print(f"  Calculated: {siraha_internet:.2f}%")
print(f"  Thesis states: 14.3%")
print(f"  Status: {'[MATCH]' if abs(siraha_internet - 14.3) < 0.1 else '[MISMATCH]'}")

# Mahottari: 18% overall
mahottari_2021 = df_2021[df_2021['District'] == 'Mahottari']
mahottari_internet = weighted_avg(mahottari_2021, 'Internet_Access_Rate')
print(f"\n[OK] Mahottari Internet Access:")
print(f"  Calculated: {mahottari_internet:.2f}%")
print(f"  Thesis states: 18%")
print(f"  Status: {'[MATCH]' if abs(mahottari_internet - 18.0) < 0.1 else '[MISMATCH]'}")

print("\n" + "="*80)
print("3. ELECTRICITY ACCESS & OUTLIER DETECTION")
print("="*80)

# Check electricity >70% for Mahottari and Siraha
siraha_electricity = weighted_avg(siraha_2021, 'Electricity_Access_Rate')
mahottari_electricity = weighted_avg(mahottari_2021, 'Electricity_Access_Rate')

print(f"\n[OK] Siraha Electricity Access: {siraha_electricity:.1f}%")
print(f"  Thesis: >70% with internet 14.3%")
print(f"  Status: {'[MATCH - outlier pattern]' if siraha_electricity > 70 and siraha_internet < 20 else '[CHECK]'}")

print(f"\n[OK] Mahottari Electricity Access: {mahottari_electricity:.1f}%")
print(f"  Thesis: >70% with internet 18%")
print(f"  Status: {'[MATCH - outlier pattern]' if mahottari_electricity > 70 and mahottari_internet < 25 else '[CHECK]'}")

print("\n" + "="*80)
print("4. GENDER LITERACY GAP")
print("="*80)

# Check 14 percentage point gap
for district in df_2021['District'].unique():
    dist_data = df_2021[df_2021['District'] == district]
    if not dist_data.empty:
        male_lit = dist_data['Literacy_Rate_Male'].values[0]
        female_lit = dist_data['Literacy_Rate_Female'].values[0]
        gap = male_lit - female_lit
        status = "[OK]" if abs(gap - 14) < 1 else "[CHECK]"
        print(f"{status} {district}: Male {male_lit}%, Female {female_lit}%, Gap: {gap}%")

print("\n" + "="*80)
print("5. GROWTH RATES (2011-2021)")
print("="*80)

def calculate_growth_rate(district_name):
    dist_2011 = df_2011[df_2011['District'] == district_name]
    dist_2021 = df_2021[df_2021['District'] == district_name]
    
    internet_2011 = weighted_avg(dist_2011, 'Internet_Access_Rate')
    internet_2021 = weighted_avg(dist_2021, 'Internet_Access_Rate')
    
    if internet_2011 > 0:
        total_growth = ((internet_2021 / internet_2011) - 1) * 100
        annual_growth = ((internet_2021 / internet_2011) ** (1/10) - 1) * 100
    else:
        total_growth = 0
        annual_growth = 0
    
    return internet_2011, internet_2021, total_growth, annual_growth

# Bara: Strong growth
bara_2011_val, bara_2021_val, bara_total, bara_annual = calculate_growth_rate('Bara')
print(f"\n[OK] Bara Growth:")
print(f"  2011: {bara_2011_val:.2f}%, 2021: {bara_2021_val:.2f}%")
print(f"  Total Growth: {bara_total:.1f}% over 10 years")
print(f"  Annual Growth: {bara_annual:.2f}% per year")
print(f"  Status: {'[STRONG GROWTH]' if bara_annual > 4 else '[CHECK]'}")

# Parsa: Strong growth
parsa_2011_val, parsa_2021_val, parsa_total, parsa_annual = calculate_growth_rate('Parsa')
print(f"\n[OK] Parsa Growth:")
print(f"  2011: {parsa_2011_val:.2f}%, 2021: {parsa_2021_val:.2f}%")
print(f"  Total Growth: {parsa_total:.1f}% over 10 years")
print(f"  Annual Growth: {parsa_annual:.2f}% per year")
print(f"  Status: {'[STRONG GROWTH]' if parsa_annual > 4 else '[CHECK]'}")

# Siraha: Slower progress
siraha_2011_val, siraha_2021_val, siraha_total, siraha_annual = calculate_growth_rate('Siraha')
print(f"\n[OK] Siraha Growth:")
print(f"  2011: {siraha_2011_val:.2f}%, 2021: {siraha_2021_val:.2f}%")
print(f"  Total Growth: {siraha_total:.1f}% over 10 years")
print(f"  Annual Growth: {siraha_annual:.2f}% per year")
print(f"  Status: {'[SLOWER PROGRESS]' if siraha_annual < bara_annual and siraha_annual < parsa_annual else '[CHECK]'}")

print("\n" + "="*80)
print("6. 2031 PROJECTION & GAP WIDENING")
print("="*80)

# Calculate 2031 projections
def project_2031(district_name):
    dist_2011_val, dist_2021_val, _, annual_growth = calculate_growth_rate(district_name)
    
    # Convert annual growth to decimal
    annual_rate = annual_growth / 100
    
    # Project to 2031 (10 years from 2021)
    if annual_rate > 0:
        projected_2031 = dist_2021_val * ((1 + annual_rate) ** 10)
        projected_2031 = min(projected_2031, 100)  # Cap at 100%
    else:
        projected_2031 = dist_2021_val
    
    return dist_2021_val, projected_2031

bara_2021_proj, bara_2031_proj = project_2031('Bara')
siraha_2021_proj, siraha_2031_proj = project_2031('Siraha')

gap_2021 = bara_2021_proj - siraha_2021_proj
gap_2031 = bara_2031_proj - siraha_2031_proj
gap_change = gap_2031 - gap_2021

print(f"\n[OK] Bara-Siraha Gap Analysis:")
print(f"  2021: Bara {bara_2021_proj:.1f}%, Siraha {siraha_2021_proj:.1f}%, Gap: {gap_2021:.1f}%")
print(f"  2031: Bara {bara_2031_proj:.1f}%, Siraha {siraha_2031_proj:.1f}%, Gap: {gap_2031:.1f}%")
print(f"  Gap Change: +{gap_change:.1f} percentage points")
print(f"  Thesis states: Gap increases by 5.9 percentage points")
gap_diff = abs(gap_change - 5.9)
status = '[MATCH]' if gap_diff < 1.0 else f'[MISMATCH - differs by {gap_diff:.1f} points]'
print(f"  Status: {status}")

print("\n" + "="*80)
print("7. PRIORITY RANKING VERIFICATION")
print("="*80)

# Calculate priority scores (simplified version)
def calculate_priority_score(district_name):
    dist_2021 = df_2021[df_2021['District'] == district_name]
    
    internet = weighted_avg(dist_2021, 'Internet_Access_Rate')
    electricity = weighted_avg(dist_2021, 'Electricity_Access_Rate')
    literacy = weighted_avg(dist_2021, 'Literacy_Rate_Total')
    
    # Urban-rural gap
    urban_internet = dist_2021[dist_2021['Urban_Rural'] == 'Urban']['Internet_Access_Rate'].values[0]
    rural_internet = dist_2021[dist_2021['Urban_Rural'] == 'Rural']['Internet_Access_Rate'].values[0]
    gap = urban_internet - rural_internet
    
    # Need-based scoring (lower access = higher priority)
    internet_deficit = (100 - internet) / 100
    gap_component = min(gap / 50.0, 1.0)
    
    # Outlier detection
    is_outlier = (electricity > 70) and (internet < 25)
    outlier_boost = 0.25 if is_outlier and electricity > 89 else 0.20 if is_outlier else 0.0
    
    # Priority score components
    internet_score = (internet_deficit * 0.55 + gap_component * 0.20) * (1.0 + outlier_boost) * 45
    electricity_score = ((100 - electricity) / 100) * 30
    literacy_score = ((100 - literacy) / 100) * 25
    
    total_score = internet_score + electricity_score + literacy_score
    
    return {
        'District': district_name,
        'Internet': internet,
        'Electricity': electricity,
        'Priority_Score': total_score,
        'Is_Outlier': is_outlier
    }

districts_to_check = ['Siraha', 'Mahottari', 'Sarlahi', 'Bara', 'Parsa']
priority_results = []

for district in districts_to_check:
    result = calculate_priority_score(district)
    priority_results.append(result)

# Sort by priority score
priority_results.sort(key=lambda x: x['Priority_Score'], reverse=True)

print("\n[OK] Calculated Priority Ranking:")
for i, result in enumerate(priority_results, 1):
    outlier_marker = " (OUTLIER)" if result['Is_Outlier'] else ""
    print(f"  {i}. {result['District']}: Score {result['Priority_Score']:.1f}, Internet {result['Internet']:.1f}%{outlier_marker}")

expected_ranking = ['Siraha', 'Mahottari', 'Sarlahi', 'Bara', 'Parsa']
actual_ranking = [r['District'] for r in priority_results]

print(f"\n  Expected: {expected_ranking}")
print(f"  Actual:   {actual_ranking}")
print(f"  Status: {'[MATCH]' if actual_ranking == expected_ranking else '[MISMATCH]'}")

print("\n" + "="*80)
print("8. BUDGET ALLOCATION VERIFICATION")
print("="*80)

# Calculate budget allocation (proportional to priority scores)
total_score = sum([r['Priority_Score'] for r in priority_results])
budget_total = 100_000_000  # NPR 100 million

for result in priority_results:
    percentage = (result['Priority_Score'] / total_score) * 100
    allocated = (percentage / 100) * budget_total
    result['Budget_Percentage'] = percentage
    result['Allocated_Budget'] = allocated

siraha_budget = next(r for r in priority_results if r['District'] == 'Siraha')
print(f"\n[OK] Siraha Budget Allocation:")
print(f"  Percentage: {siraha_budget['Budget_Percentage']:.2f}%")
print(f"  Amount: NPR {siraha_budget['Allocated_Budget']/1_000_000:.2f} million")
print(f"  Thesis states: ~15.2% (NPR 15.2M)")
diff = abs(siraha_budget['Budget_Percentage'] - 15.2)
status = '[MATCH]' if diff < 2.0 else f'[MISMATCH - differs by {diff:.1f}%]'
print(f"  Status: {status}")

print("\n" + "="*80)
print("SUMMARY")
print("="*80)

print("\nKey Findings Verification:")
print("1. Parsa 34.5% urban-rural gap: [CHECK ABOVE]")
print("2. Siraha 14.3% internet access: [CHECK ABOVE]")
print("3. Mahottari 18% internet access: [CHECK ABOVE]")
print("4. Electricity >70% for outliers: [CHECK ABOVE]")
print("5. Gender literacy 14pt gap: [CHECK ABOVE]")
print("6. Bara/Parsa strong growth: [CHECK ABOVE]")
print("7. Siraha slower progress: [CHECK ABOVE]")
print("8. Priority ranking: [CHECK ABOVE]")
print("9. Budget allocation: [CHECK ABOVE]")
print("10. 2031 gap widening: [CHECK ABOVE]")

print("\n" + "="*80)


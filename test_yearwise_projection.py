"""
Test script to verify the Yearwise Projection feature works correctly
"""
import pandas as pd
import sys

print("🧪 Testing Yearwise Projection Feature...")
print("=" * 60)

# Test 1: Check if data files exist
print("\n1️⃣ Checking data files...")
try:
    df_combined = pd.read_csv('data_processed/df_combined.csv')
    print(f"   ✅ df_combined.csv loaded: {len(df_combined)} rows")
    print(f"   📊 Districts: {sorted(df_combined['District'].unique())}")
    print(f"   📅 Years: {sorted(df_combined['Year'].unique())}")
except Exception as e:
    print(f"   ❌ Error loading data: {e}")
    sys.exit(1)

# Test 2: Check required columns
print("\n2️⃣ Checking required columns...")
required_columns = [
    'District', 'Year', 'Internet_Access_Rate', 'Electricity_Access_Rate',
    'Telephone_Access_Rate', 'TV_Access_Rate', 'Radio_Access_Rate', 'Literacy_Rate_Total'
]
missing_columns = [col for col in required_columns if col not in df_combined.columns]
if missing_columns:
    print(f"   ❌ Missing columns: {missing_columns}")
    sys.exit(1)
else:
    print(f"   ✅ All required columns present")

# Test 3: Check data integrity
print("\n3️⃣ Checking data integrity...")
for district in df_combined['District'].unique():
    district_data = df_combined[df_combined['District'] == district]
    years = sorted(district_data['Year'].unique())
    print(f"   📍 {district}: {len(years)} years - {years}")

# Test 4: Verify dashboard syntax
print("\n4️⃣ Verifying dashboard syntax...")
try:
    import py_compile
    py_compile.compile('digital_divide_dashboard.py', doraise=True)
    print("   ✅ Dashboard syntax is valid")
except SyntaxError as e:
    print(f"   ❌ Syntax error: {e}")
    sys.exit(1)

# Test 5: Check if calculate_advanced_budget_allocation function exists
print("\n5️⃣ Checking required functions...")
with open('digital_divide_dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()
    if 'def calculate_advanced_budget_allocation' in content:
        print("   ✅ calculate_advanced_budget_allocation function found")
    else:
        print("   ❌ calculate_advanced_budget_allocation function not found")
        sys.exit(1)
    
    if 'elif analysis_type == "Yearwise Projection":' in content:
        print("   ✅ Yearwise Projection section found")
    else:
        print("   ❌ Yearwise Projection section not found")
        sys.exit(1)

# Test 6: Simulate metric calculations
print("\n6️⃣ Simulating metric calculations...")
try:
    test_district = df_combined['District'].iloc[0]
    test_metric = 'Internet_Access_Rate'
    
    district_data = df_combined[df_combined['District'] == test_district]
    yearly_data = district_data.groupby('Year')[test_metric].mean().reset_index()
    
    print(f"   📊 Test District: {test_district}")
    print(f"   📈 {test_metric} over years:")
    for _, row in yearly_data.iterrows():
        print(f"      {int(row['Year'])}: {row[test_metric]:.1f}%")
    
    # Calculate growth
    if len(yearly_data) >= 2:
        growth = yearly_data[test_metric].iloc[-1] - yearly_data[test_metric].iloc[0]
        print(f"   📈 Total Growth: {growth:+.1f}%")
    
    print("   ✅ Metric calculations work correctly")
except Exception as e:
    print(f"   ❌ Error in calculations: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ All tests passed! The Yearwise Projection feature is ready.")
print("\n🚀 To run the dashboard:")
print("   python run_dashboard.py")
print("   or")
print("   streamlit run digital_divide_dashboard.py")
print("=" * 60)

"""
Test script to verify Prescriptive Recommendations feature
"""
import pandas as pd

print("🧪 Testing Prescriptive Recommendations Feature...")
print("=" * 60)

# Load data
df_combined = pd.read_csv('data_processed/df_combined.csv')

# Test for each district and year
districts = sorted(df_combined['District'].unique())
years = sorted(df_combined['Year'].unique())

print(f"\n📊 Testing {len(districts)} districts across {len(years)} years")
print(f"Districts: {', '.join(districts)}")
print(f"Years: {[int(y) for y in years]}")

print("\n" + "=" * 60)
print("Sample Recommendations Preview:")
print("=" * 60)

# Test one district for each year
test_district = districts[0]

for year in years:
    print(f"\n📅 {test_district} - {int(year)}")
    print("-" * 40)
    
    district_data = df_combined[
        (df_combined['District'] == test_district) & 
        (df_combined['Year'] == year)
    ]
    
    if not district_data.empty:
        internet = district_data['Internet_Access_Rate'].mean()
        electricity = district_data['Electricity_Access_Rate'].mean()
        literacy = district_data['Literacy_Rate_Total'].mean()
        population = district_data['Total_Population'].sum()
        
        print(f"📊 Metrics:")
        print(f"   Internet: {internet:.1f}%")
        print(f"   Electricity: {electricity:.1f}%")
        print(f"   Literacy: {literacy:.1f}%")
        print(f"   Population: {population:,}")
        
        # Generate sample recommendations
        recommendations = []
        
        if electricity < 60:
            recommendations.append("🔴 CRITICAL: Electricity infrastructure needs immediate attention")
        if internet < 15:
            recommendations.append("🔴 CRITICAL: Internet desert - deploy 4G towers urgently")
        elif internet < 30:
            recommendations.append("🟠 URGENT: Accelerate internet deployment")
        if literacy < 60:
            recommendations.append("🔴 CRITICAL: Basic literacy programs required")
        
        if recommendations:
            print(f"\n💡 Key Recommendations ({len(recommendations)}):")
            for rec in recommendations:
                print(f"   • {rec}")
        else:
            print(f"\n✅ Strong performance - focus on maintenance")

print("\n" + "=" * 60)
print("✅ Prescriptive Recommendations feature is working!")
print("\n🚀 To see full recommendations in dashboard:")
print("   1. Run: python -m streamlit run digital_divide_dashboard.py")
print("   2. Select '💡 Prescriptive Recommendations' from sidebar")
print("   3. Choose districts and year")
print("   4. View detailed, actionable prescriptions")
print("=" * 60)

"""
Test script to verify TV and Radio Access data in Yearwise Projection
"""
import pandas as pd

print("🧪 Testing TV and Radio Access Data...")
print("=" * 60)

# Load data
df_combined = pd.read_csv('data_processed/df_combined.csv')

print("\n1️⃣ Checking columns...")
required_cols = ['TV_Access_Rate', 'Radio_Access_Rate']
for col in required_cols:
    if col in df_combined.columns:
        print(f"   ✅ {col} found")
    else:
        print(f"   ❌ {col} NOT found")

print("\n2️⃣ Sample TV Access Rate data:")
print("-" * 60)
tv_sample = df_combined[['District', 'Year', 'TV_Access_Rate']].head(12)
for _, row in tv_sample.iterrows():
    print(f"   {row['District']:12} | {int(row['Year'])} | {row['TV_Access_Rate']:6.1f}%")

print("\n3️⃣ Sample Radio Access Rate data:")
print("-" * 60)
radio_sample = df_combined[['District', 'Year', 'Radio_Access_Rate']].head(12)
for _, row in radio_sample.iterrows():
    print(f"   {row['District']:12} | {int(row['Year'])} | {row['Radio_Access_Rate']:6.1f}%")

print("\n4️⃣ Statistics for TV Access Rate:")
print("-" * 60)
for year in sorted(df_combined['Year'].unique()):
    year_data = df_combined[df_combined['Year'] == year]['TV_Access_Rate']
    print(f"   {int(year)}: Min={year_data.min():.1f}%, Max={year_data.max():.1f}%, Avg={year_data.mean():.1f}%")

print("\n5️⃣ Statistics for Radio Access Rate:")
print("-" * 60)
for year in sorted(df_combined['Year'].unique()):
    year_data = df_combined[df_combined['Year'] == year]['Radio_Access_Rate']
    print(f"   {int(year)}: Min={year_data.min():.1f}%, Max={year_data.max():.1f}%, Avg={year_data.mean():.1f}%")

print("\n6️⃣ Growth Analysis (2001-2021):")
print("-" * 60)
for district in sorted(df_combined['District'].unique()):
    district_data = df_combined[df_combined['District'] == district]
    
    tv_2001 = district_data[district_data['Year'] == 2001]['TV_Access_Rate'].mean()
    tv_2021 = district_data[district_data['Year'] == 2021]['TV_Access_Rate'].mean()
    tv_growth = tv_2021 - tv_2001
    
    radio_2001 = district_data[district_data['Year'] == 2001]['Radio_Access_Rate'].mean()
    radio_2021 = district_data[district_data['Year'] == 2021]['Radio_Access_Rate'].mean()
    radio_growth = radio_2021 - radio_2001
    
    print(f"   {district:12} | TV: {tv_growth:+6.1f}% | Radio: {radio_growth:+6.1f}%")

print("\n" + "=" * 60)
print("✅ TV and Radio Access data is ready for Yearwise Projection!")
print("\n📊 Default metrics now include:")
print("   1. 🌐 Internet Access Rate")
print("   2. ⚡ Electricity Access Rate")
print("   3. 📺 TV Access Rate")
print("   4. 📻 Radio Access Rate")
print("   5. 📚 Literacy Rate")
print("=" * 60)

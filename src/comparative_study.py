import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_comparative_study(df_2001, df_2011, df_2021):
    # Add a 'Year' column to each DataFrame for easier merging and plotting
    df_2001['Year'] = 2001
    df_2011['Year'] = 2011
    df_2021['Year'] = 2021

    # Combine all dataframes
    combined_df = pd.concat([df_2001, df_2011, df_2021], ignore_index=True)

    # Ensure numeric columns are actually numeric
    numeric_cols = [
        'Total_Population', 'Male', 'Female',
        'Literacy_Rate_Total', 'Literacy_Rate_Male', 'Literacy_Rate_Female', 'Literacy_Rate_Youth',
        'Households_Total', 'Households_with_Electricity', 'Households_with_Radio',
        'Households_with_TV', 'Households_with_Telephone',
        'Electricity_Access_Rate', 'Radio_Access_Rate', 'TV_Access_Rate', 'Telephone_Access_Rate',
        'Internet_Access_Rate'
    ]
    for col in numeric_cols:
        if col in combined_df.columns:
            combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce')

    print("\n--- Comparative Study Results ---")

    # Ensure output directory exists
    output_dir = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\reports\visualized_images_2021"
    os.makedirs(output_dir, exist_ok=True)

    # --- Existing Visualizations ---
    # Overall Literacy Rate Trend
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=combined_df, x='Year', y='Literacy_Rate_Total', hue='Urban_Rural', marker='o', errorbar=None)
    plt.title('Overall Literacy Rate Trend (2001-2021)')
    plt.ylabel('Literacy Rate (%)')
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'literacy_rate_trend.png'))
    plt.close()
    print("Generated: literacy_rate_trend.png")

    # Internet Access Rate Trend (only 2011 and 2021 available)
    internet_df = combined_df[combined_df['Internet_Access_Rate'].notna()]
    if not internet_df.empty:
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=internet_df, x='Year', y='Internet_Access_Rate', hue='Urban_Rural', marker='o', errorbar=None)
        plt.title('Internet Access Rate Trend (2011-2021)')
        plt.ylabel('Internet Access Rate (%)')
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, 'internet_access_trend.png'))
        plt.close()
        print("Generated: internet_access_trend.png")
    else:
        print("Internet Access Rate data not sufficient for trend visualization.")

    # Electricity Access Rate Trend
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=combined_df, x='Year', y='Electricity_Access_Rate', hue='Urban_Rural', marker='o', errorbar=None)
    plt.title('Electricity Access Rate Trend (2001-2021)')
    plt.ylabel('Electricity Access Rate (%)')
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'electricity_access_trend.png'))
    plt.close()
    print("Generated: electricity_access_trend.png")

    # --- New Visualizations for 2021 District-wise Ratios ---
    df_2021_filtered = combined_df[combined_df['Year'] == 2021].copy()

    # Pie Chart: Urban vs Rural Population for a specific district (e.g., Dhanusha) in 2021
    dhanusha_2021 = df_2021_filtered[df_2021_filtered['District'] == 'Dhanusha']
    if not dhanusha_2021.empty:
        urban_pop = dhanusha_2021[dhanusha_2021['Urban_Rural'] == 'Urban']['Total_Population'].sum()
        rural_pop = dhanusha_2021[dhanusha_2021['Urban_Rural'] == 'Rural']['Total_Population'].sum()
        
        if urban_pop > 0 or rural_pop > 0:
            labels = ['Urban', 'Rural']
            sizes = [urban_pop, rural_pop]
            colors = ['#66b3ff', '#99ff99']
            explode = (0.1, 0)  # explode 1st slice

            plt.figure(figsize=(8, 8))
            plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title('Dhanusha District Population Distribution (Urban vs. Rural) - 2021')
            plt.savefig(os.path.join(output_dir, 'dhanusha_2021_urban_rural_pie.png'))
            plt.close()
            print("Generated: dhanusha_2021_urban_rural_pie.png")

    # Bar Graph: Literacy Rate per District for 2021
    literacy_2021_district = df_2021_filtered.groupby('District')['Literacy_Rate_Total'].mean().reset_index()
    plt.figure(figsize=(12, 7))
    sns.barplot(x='Literacy_Rate_Total', y='District', data=literacy_2021_district.sort_values(by='Literacy_Rate_Total', ascending=False), palette='coolwarm')
    plt.title('Total Literacy Rate per District - 2021 (Extrapolated)')
    plt.xlabel('Literacy Rate (%)')
    plt.ylabel('District')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '2021_district_literacy_bar.png'))
    plt.close()
    print("Generated: 2021_district_literacy_bar.png")

    # --- Internet Access Comparison (2011 vs. 2021 per District) ---
    internet_access_comparison = combined_df[combined_df['Year'].isin([2011, 2021])].copy()
    internet_access_comparison = internet_access_comparison.groupby(['District', 'Year'])['Internet_Access_Rate'].mean().reset_index()

    plt.figure(figsize=(14, 8))
    sns.barplot(x='District', y='Internet_Access_Rate', hue='Year', data=internet_access_comparison, palette='viridis')
    plt.title('Internet Access Rate Comparison per District (2011 vs. 2021)')
    plt.xlabel('District')
    plt.ylabel('Internet Access Rate (%)')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Year')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'internet_access_district_comparison_2011_2021.png'))
    plt.close()
    print("Generated: internet_access_district_comparison_2011_2021.png")

    print("All requested visualizations generated and saved in reports/visualized_images_2021/")

if __name__ == "__main__":
    # Define paths
    path_2001 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2001.csv"
    path_2011 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2011.csv"
    path_2021 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2021.csv"
    
    # Create the directory for visualized images if it doesn't exist
    output_dir = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\reports\visualized_images_2021"
    os.makedirs(output_dir, exist_ok=True)

    # Load data
    df_2001 = pd.read_csv(path_2001)
    df_2011 = pd.read_csv(path_2011)
    df_2021 = pd.read_csv(path_2021)

    # Perform comparative study and generate new visualizations
    perform_comparative_study(df_2001, df_2011, df_2021)
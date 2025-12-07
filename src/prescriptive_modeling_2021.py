import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_prescriptive_modeling(df_2021):
    print("\n--- Prescriptive Modeling Results ---")

    # Ensure Internet_Access_Rate is numeric
    df_2021['Internet_Access_Rate'] = pd.to_numeric(df_2021['Internet_Access_Rate'], errors='coerce')

    # Drop rows where Internet_Access_Rate is NaN (if any)
    df_2021_cleaned = df_2021.dropna(subset=['Internet_Access_Rate']).copy()

    # Rank areas by Internet Access Rate (lowest first = highest need)
    df_2021_cleaned['Rank'] = df_2021_cleaned['Internet_Access_Rate'].rank(ascending=True)

    # Sort by rank to see areas with highest need
    ranked_areas = df_2021_cleaned.sort_values(by='Rank').reset_index(drop=True)

    print("Top 5 Areas with Lowest Internet Access Rate (Highest Need for Intervention):")
    print(ranked_areas[['Zone', 'District', 'Urban_Rural', 'Internet_Access_Rate', 'Rank']].head(5))

    # Visualize the ranking of Internet Access Rate
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Internet_Access_Rate', y=ranked_areas[['District', 'Urban_Rural']].apply(lambda x: f"{x[0]} ({x[1]})", axis=1), data=ranked_areas.head(10), palette='viridis')
    plt.title('Top 10 Areas by Internet Access Rate (2021 Extrapolated) - Lowest First')
    plt.xlabel('Internet Access Rate (%)')
    plt.ylabel('Area')
    plt.tight_layout()
    plt.savefig(r'C:\Users\User\Desktop\DIGITAL_DIVIDE\reports\visualized_images_2021\prescriptive_internet_access_ranking.png')
    plt.close()
    print("Generated: prescriptive_internet_access_ranking.png")

    print("Prescriptive modeling complete. Visualizations saved in reports/visualized_images_2021/")

if __name__ == "__main__":
    # Define paths
    path_2021 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2021.csv"
    
    # Create the directory for visualized images if it doesn't exist
    import os
    output_dir = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\reports\visualized_images_2021"
    os.makedirs(output_dir, exist_ok=True)

    # Load data
    df_2021 = pd.read_csv(path_2021)

    # Perform prescriptive modeling
    perform_prescriptive_modeling(df_2021)

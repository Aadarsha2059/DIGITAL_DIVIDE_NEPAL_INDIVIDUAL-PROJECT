# File: DIGITAL_DIVIDE/src/prescriptive_model/allocate_resources.py

import pandas as pd

def load_processed_data(path="../../data_processed/df_2001.csv"):
    """
    Load processed 2001 dataset with predicted access rates.
    """
    df = pd.read_csv(path)
    return df

def allocate_by_rank(df, tech='Electricity_Access_Rate', budget=3):
    """
    Rank districts based on technology access.
    Lowest access = rank 1. Recommend 'budget' lowest-access districts.
    
    Returns:
        df: DataFrame with Rank and Recommended columns
        recommended_districts: list of recommended districts
    """
    df['Rank'] = df[tech].rank(method='min', ascending=True)
    df['Recommended'] = df['Rank'].apply(lambda x: 1 if x <= budget else 0)
    recommended_districts = df[df['Recommended']==1]['District'].tolist()
    return df, recommended_districts

def assign_colors(df, tech='Electricity_Access_Rate'):
    """
    Assign colors for prescriptive visualization based on quantiles.
    Returns a list of colors for plotting.
    """
    q1 = df[tech].quantile(0.25)
    q2 = df[tech].quantile(0.5)
    q3 = df[tech].quantile(0.75)
    
    colors = []
    for val in df[tech]:
        if val <= q1:
            colors.append('red')        # lowest 25% -> poor
        elif val <= q2:
            colors.append('orange')     # 25-50% -> moderate-low
        elif val <= q3:
            colors.append('blue')       # 50-75% -> moderate-high
        else:
            colors.append('green')      # top 25% -> high
    return colors

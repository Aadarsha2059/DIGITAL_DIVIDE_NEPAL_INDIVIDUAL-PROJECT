import pandas as pd

def extrapolate_2021_data(df_2001, df_2011):
    df_2021 = df_2011.copy()
    
    # Columns to extrapolate (excluding 'Internet_Access_Rate' for now)
    extrapolate_cols = [
        'Total_Population', 'Male', 'Female',
        'Literacy_Rate_Total', 'Literacy_Rate_Male', 'Literacy_Rate_Female', 'Literacy_Rate_Youth',
        'Households_Total', 'Households_with_Electricity', 'Households_with_Radio',
        'Households_with_TV', 'Households_with_Telephone',
        'Electricity_Access_Rate', 'Radio_Access_Rate', 'TV_Access_Rate', 'Telephone_Access_Rate'
    ]

    # Calculate growth rates or differences between 2001 and 2011
    # Assuming a linear extrapolation for simplicity over a decade (2001 to 2011)
    # And applying that same growth for 2011 to 2021
    for col in extrapolate_cols:
        # Ensure columns are numeric, coercing errors to NaN
        df_2001[col] = pd.to_numeric(df_2001[col], errors='coerce')
        df_2011[col] = pd.to_numeric(df_2011[col], errors='coerce')

        # Calculate the decadal change
        change = df_2011[col] - df_2001[col]
        
        # Extrapolate for 2021
        df_2021[col] = df_2011[col] + change
        
        # Ensure rates do not exceed 100 or go below 0
        if 'Rate' in col:
            df_2021[col] = df_2021[col].clip(lower=0, upper=100)
        else:
            df_2021[col] = df_2021[col].clip(lower=0) # Population/Household counts shouldn't be negative

    # Special handling for 'Internet_Access_Rate'
    # It only exists in 2011. Let's assume a significant growth, e.g., 50% increase from 2011 to 2021
    # This is an assumption and can be adjusted.
    if 'Internet_Access_Rate' in df_2011.columns:
        df_2021['Internet_Access_Rate'] = df_2011['Internet_Access_Rate'] * 1.5
        df_2021['Internet_Access_Rate'] = df_2021['Internet_Access_Rate'].clip(lower=0, upper=100)
    else:
        # If for some reason it's not in 2011, initialize it with a default or 0
        df_2021['Internet_Access_Rate'] = 0.0

    return df_2021

if __name__ == "__main__":
    # Define paths
    path_2001 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2001.csv"
    path_2011 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2011.csv"
    path_2021_output = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2021.csv"

    # Load data
    df_2001 = pd.read_csv(path_2001)
    df_2011 = pd.read_csv(path_2011)

    # Extrapolate
    df_2021 = extrapolate_2021_data(df_2001, df_2011)

    # Save the extrapolated data
    df_2021.to_csv(path_2021_output, index=False)
    print(f"df_2021.csv created successfully at {path_2021_output}")

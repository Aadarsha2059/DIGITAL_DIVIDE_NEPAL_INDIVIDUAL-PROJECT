import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def perform_predictive_modeling(df_2001, df_2011, df_2021):
    # Add a 'Year' column to each DataFrame
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
        'Internet_Access_Rate', 'Year'
    ]
    for col in numeric_cols:
        if col in combined_df.columns:
            combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce')

    # Drop rows with NaN values in target or features for simplicity
    # For a real-world scenario, more sophisticated imputation would be used
    model_df = combined_df.dropna(subset=['Internet_Access_Rate']).copy()

    # Feature Engineering: Convert categorical variables to numerical using one-hot encoding
    model_df = pd.get_dummies(model_df, columns=['Zone', 'District', 'Urban_Rural'], drop_first=True)

    # Define features (X) and target (y)
    # Exclude the target itself and other non-feature columns
    features = [col for col in model_df.columns if col not in [
        'Internet_Access_Rate', 'Male', 'Female', 'Households_Total', # Exclude highly correlated or redundant features
        'Households_with_Electricity', 'Households_with_Radio', 'Households_with_TV', 'Households_with_Telephone'
    ]]
    
    # Ensure all features are numeric and handle potential boolean columns from get_dummies
    for col in features:
        if model_df[col].dtype == bool:
            model_df[col] = model_df[col].astype(int)

    X = model_df[features]
    y = model_df['Internet_Access_Rate']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Random Forest Regressor model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"\n--- Predictive Modeling Results ---")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared: {r2:.2f}")

    # Feature Importance
    feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    print("\nTop 10 Feature Importances:")
    print(feature_importances.head(10))

    # Plot Feature Importances
    plt.figure(figsize=(12, 7))
    sns.barplot(x=feature_importances.head(10), y=feature_importances.head(10).index)
    plt.title('Top 10 Feature Importances for Internet Access Rate Prediction')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.tight_layout()
    plt.savefig(r'C:\Users\User\Desktop\DIGITAL_DIVIDE\reports\visualized_images_2021\feature_importance_internet_access.png')
    plt.close()
    print("Generated: feature_importance_internet_access.png")

    print("Predictive modeling complete. Visualizations saved in reports/visualized_images_2021/")

if __name__ == "__main__":
    # Define paths
    path_2001 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2001.csv"
    path_2011 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2011.csv"
    path_2021 = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\data_processed\df_2021.csv"
    
    # Create the directory for visualized images if it doesn't exist
    import os
    output_dir = r"C:\Users\User\Desktop\DIGITAL_DIVIDE\reports\visualized_images_2021"
    os.makedirs(output_dir, exist_ok=True)

    # Load data
    df_2001 = pd.read_csv(path_2001)
    df_2011 = pd.read_csv(path_2011)
    df_2021 = pd.read_csv(path_2021)

    # Perform predictive modeling
    perform_predictive_modeling(df_2001, df_2011, df_2021)

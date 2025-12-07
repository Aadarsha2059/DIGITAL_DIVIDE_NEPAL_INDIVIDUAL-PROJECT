# src/random_forest_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def load_data(path="../data_processed/df_2001.csv"):
    df = pd.read_csv(path)
    return df

def prepare_features(df):
    # Features and target
    X = df[['Total_Population','Male','Female','Literacy_Rate_Male','Literacy_Rate_Female']]
    y = df['Electricity_Access_Rate']
    return X, y

def train_random_forest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    y_pred = rf_model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Random Forest Regression Results")
    print(f"MSE: {mse:.2f}, R²: {r2:.2f}")
    
    return rf_model, X_test, y_test, y_pred

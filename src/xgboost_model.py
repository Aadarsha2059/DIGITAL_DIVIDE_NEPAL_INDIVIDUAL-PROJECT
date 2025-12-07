# src/xgboost_model.py

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def load_data(path="../data_processed/df_2001.csv"):
    """Load processed 2001 dataset"""
    df = pd.read_csv(path)
    return df

def prepare_features(df, target="Electricity_Access_Rate"):
    """
    Prepare feature matrix X and target vector y
    target: choose 'Electricity_Access_Rate', 'TV_Access_Rate', 'Telephone_Access_Rate', 'Radio_Access_Rate'
    """
    features = ['Total_Population','Male','Female','Literacy_Rate_Male','Literacy_Rate_Female']
    X = df[features]
    y = df[target]
    return X, y

def train_xgboost(X, y):
    """Train XGBoost regressor and return predictions"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = xgb.XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    # Evaluate
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("XGBoost Regression Results")
    print(f"MSE: {mse:.2f}, R²: {r2:.2f}")
    
    return model, X_test, y_test, y_pred

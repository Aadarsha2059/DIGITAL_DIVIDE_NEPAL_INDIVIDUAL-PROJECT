import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_data(path="../data_processed/df_2001.csv"):
    df = pd.read_csv(path)
    return df

def prepare_features(df):
    # Select features for prediction
    X = df[['Total_Population','Male','Female','Literacy_Rate_Male','Literacy_Rate_Female']]
    y = df['Electricity_Access_Rate']  # target
    return X, y

def train_predictive_model(X, y):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Evaluate
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R2 Score: {r2:.2f}")
    
    return model, X_test, y_test, y_pred

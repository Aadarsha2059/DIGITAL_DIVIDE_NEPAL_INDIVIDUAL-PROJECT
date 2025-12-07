import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Simple test to see if Streamlit works
st.title("🇳🇵 Digital Divide Nepal Dashboard - Test")
st.write("Testing dashboard functionality...")

# Test data loading
try:
    st.write("Loading data files...")
    df_2001 = pd.read_csv('data_processed/df_2001.csv')
    df_2011 = pd.read_csv('data_processed/df_2011.csv')
    df_2021 = pd.read_csv('data_processed/df_2021.csv')
    df_combined = pd.read_csv('data_processed/df_combined.csv')
    
    st.success("✅ All data files loaded successfully!")
    
    # Show basic info
    st.write(f"df_2001 shape: {df_2001.shape}")
    st.write(f"df_2011 shape: {df_2011.shape}")
    st.write(f"df_2021 shape: {df_2021.shape}")
    st.write(f"df_combined shape: {df_combined.shape}")
    
    # Show sample data
    st.subheader("Sample Data from df_combined:")
    st.dataframe(df_combined.head())
    
    # Show available districts
    districts = sorted(df_combined['District'].unique())
    st.write(f"Available districts: {districts}")
    
    # Simple chart test
    st.subheader("Test Chart:")
    if 'Internet_Access_Rate' in df_combined.columns:
        fig = px.line(df_combined.groupby('Year')['Internet_Access_Rate'].mean().reset_index(), 
                     x='Year', y='Internet_Access_Rate', 
                     title='Average Internet Access Rate Over Time')
        st.plotly_chart(fig)
    
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.write("Please check if the CSV files exist in the data_processed folder.")

st.write("If you see this message, Streamlit is working correctly!")
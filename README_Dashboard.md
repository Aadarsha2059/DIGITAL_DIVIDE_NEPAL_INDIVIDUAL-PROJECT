# 🇳🇵 Digital Divide Nepal Dashboard

An interactive web-based dashboard for analyzing digital infrastructure and access patterns across Nepal's districts from 2001 to 2021.

## 🌟 Enhanced Features

### 📊 **Interactive Analysis**
- **District Comparison**: Compare digital metrics between any two districts
- **Year Selection**: Analyze data across different census years (2001, 2011, 2021)
- **Multiple Metrics**: Internet, electricity, TV, radio, telephone access rates, and literacy rates

### 🎨 **Custom Visualizations** ⭐ NEW
- **7 Chart Types**: Line, Bar, Pie, Histogram, Box Plot, Scatter Plot, Heatmap
- **Flexible Filtering**: Choose districts, metrics, and years
- **Interactive Controls**: Real-time chart updates based on selections
- **Export Options**: Download charts and underlying data

### 💰 **Smart Budget Allocation** ⭐ NEW
- **Investment Planning**: Allocate budgets across districts intelligently
- **Priority Scoring**: AI-powered priority ranking based on need and impact
- **4 Investment Types**: Internet, Electricity, Telephone, Digital Literacy
- **Visual Budget Distribution**: Interactive charts showing optimal allocation
- **ROI Predictions**: Expected impact of investments

### 📥 **Data Downloads** ⭐ NEW
- **Multiple Formats**: CSV and Excel downloads
- **Complete Datasets**: All census years (2001, 2011, 2021)
- **Filtered Data**: Download specific districts or years
- **Data Dictionary**: Complete column descriptions
- **Usage Guidelines**: Licensing and citation information

### 🔮 **Predictive Modeling**
- **Trend Analysis**: Polynomial regression models to predict future trends
- **R² Score Display**: Model accuracy indicators
- **5-Year Forecasts**: Predictions for digital access rates

### 💡 **Prescriptive Recommendations**
- **Data-Driven Insights**: Automated recommendations based on current metrics
- **Priority Identification**: Critical, high, and medium priority areas
- **Strategic Guidance**: Infrastructure and policy recommendations

### 🎨 **Enhanced UI/UX** ⭐ NEW
- **Gradient Backgrounds**: Beautiful color schemes throughout
- **Responsive Design**: Works on all screen sizes
- **Interactive Elements**: Hover effects and smooth transitions
- **Professional Styling**: Modern card-based layouts
- **Intuitive Navigation**: Clear section organization

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Required CSV files in `data_processed/` folder:
  - `df_2001.csv`
  - `df_2011.csv`
  - `df_2021.csv`
  - `df_combined.csv`

### Installation & Setup

1. **Automated Setup** (Recommended):
   ```bash
   python setup_dashboard.py
   ```

2. **Manual Setup**:
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Run the dashboard
   streamlit run digital_divide_dashboard.py
   ```

### 🖥️ **Running the Dashboard**

**Option 1: Using Streamlit directly**
```bash
streamlit run digital_divide_dashboard.py
```

**Option 2: Using Python module**
```bash
python -m streamlit run digital_divide_dashboard.py
```

**Option 3: With custom port**
```bash
streamlit run digital_divide_dashboard.py --server.port 8502
```

The dashboard will automatically open in your web browser at `http://localhost:8501`

## 📱 Dashboard Usage

### 🎛️ **Sidebar Controls**
- **District Selection**: Choose two districts for comparison
- **Year Selection**: Select census year for analysis
- **Analysis Type**: Choose from four analysis modes
- **Metrics Selection**: Select which metrics to display

### 📋 **Analysis Modes**

1. **Overview**: 
   - Key metrics summary for selected districts
   - Population demographics
   - Urban vs Rural breakdown

2. **Comparative Analysis**:
   - Side-by-side district comparisons
   - Interactive trend charts
   - Summary comparison tables

3. **Predictive Modeling**:
   - Future trend predictions (5-year forecast)
   - Model accuracy indicators
   - Trend direction analysis

4. **Prescriptive Recommendations**:
   - Data-driven policy recommendations
   - Priority area identification
   - Strategic development guidance

## 📊 Available Metrics

- **Internet Access Rate**: Percentage of households with internet access
- **Electricity Access Rate**: Percentage of households with electricity
- **TV Access Rate**: Percentage of households with television
- **Radio Access Rate**: Percentage of households with radio
- **Telephone Access Rate**: Percentage of households with telephone
- **Literacy Rate Total**: Overall literacy percentage

## 🔧 Technical Details

### **Built With**
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning for predictions
- **NumPy**: Numerical computations

### **Predictive Models**
- **Polynomial Regression**: Automatic degree selection (1-3)
- **R² Score Optimization**: Best-fit model selection
- **Trend Extrapolation**: 5-year future predictions
- **Boundary Constraints**: Predictions capped at realistic ranges (0-100%)

### **Data Processing**
- **Automatic Data Loading**: Cached data loading for performance
- **Missing Value Handling**: Graceful handling of incomplete data
- **Urban-Rural Aggregation**: Separate analysis for different area types
- **Year-over-Year Comparison**: Temporal trend analysis

## 🎯 Use Cases

### **For Policymakers**
- Identify districts needing urgent digital infrastructure investment
- Compare progress between different regions
- Plan resource allocation based on predictive models

### **For Researchers**
- Analyze digital divide patterns across Nepal
- Study correlation between different access metrics
- Generate insights for academic research

### **For Development Organizations**
- Target interventions in underserved areas
- Monitor progress of digital inclusion initiatives
- Design evidence-based programs

## 🔍 Troubleshooting

### **Common Issues**

1. **"No module named 'streamlit'"**
   ```bash
   pip install streamlit
   ```

2. **"FileNotFoundError: CSV files not found"**
   - Ensure all CSV files are in the `data_processed/` folder
   - Check file names match exactly: `df_2001.csv`, `df_2011.csv`, etc.

3. **Dashboard not opening in browser**
   - Manually navigate to `http://localhost:8501`
   - Try a different port: `streamlit run digital_divide_dashboard.py --server.port 8502`

4. **Performance Issues**
   - Clear Streamlit cache: Click "Clear Cache" in the hamburger menu
   - Restart the dashboard application

### **Data Requirements**
- CSV files must contain required columns (District, Year, Urban_Rural, etc.)
- Data should be properly formatted with numeric values for metrics
- Missing values are handled automatically but may affect predictions

## 🤝 Contributing

Feel free to enhance the dashboard by:
- Adding new visualization types
- Implementing additional predictive models
- Improving the user interface
- Adding more detailed recommendations

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for Digital Nepal Initiative**
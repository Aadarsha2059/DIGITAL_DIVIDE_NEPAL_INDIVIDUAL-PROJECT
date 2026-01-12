# Python Libraries Documentation
## Digital Divide Nepal Dashboard - Library Reference Guide

This document provides a comprehensive explanation of all Python libraries used in the Digital Divide Nepal Dashboard project, detailing how each library contributes to the functionality and analysis capabilities.

---

## 📚 Core Libraries Overview

### 1. **Streamlit** (`streamlit`)
**Purpose**: Web application framework for building interactive dashboards

**How it helps your project**:
- **Interactive Dashboard Creation**: Streamlit enables you to create a user-friendly web interface without writing HTML, CSS, or JavaScript
- **Real-time Data Visualization**: Allows users to interact with your data through dropdowns, sliders, and buttons, updating visualizations instantly
- **Sidebar Navigation**: Provides the sidebar interface where users select districts, years, analysis types, and metrics
- **Data Display**: Renders tables, charts, and formatted text in a clean, professional layout
- **File Downloads**: Enables users to download CSV and Excel files directly from the dashboard

**Key Features Used**:
- `st.sidebar` - Creates the navigation sidebar
- `st.selectbox` - District and year selection dropdowns
- `st.radio` - Analysis type selection
- `st.dataframe` - Displays data tables
- `st.plotly_chart` - Embeds interactive Plotly charts
- `st.metric` - Shows key performance indicators
- `st.cache_data` - Caches data loading for faster performance

**Example in your project**: The entire dashboard interface, from district selection to displaying budget allocation results, is built using Streamlit components.

---

### 2. **Pandas** (`pandas`)
**Purpose**: Data manipulation and analysis library

**How it helps your project**:
- **Data Loading**: Reads CSV files containing census data (2001, 2011, 2021) for all 8 districts
- **Data Cleaning**: Handles missing values, converts data types, and ensures data consistency
- **Data Filtering**: Filters data by district, year, and urban/rural classification
- **Data Aggregation**: Groups data to calculate averages, sums, and other statistics
- **Data Transformation**: Pivots tables, merges datasets, and creates new calculated columns
- **Population Calculations**: Aggregates urban and rural populations to get district totals

**Key Features Used**:
- `pd.read_csv()` - Loads census data files
- `df.groupby()` - Groups data by district, year, or urban/rural
- `df.pivot_table()` - Creates cross-tabulated views for heatmaps
- `df.merge()` - Combines datasets
- `df.filter()` - Filters data based on conditions
- `df.agg()` - Performs aggregations (sum, mean, etc.)

**Example in your project**: When you select "Dhanusha" district and year "2021", Pandas filters the combined dataset to show only relevant records, then calculates averages for internet access, electricity, literacy rates, etc.

---

### 3. **Plotly Express** (`plotly.express`)
**Purpose**: High-level interface for creating interactive visualizations

**How it helps your project**:
- **Quick Chart Creation**: Creates beautiful, interactive charts with minimal code
- **Interactive Features**: Users can zoom, pan, hover for details, and toggle data series
- **Multiple Chart Types**: Supports line charts, bar charts, pie charts, box plots, and more
- **Color Coding**: Automatically assigns colors to different districts or categories
- **Export Capabilities**: Users can download charts as PNG images

**Key Features Used**:
- `px.line()` - Creates line charts showing trends over time (2001-2021)
- `px.bar()` - Creates bar charts for comparing districts
- `px.pie()` - Creates pie charts for distribution analysis
- `px.box()` - Creates box plots showing statistical distributions
- `px.scatter()` - Creates scatter plots for correlation analysis
- `px.imshow()` - Creates heatmaps for matrix visualization

**Example in your project**: When viewing "Yearwise Projection", Plotly Express creates line charts showing how internet access rates changed from 2001 to 2021 for each district, with interactive tooltips showing exact values.

---

### 4. **Plotly Graph Objects** (`plotly.graph_objects`)
**Purpose**: Low-level interface for advanced, customizable visualizations

**How it helps your project**:
- **Advanced Customization**: Provides fine-grained control over chart appearance
- **Complex Visualizations**: Creates multi-panel charts, 3D plots, and radar charts
- **Custom Annotations**: Adds text labels, arrows, and shapes to charts
- **Subplot Creation**: Combines multiple charts into one figure (e.g., budget allocation with ROI and priority scores)
- **Advanced Styling**: Customizes colors, fonts, layouts, and interactions

**Key Features Used**:
- `go.Figure()` - Creates custom figure objects
- `go.Scatter()` - Creates scatter plots with custom styling
- `go.Bar()` - Creates bar charts with custom colors
- `go.Scatter3d()` - Creates 3D scatter plots
- `go.Scatterpolar()` - Creates radar charts
- `make_subplots()` - Creates multi-panel charts

**Example in your project**: In "Budget Allocation", Graph Objects creates a 4-panel subplot showing budget percentage, expected ROI, priority scores, and population vs budget in a single interactive visualization.

---

### 5. **NumPy** (`numpy`)
**Purpose**: Numerical computing library for mathematical operations

**How it helps your project**:
- **Mathematical Calculations**: Performs complex calculations for priority scores, ROI predictions, and statistical analysis
- **Array Operations**: Handles large datasets efficiently
- **Statistical Functions**: Calculates means, medians, standard deviations, and percentiles
- **Logarithmic Scaling**: Uses log functions for population weighting in priority calculations
- **Data Clipping**: Ensures values stay within valid ranges (0-100% for rates)

**Key Features Used**:
- `np.mean()` - Calculates averages
- `np.log10()` - Logarithmic scaling for population factors
- `np.clip()` - Clips values to valid ranges
- `np.random` - Generates random variations (for realistic data)
- `np.array()` - Converts data to arrays for efficient processing

**Example in your project**: When calculating priority scores, NumPy computes logarithmic population factors: `np.log10(total_population / 10000)`, which gives higher weight to larger districts while preventing extreme values.

---

### 6. **Scikit-learn** (`sklearn`)
**Purpose**: Machine learning library for predictive modeling and data analysis

**How it helps your project**:

#### 6.1. **KMeans Clustering** (`sklearn.cluster.KMeans`)
- **Purpose**: Groups districts into clusters based on similar characteristics
- **How it helps**: Identifies districts with similar digital divide patterns (e.g., high electricity but low internet = outlier pattern)
- **Usage**: Creates 2-3 clusters to identify high-need, medium-need, and low-need districts
- **Benefit**: Helps prioritize budget allocation by grouping similar districts together

#### 6.2. **Linear Regression** (`sklearn.linear_model.LinearRegression`)
- **Purpose**: Predicts future trends based on historical data
- **How it helps**: Forecasts internet access rates, electricity coverage, and literacy rates for future years
- **Usage**: Trains on 2001-2021 data to predict 2025, 2030 values
- **Benefit**: Enables forward-looking budget planning and goal setting

#### 6.3. **Polynomial Features** (`sklearn.preprocessing.PolynomialFeatures`)
- **Purpose**: Creates polynomial features for non-linear trend modeling
- **How it helps**: Captures acceleration or deceleration in growth rates (e.g., internet adoption speeding up)
- **Usage**: Transforms year data into polynomial features (year, year², year³)
- **Benefit**: More accurate predictions for metrics with non-linear growth patterns

#### 6.4. **Random Forest Regressor** (`sklearn.ensemble.RandomForestRegressor`)
- **Purpose**: Advanced machine learning model for complex predictions
- **How it helps**: Uses multiple decision trees to predict outcomes more accurately than simple linear regression
- **Usage**: Predicts ROI and expected improvements based on multiple factors (internet, electricity, literacy, population)
- **Benefit**: Handles complex relationships between variables for better accuracy

#### 6.5. **R² Score** (`sklearn.metrics.r2_score`)
- **Purpose**: Measures prediction accuracy
- **How it helps**: Evaluates how well your predictive models fit the data (0-1 scale, 1 = perfect)
- **Usage**: Shows model quality in "Predictive Modeling" section
- **Benefit**: Helps you understand prediction reliability

#### 6.6. **Standard Scaler** (`sklearn.preprocessing.StandardScaler`)
- **Purpose**: Normalizes data to same scale before clustering
- **How it helps**: Ensures internet access (0-100%) and population (thousands) are on comparable scales
- **Usage**: Scales metrics before K-means clustering
- **Benefit**: Prevents large numbers (population) from dominating small numbers (percentages) in clustering

#### 6.7. **Train-Test Split** (`sklearn.model_selection.train_test_split`)
- **Purpose**: Splits data into training and testing sets
- **How it helps**: Trains models on historical data and tests on unseen data to validate accuracy
- **Usage**: Uses 2001-2011 for training, 2021 for testing predictions
- **Benefit**: Ensures models work on new data, not just memorized patterns

**Example in your project**: In "Budget Allocation", KMeans clusters districts into groups. Districts like Siraha and Mahottari (high electricity, low internet) are grouped together as "outlier pattern" districts, receiving higher priority scores.

---

### 7. **SciPy** (`scipy.stats`) - Optional
**Purpose**: Scientific computing library for statistical functions

**How it helps your project**:
- **Statistical Tests**: Performs hypothesis testing and confidence intervals
- **Distribution Analysis**: Analyzes data distributions for normality
- **Confidence Intervals**: Calculates prediction confidence ranges
- **Advanced Statistics**: Provides z-scores, p-values, and correlation coefficients

**Key Features Used**:
- `stats.norm.ppf()` - Calculates confidence intervals for predictions
- Statistical tests for data validation

**Example in your project**: In predictive modeling, SciPy calculates 95% confidence intervals, showing that a predicted 45% internet access rate might actually range from 42% to 48% with 95% confidence.

---

### 8. **Plotly Figure Factory** (`plotly.figure_factory`)
**Purpose**: Specialized functions for creating complex visualizations

**How it helps your project**:
- **Gantt Charts**: Creates timeline visualizations (though removed in latest version)
- **Statistical Charts**: Creates distribution plots and correlation matrices
- **Specialized Visualizations**: Provides ready-made complex chart types

**Key Features Used**:
- `ff.create_gantt()` - Creates project timeline charts (if needed)

---

### 9. **Standard Library Modules**

#### 9.1. **Warnings** (`warnings`)
- **Purpose**: Suppresses non-critical warnings
- **How it helps**: Keeps the dashboard clean by hiding deprecation warnings and data type conversion messages
- **Usage**: `warnings.filterwarnings('ignore')`

#### 9.2. **IO** (`io`)
- **Purpose**: Input/output operations
- **How it helps**: Creates in-memory file objects for CSV/Excel downloads
- **Usage**: Generates downloadable files without saving to disk

#### 9.3. **Datetime** (`datetime`, `timedelta`)
- **Purpose**: Date and time handling
- **How it helps**: Formats dates in reports, calculates time differences for growth rates
- **Usage**: Shows "Last Updated" timestamps, calculates years between census data

#### 9.4. **Base64** (`base64`)
- **Purpose**: Encodes binary data for web transmission
- **How it helps**: Converts CSV/Excel files to downloadable links
- **Usage**: Creates download buttons for data exports

---

## 🔗 Library Integration in Your Project

### Data Flow Example:
1. **Pandas** loads CSV files → `df_2001`, `df_2011`, `df_2021`
2. **Pandas** combines and filters data → `df_combined` filtered by district/year
3. **NumPy** calculates priority scores → mathematical operations
4. **Scikit-learn** performs clustering → `KMeans` groups districts
5. **Scikit-learn** predicts ROI → `RandomForestRegressor` forecasts improvements
6. **Plotly** creates visualizations → `px.line()`, `go.Figure()` render charts
7. **Streamlit** displays everything → `st.plotly_chart()`, `st.dataframe()` show results

### Performance Optimization:
- **Streamlit Caching** (`@st.cache_data`): Caches data loading so CSV files aren't re-read on every interaction
- **Pandas Efficiency**: Uses vectorized operations instead of loops for faster processing
- **NumPy Arrays**: Converts data to arrays for faster mathematical operations

---

## 📊 Library Usage Statistics in Your Project

| Library | Primary Use Cases | Lines of Code Impact |
|---------|------------------|---------------------|
| Streamlit | UI, Navigation, Display | ~40% of code |
| Pandas | Data Loading, Filtering, Aggregation | ~25% of code |
| Plotly | All Visualizations | ~20% of code |
| NumPy | Calculations, Math Operations | ~8% of code |
| Scikit-learn | ML, Clustering, Predictions | ~5% of code |
| Others | Utilities, Helpers | ~2% of code |

---

## 🎯 Key Benefits Summary

1. **Streamlit**: Makes your dashboard accessible to non-technical users through a simple web interface
2. **Pandas**: Handles all data operations efficiently, from loading to complex aggregations
3. **Plotly**: Creates publication-quality, interactive visualizations that engage users
4. **NumPy**: Performs fast mathematical calculations for priority scoring and statistics
5. **Scikit-learn**: Adds AI/ML capabilities for clustering and predictive analytics
6. **SciPy**: Provides advanced statistical validation for predictions

Together, these libraries transform raw census data into an interactive, intelligent dashboard that helps policymakers make data-driven decisions about digital divide interventions in Nepal's Province 2.

---

## 📚 Further Learning Resources

- **Streamlit**: https://docs.streamlit.io/
- **Pandas**: https://pandas.pydata.org/docs/
- **Plotly**: https://plotly.com/python/
- **Scikit-learn**: https://scikit-learn.org/stable/
- **NumPy**: https://numpy.org/doc/

---

*Last Updated: 2024*
*Project: Digital Divide Nepal Dashboard - Province 2 (Madhesh Pradesh) Analysis*

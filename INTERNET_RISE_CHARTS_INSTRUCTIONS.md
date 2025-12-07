# Internet Access Rate Charts - Usage Instructions

## Overview
This project generates trend charts showing Internet Access Rate from 2001 to 2021 for 8 districts in Nepal, with Urban vs Rural comparisons.

## Files Structure
```
DIGITAL_DIVIDE/
├── merge_csv_files.py                           # Merges 2001, 2011, 2021 CSV files
├── generate_all_district_charts.py              # Master script (runs all district scripts)
├── data_processed/
│   ├── df_combined.csv                          # Merged dataset with Year column
│   └── internet_rise_all_districts/             # Output folder for all charts
│       ├── dhanusha_internet_2001_2021.png
│       ├── mahottari_internet_2001_2021.png
│       ├── sarlahi_internet_2001_2021.png
│       ├── bara_internet_2001_2021.png
│       ├── parsa_internet_2001_2021.png
│       ├── rautahat_internet_2001_2021.png
│       ├── siraha_internet_2001_2021.png
│       └── saptari_internet_2001_2021.png
└── codes/
    └── internet_rise_plots/                     # Individual district scripts
        ├── dhanusha_internet_plot.py
        ├── mahottari_internet_plot.py
        ├── sarlahi_internet_plot.py
        ├── bara_internet_plot.py
        ├── parsa_internet_plot.py
        ├── rautahat_internet_plot.py
        ├── siraha_internet_plot.py
        └── saptari_internet_plot.py
```

## Prerequisites
- Python 3.6+
- Required libraries:
  - pandas
  - matplotlib
  - seaborn
  - os (built-in)

Install dependencies:
```bash
pip install pandas matplotlib seaborn
```

## How to Run

### Step 1: Merge CSV Files (if not already done)
If `data_processed/df_combined.csv` doesn't exist, run:
```bash
python merge_csv_files.py
```

This script:
- Loads `df_2001.csv`, `df_2011.csv`, `df_2021.csv`
- Adds a `Year` column to each dataset
- Merges by `District` and `Urban_Rural`
- Adds `Internet_Access_Rate = 0` for 2001 data (internet wasn't widely available)
- Saves merged data to `df_combined.csv`

### Step 2: Generate All Charts (Recommended)
Run the master script from the project root:
```bash
python generate_all_district_charts.py
```

This will:
- Execute all 8 district scripts sequentially
- Generate all charts automatically
- Save PNG files to `data_processed/internet_rise_all_districts/`
- Display a summary of success/failure for each district

### Step 3: Generate Individual District Charts
You can also run individual scripts directly:
```bash
# From the project root
python codes/internet_rise_plots/dhanusha_internet_plot.py
python codes/internet_rise_plots/mahottari_internet_plot.py
# ... etc for other districts
```

## Output Location
All charts are saved to:
```
data_processed/internet_rise_all_districts/
```

Chart naming format:
- `{district_name}_internet_2001_2021.png` (lowercase district name)

## Chart Features
Each chart includes:
- **X-axis**: Year (2001, 2011, 2021)
- **Y-axis**: Internet Access Rate (%)
- **Two lines**: Urban (blue) and Rural (purple)
- **Smooth trend lines**: Dashed lines showing trends
- **High-quality output**: 300 DPI resolution
- **Clear labels**: District name in title, legend showing Urban vs Rural
- **Gridlines**: Subtle grid for easier reading

## Districts Included
1. Dhanusha
2. Mahottari
3. Sarlahi
4. Bara
5. Parsa
6. Rautahat
7. Siraha
8. Saptari

## Viewing the Charts
After running the scripts, open the PNG files from:
```
data_processed/internet_rise_all_districts/
```

You can:
- Double-click PNG files to view in your default image viewer
- Open in any image editing software
- Use in presentations or reports

## Troubleshooting

### Error: "File not found: df_combined.csv"
**Solution**: Run `python merge_csv_files.py` first to create the merged dataset.

### Error: "Module not found: pandas/matplotlib/seaborn"
**Solution**: Install missing libraries:
```bash
pip install pandas matplotlib seaborn
```

### Error: Charts not generating
**Solution**: 
1. Check that `data_processed/df_combined.csv` exists
2. Verify all CSV files (df_2001.csv, df_2011.csv, df_2021.csv) are in `data_processed/`
3. Ensure you have write permissions in the output directory

## Notes
- The 2001 data has `Internet_Access_Rate = 0` since internet wasn't widely available
- Charts use consistent color scheme (Urban: blue, Rural: purple)
- All scripts use absolute paths, so they work from any directory
- Charts are saved at 300 DPI for high-quality output suitable for publications


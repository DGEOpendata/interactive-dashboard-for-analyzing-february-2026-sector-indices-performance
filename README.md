markdown
# February 2026 Sector Indices Performance Dashboard

## Overview
This project provides an interactive dashboard for analyzing the February 2026 Sector Indices Performance Summary dataset. The dashboard is built using Dash, a Python framework for building web applications. It allows users to filter, visualize, and export data related to sector indices performance in February 2026.

## Features
- **Interactive Filters**: Select specific indices and date ranges to focus your analysis.
- **Custom Visualizations**: Generate line charts to visualize trends in closing values.
- **Downloadable Data**: Export filtered data in CSV format for further analysis.

## Prerequisites
- Python 3.8 or higher
- Required libraries: pandas, matplotlib, plotly, dash

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/username/february-2026-sector-indices-dashboard.git
   
2. Navigate to the project directory:
   bash
   cd february-2026-sector-indices-dashboard
   
3. Install the required dependencies:
   bash
   pip install -r requirements.txt
   

## Usage
1. Place the dataset file (`Indices_Summary_FEB_2026.csv`) in the root directory.
2. Run the app:
   bash
   python app.py
   
3. Open your browser and navigate to `http://127.0.0.1:8050` to access the dashboard.

## How to Use the Dashboard
- **Select Index**: Use the dropdown menu to select the index you wish to analyze.
- **Select Date Range**: Use the date picker to choose the desired date range.
- **View Charts**: The line chart will update automatically based on your selections.
- **Download Data**: Click the 'Download Data' button to export the filtered data as a CSV file.

## Contributing
We welcome contributions! Please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

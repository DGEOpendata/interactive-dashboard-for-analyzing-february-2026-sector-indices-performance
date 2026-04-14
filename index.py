python
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import dash
from dash import dcc, html, Input, Output

# Load dataset
data = pd.read_csv('Indices_Summary_FEB_2026.csv')

# Initialize Dash app
app = dash.Dash(__name__)
app.title = 'Sector Indices Performance Dashboard'

# Layout of the dashboard
app.layout = html.Div([
    html.H1('February 2026 Sector Indices Performance Dashboard'),
    html.Label('Select Index:'),
    dcc.Dropdown(
        id='index-selector',
        options=[{'label': idx, 'value': idx} for idx in data['index_name'].unique()],
        value=data['index_name'].unique()[0]
    ),
    html.Label('Select Date Range:'),
    dcc.DatePickerRange(
        id='date-range-picker',
        start_date=data['date'].min(),
        end_date=data['date'].max(),
        display_format='YYYY-MM-DD'
    ),
    dcc.Graph(id='performance-chart'),
    html.Button('Download Data', id='download-btn'),
    dcc.Download(id='download-dataframe-csv')
])

# Callbacks
@app.callback(
    Output('performance-chart', 'figure'),
    [Input('index-selector', 'value'),
     Input('date-range-picker', 'start_date'),
     Input('date-range-picker', 'end_date')]
)
def update_chart(selected_index, start_date, end_date):
    filtered_data = data[(data['index_name'] == selected_index) &
                         (data['date'] >= start_date) &
                         (data['date'] <= end_date)]
    fig = px.line(
        filtered_data, x='date', y='closing_value', 
        title=f'{selected_index} - Closing Values',
        labels={'closing_value': 'Closing Value', 'date': 'Date'}
    )
    return fig

@app.callback(
    Output('download-dataframe-csv', 'data'),
    Input('download-btn', 'n_clicks'),
    prevent_initial_call=True
)
def download_data(n_clicks):
    return dcc.send_data_frame(data.to_csv, 'filtered_data.csv')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

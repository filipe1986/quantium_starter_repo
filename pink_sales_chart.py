from dash import Dash, html, dcc

import pandas as pd
import plotly.express as px

# reading the csv
df = pd.read_csv('pink_df.csv')

df['date'] = pd.to_datetime(df['date']) # changing date column from str to datetime

df = df.sort_values(by='date') # sorting the data frame according to date column

app = Dash() # initializing the app

fig = px.line(df, x='date', y='sales')

options = [
    {'label': 'North', 'value': 'north'},
    {'label': 'East', 'value': 'east'},
    {'label': 'South', 'value': 'south'},
    {'label': 'West', 'value': 'west'},
    {'label': 'All', 'value': 'all'}
]

app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Over Time'),
    
    # radio button
    dcc.RadioItems(
        id='region_filter',
        options=options,
        value='all' # This sets the default starting choice
    ),

    dcc.Graph(
        id='sales_line_chart',
        figure=fig)
])

@app.callback(
    Output('sales_line_chart', 'figure'),
    Input('region_filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    updated_fig = px.line(filtered_df, x='date', y='sales')
    return updated_fig

if __name__ == '__main__':
    app.run(debug=True)


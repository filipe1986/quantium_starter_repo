from dash import Dash, html, dcc
from dash.dependencies import Input, Output
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
    
    # filters
    html.Div([
        html.Label('Filter by Region:', className="mg-2"),
        dcc.RadioItems(
            id='region_filter',
            options=options, 
            value='all',
            inline=True,
            className='mb-3'
        ),
    ], className="container p-4 mb-4"),

    # graph container
    html.Div([
        dcc.Graph(
            id='sales_line_chart',
            figure=fig
        )
    ], className="container")

], className='p-4')

@app.callback(
    Output('sales_line_chart', 'figure'),
    Input('region_filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df.groupby('date', as_index=False)['sales'].sum()
        line_width = 3.5
        color = 'black'
        title = 'Pink Morse Sales - All Regions'
    else:
        filtered_df = df[df['region'] == selected_region]
        line_width = 2.8
        region_colors = {
            'north': 'red',
            'east': 'blue',
            'south': 'green',
            'west': 'orange'
        }
        color = region_colors.get(selected_region.lower(), 'blue')
        title = f'Pink Morsel Sales - {selected_region.title()} Region'

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=title,
        color_discrete_sequence=[color] # forcing single color
    )

    fig.update_layout(height=650, title_font_size=20)
    fig.update_traces(line=dict(width=line_width))

    return fig

if __name__ == '__main__':
    app.run(debug=True)


from dash import Dash, html, dcc

import pandas as pd
import plotly.express as px

# reading the csv
df = pd.read_csv('pink_df.csv')

df['date'] = pd.to_datetime(df['date']) # changing date column from str to datetime

df = df.sort_values(by='date') # sorting the data frame according to date column

app = Dash() # initializing the app

fig = px.line(df, x='date', y='sales')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Over Time'),    
    dcc.Graph(
        id='sales_line_chart',
        figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)


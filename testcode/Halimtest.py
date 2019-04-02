import datetime
import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from collections import deque
import plotly
import random
from dash.dependencies import Input, Output
import numpy as np

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)
app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div([
        html.H4('Random number test'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
)

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))
    X.append(datetime.datetime.now())

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(title='Date'),
                                                yaxis=dict(title='Temperature'),)}

with open(r'test.csv', 'a', newline='') as csvfile:
    fieldnames = ['DATE', 'TEMP']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow({'DATE':'1', 'TEMP':'1'})
if __name__ == '__main__':
    app.run_server(debug=True)

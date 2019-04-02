import datetime
 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from collections import deque
import plotly
import random
from dash.dependencies import Input, Output
from sense_hat import SenseHat
 
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)
app = dash.Dash(__name__)
 
app.layout = html.Div(
    html.Div([
        html.H4('Random number test'),
        dcc.Graph(id='live-update-graph'),
        dcc.Graph(id='temp-update-graph'),
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
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))
 
    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )
 
    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}
 
 
if __name__ == '__main__':
    app.run_server(debug=True)

@app.callback(Output('temp-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    X.append(X[-1]+1)
    Y.append(SenseHat.get_temperature)
 
    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )
 
    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}
 
 
if __name__ == '__main__':
    app.run_server(debug=True)

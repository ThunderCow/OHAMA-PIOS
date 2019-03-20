import datetime

import dash
from sense_hat import SenseHat
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from collections import deque
import plotly
import random
from dash.dependencies import Input, Output

sense = SenseHat()

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)
Z = deque(maxlen=20)
Z.append(1)
app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div([
        html.H4('Random testing for different sensors'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*3000, # in milliseconds
            n_intervals=0
        )
    ])
)

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    X.append(X[-1]+1)
    Y.append("%.2f" % sense.get_temperature())
    Z.append("%.2f" % sense.get_temperature_from_pressure())

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            z=list(Z),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y,Z),max(Y,Z)]),)}


if __name__ == '__main__':
    app.run_server(debug=True)

import datetime
from sense_hat import SenseHat
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from collections import deque
import plotly
import random
from dash.dependencies import Input, Output

sense = SenseHat()

X = deque(maxlen=20)
R = deque(maxlen=20)
X.append(1)
R.append(1)
Y = deque(maxlen=20)
Q = deque(maxlen=20)
Y.append(1)
Q.append(1)
A = deque(maxlen=20)
B = deque(maxlen=20)
A.append(1)
B.append(1)
C = deque(maxlen=20)
D = deque(maxlen=20)
C.append(1)
D.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div([
        html.H4('temprature test here'),
        dcc.Graph(id='live-update-graph'),
        html.H4('pressure test graph'),
        dcc.Graph(id='temp-update-graph'),
        html.H4('temp-humidity test'),
        dcc.Graph(id='temp2-update-graph'),
        html.H4('temp-pressure test'),
        dcc.Graph(id='temp3-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=2*1000, # in milliseconds
            n_intervals=0
        )
    ])
)


@app.callback([Output('live-update-graph', 'figure'),
               Output('temp-update-graph', 'figure'),
               Output('temp2-update-graph', 'figure'),
               Output('temp3-update-graph', 'figure')],
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    R.append(R[-1]+1)
    Q.append("%.2f" % sense.get_pressure())

    X.append(X[-1] + 1)
    Y.append("%.2f" % sense.get_temperature())

    A.append(X[-1] + 1)
    B.append("%.2f" % sense.get_humidity())

    C.append(X[-1] + 1)
    D.append("%.2f" % sense.get_temperature_from_pressure())

    data1 = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )
    rdata1 = {'data': [data1], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                   yaxis=dict(range=[min(Y), max(Y)]),)}
    data2 = plotly.graph_objs.Scatter(
            x=list(R),
            y=list(Q),
            name='Scatter',
            mode='lines+markers'
            )
    rdata2 = {'data': [data2], 'layout': go.Layout(xaxis=dict(range=[min(R), max(R)]),
                                                   yaxis=dict(range=[min(Q), max(Q)]),)}

    data3 = plotly.graph_objs.Scatter(
            x=list(A),
            y=list(B),
            name='Scatter',
            mode='lines+markers'
            )
    rdata3 = {'data': [data3], 'layout': go.Layout(xaxis=dict(range=[min(A), max(A)]),
                                                   yaxis=dict(range=[min(B), max(B)]),)}

    data4 = plotly.graph_objs.Scatter(
            x=list(C),
            y=list(D),
            name='Scatter',
            mode='lines+markers'
            )
    rdata4 = {'data': [data4], 'layout': go.Layout(xaxis=dict(range=[min(C), max(C)]),
                                                   yaxis=dict(range=[min(D), max(D)]),)}
    return rdata1, rdata2, rdata3, rdata4


if __name__ == '__main__':
    app.run_server(debug=True)



# importing pythong libraries
import datetime
import time
#from sense_hat import SenseHat
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from collections import deque
import plotly
import random
from dash.dependencies import Input, Output
import exportCsv
from sense_hat import SenseHat

sense = SenseHat()
app = dash.Dash(__name__)

export = exportCsv.CsvExport()
#sense = SenseHat()

X = deque(maxlen=20)
Y = deque(maxlen=20)
R = deque(maxlen=20)
Q = deque(maxlen=20)
A = deque(maxlen=20)
B = deque(maxlen=20)
C = deque(maxlen=20)
D = deque(maxlen=20)
E = deque(maxlen=20)
F = deque(maxlen=20)

# appending varbls
X.append(1)
R.append(1)
Y.append(1)
Q.append(1)
A.append(1)
B.append(1)
C.append(1)
D.append(1)
E.append(1)
F.append(1)
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
        html.H4('temp-humidity test'),
        dcc.Graph(id='temp5-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=5 * 1000,  # in milliseconds
            n_intervals=0
        )
    ])
)

# starting the server
def start_server():
    app.run_server(debug=True)


@app.callback([Output('live-update-graph', 'figure'),
               Output('temp-update-graph', 'figure'),
               Output('temp2-update-graph', 'figure'),
                   Output('temp3-update-graph', 'figure'),
                   Output('temp5-update-graph', 'figure')],
               [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    dt_log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    X.append(datetime.datetime.now())
    input1 = ("%.2f" % sense.get_temperature())
    Y.append(input1)

    R.append(dt_log)
    input2 = ("%.2f" % sense.get_pressure())
    Q.append(input2)
    A.append(datetime.datetime.now())
    input3 = ("%.2f" % sense.get_humidity())
    B.append(input3)

    C.append(datetime.datetime.now())
    input4 = ("%.2f" % sense.get_temperature_from_pressure())
    D.append(input4)

    E.append(datetime.datetime.now())
    input5 = ("%.2f" % sense.get_temperature_from_humidity())
    F.append(input5)
    export.writeData(dt_log, input1, input2, input3, input4, input5)

    data1 = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )
    rdata1 = {'data': [data1], 'layout': go.Layout(xaxis=dict(title='DATES'),
                                                   yaxis=dict(title='Temprature'), )}
    data2 = plotly.graph_objs.Scatter(
        x=list(R),
        y=list(Q),
        name='Scatter',
        mode='lines+markers'
    )
    rdata2 = {'data': [data2], 'layout': go.Layout(xaxis=dict(title='DATES'),
                                                   yaxis=dict(title='Pressure'), )}

    data3 = plotly.graph_objs.Scatter(
        x=list(A),
        y=list(B),
        name='Scatter',
        mode='lines+markers'
    )
    rdata3 = {'data': [data3], 'layout': go.Layout(xaxis=dict(title='DATES'),
                                                   yaxis=dict(title='Humidity'), )}

    data4 = plotly.graph_objs.Scatter(
        x=list(C),
        y=list(D),
        name='Scatter',
        mode='lines+markers'
    )
    rdata4 = {'data': [data4], 'layout': go.Layout(xaxis=dict(title='DATES'),
                                                   yaxis=dict(title='Temp_from_Pressure'), )}

    data5 = plotly.graph_objs.Scatter(
        x=list(E),
        y=list(F),
        name='scatter',
        mode='lines+markers'
    )
    rdata5 = {'data': [data5], 'layout': go.Layout(xaxis=dict(title='DATES'),
                                                   yaxis=dict(title='Temp_from_Humidity'), )}

    return rdata1, rdata2, rdata3, rdata4, rdata5

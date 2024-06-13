import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import random
import datetime
import plotly.graph_objs as go
import threading
import time

# Initialiseer de Dash app
app = dash.Dash(__name__)

# Initialiseer een lijst om de datapunten op te slaan
data_points = []

# Functie om data continu te genereren en op te slaan in de lijst
def generate_data():
    while True:
        current_time = datetime.datetime.now()
        blood_pressure = random.randint(60, 120)
        oxygen_levels = random.randint(90, 100)
        
        # Append huidig datapunt aan de lijst
        data_point = {'time': current_time, 'blood_pressure': blood_pressure, 'oxygen_levels': oxygen_levels}
        data_points.append(data_point)
        
        time.sleep(1)  # Wacht 1 seconde voordat het volgende datapunt wordt gegenereerd

# Start een aparte thread om de data continu te genereren
data_thread = threading.Thread(target=generate_data)
data_thread.daemon = True
data_thread.start()

# Definieer de layout van de Dash app
app.layout = html.Div([
    dcc.Tabs(id='tabs', value='Home', children=[
        dcc.Tab(label='Home', value='Home'),
        dcc.Tab(label='Blood', value='Blood'),
        dcc.Tab(label='Oxygen', value='Oxygen'),
    ]),
    html.Div(id='page-content'),
    dcc.Interval(
        id='graph-update',
        interval=1000,  # Update de grafiek elke 1000 ms (1 seconde)
        n_intervals=0
    )
])

# Callback functie om de inhoud van het geselecteerde tabblad weer te geven
@app.callback(
    Output('page-content', 'children'),
    [Input('tabs', 'value'),
     Input('graph-update', 'n_intervals')]
)
def render_content(tab, n_intervals):
    if tab == 'Home':
        # Existing code for home tab
        # Retrieve blood pressure and oxygen data
        x_data = [data_point['time'] for data_point in data_points]
        blood_pressure_data = [data_point['blood_pressure'] for data_point in data_points]
        oxygen_levels_data = [data_point['oxygen_levels'] for data_point in data_points]

        trace1 = go.Scatter(x=x_data, y=blood_pressure_data, mode='lines+markers', name='Blood Pressure')
        trace2 = go.Scatter(x=x_data, y=oxygen_levels_data, mode='lines+markers', name='Oxygen Levels')

        layout = go.Layout(
            title='Real-time Health Data',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Value'},
            showlegend=True
        )

        graph = dcc.Graph(id='live-graph', figure={'data': [trace1, trace2], 'layout': layout})

        return html.Div([
            html.H1('Home'),
            html.P("Real-time Health Data"),
            graph
        ])
    elif tab == 'Blood':
        # Retrieve blood pressure data for the Blood page
        x_data = [data_point['time'] for data_point in data_points]
        blood_pressure_data = [data_point['blood_pressure'] for data_point in data_points]

        trace = go.Scatter(x=x_data, y=blood_pressure_data, mode='lines+markers', name='Blood Pressure')

        layout = go.Layout(
            title='Blood Pressure Data',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Blood Pressure'},
            showlegend=True
        )

        blood_graph = dcc.Graph(id='blood-graph', figure={'data': [trace], 'layout': layout})

        return html.Div([
            html.H1('Blood'),
            blood_graph
        ])
    elif tab == 'Oxygen':
        # Retrieve oxygen levels data for the Oxygen page
        x_data = [data_point['time'] for data_point in data_points]
        oxygen_levels_data = [data_point['oxygen_levels'] for data_point in data_points]

        trace = go.Scatter(x=x_data, y=oxygen_levels_data, mode='lines+markers', name='Oxygen Levels')

        layout = go.Layout(
            title='Oxygen Levels Data',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Oxygen Levels'},
            showlegend=True
        )

        oxygen_graph = dcc.Graph(id='oxygen-graph', figure={'data': [trace], 'layout': layout})

        return html.Div([
            html.H1('Oxygen'),
            oxygen_graph
        ])

# Callback functie om de grafiek continu bij te werken met nieuwe datapunten
@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph(n):
    # Maak de data klaar voor de grafiek
    x_data = [data_point['time'] for data_point in data_points]
    blood_pressure_data = [data_point['blood_pressure'] for data_point in data_points]
    oxygen_levels_data = [data_point['oxygen_levels'] for data_point in data_points]
    
    # Maak de plotly grafiek
    trace1 = go.Scatter(x=x_data, y=blood_pressure_data, mode='lines+markers', name='Blood Pressure')
    trace2 = go.Scatter(x=x_data, y=oxygen_levels_data, mode='lines+markers', name='Oxygen Levels')
    
    layout = go.Layout(
        title='Real-time Health Data',
        xaxis={'title': 'Time'},
        yaxis={'title': 'Value'},
        showlegend=True
    )
    
    return {'data': [trace1, trace2], 'layout': layout}

# Start de Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

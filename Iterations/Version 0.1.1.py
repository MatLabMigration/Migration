import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import random
import datetime
import plotly.graph_objs as go
import threading
import time

app = dash.Dash(__name__)

# Initialize a list to store data points
data_points = []

# Function to continuously generate and store data in the list
def generate_data():
    while True:
        current_time = datetime.datetime.now()
        blood_pressure = random.randint(60, 120)
        oxygen_levels = random.randint(90, 100)
        heart_rate = random.randint(60, 100)
        hydration = random.randint(0, 100)
        
        # Put data into the list
        data_point = {'time': current_time, 'blood_pressure': blood_pressure, 
                      'oxygen_levels': oxygen_levels, 'heart_rate': heart_rate, 
                      'hydration': hydration}
        data_points.append(data_point)
        
        time.sleep(1)  # Wait 1 second before generating the next data point

# Start a separate thread to continuously generate data
data_thread = threading.Thread(target=generate_data)
data_thread.daemon = True
data_thread.start()

app.layout = html.Div([
    dcc.Tabs(id='tabs', value='Home', children=[
        dcc.Tab(label='Home', value='Home'),
        dcc.Tab(label='Heart Rate', value='Heart Rate'),
        dcc.Tab(label='Hydration', value='Hydration'),
    ]),
    html.Div(id='page-content'),
    dcc.Interval(
        id='graph-update',
        interval=1000,  # Update the graph every 1000 ms (1 second)
        n_intervals=0
    )
])

# Callback function to render the content of the selected tab
@app.callback(
    Output('page-content', 'children'),
    [Input('tabs', 'value'),
     Input('graph-update', 'n_intervals')]
)
def render_content(tab, n_intervals):
    if tab == 'Home':
        # Retrieve data for the home page
        x_data = [data_point['time'] for data_point in data_points]
        blood_pressure_data = [data_point['blood_pressure'] for data_point in data_points]
        oxygen_levels_data = [data_point['oxygen_levels'] for data_point in data_points]

        trace1 = go.Scatter(x=x_data, y=oxygen_levels_data, mode='lines+markers', name='Oxygen Levels', line=dict(color='green'), marker=dict(color='green'))
        trace2 = go.Scatter(x=x_data, y=blood_pressure_data, mode='lines+markers', name='Blood Pressure')

        layout = go.Layout(
            title='Real-time Health Data',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Value'},
            showlegend=True
        )

        graph = dcc.Graph(
            id='live-graph',
            figure={'data': [trace1, trace2], 'layout': layout},
            config={'scrollZoom': True, 'staticPlot': False}
        )

        return html.Div([
            html.H1('Home'),
            html.P("Real-time Health Data"),
            graph
        ])
    elif tab in ['Heart Rate', 'Hydration']:
        # Retrieve data for the selected tab
        x_data = [data_point['time'] for data_point in data_points]
        
        if tab == 'Heart Rate':
            y_data = [data_point['heart_rate'] for data_point in data_points]
            ylabel = 'Heart Rate'
            line_color = 'red'
            marker_color = 'red'
        elif tab == 'Hydration':
            y_data = [data_point['hydration'] for data_point in data_points]
            ylabel = 'Hydration'
            line_color = 'blue'
            marker_color = 'blue'

        trace = go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines+markers',
            name=ylabel,
            line=dict(color=line_color), 
            marker=dict(color=marker_color) 
        )

        layout = go.Layout(
            title=f'{ylabel} Data',
            xaxis={'title': 'Time'},
            yaxis={'title': ylabel},
            showlegend=True
        )

        graph = dcc.Graph(id=f'{tab.lower()}-graph', figure={'data': [trace], 'layout': layout})

        return html.Div([
            html.H1(tab),
            graph
        ])


# Callback function to continuously update the graph with new data points
@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph(n):
    # Prepare data for the graph
    x_data = [data_point['time'] for data_point in data_points]
    blood_pressure_data = [data_point['blood_pressure'] for data_point in data_points]
    oxygen_levels_data = [data_point['oxygen_levels'] for data_point in data_points]
    
    trace1 = go.Scatter(x=x_data, y=oxygen_levels_data, mode='lines+markers', name='Oxygen Levels', line=dict(color='green'), marker=dict(color='green'))
    trace2 = go.Scatter(x=x_data, y=blood_pressure_data, mode='lines+markers', name='Blood Pressure')
    
    layout = go.Layout(
        title='Real-time Health Data',
        xaxis={'title': 'Time'},
        yaxis={'title': 'Value'},
        showlegend=True,
        uirevision=n 
    )
    
    return {'data': [trace1, trace2], 'layout': layout}

# Start the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

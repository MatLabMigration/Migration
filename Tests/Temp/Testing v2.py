import dash
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Output, Input
import random
import datetime
import threading
import time

# Initialize the Dash app
app = dash.Dash(__name__)

# Define CSS styles for the navbar and links
navbar_style = {
    'background-color': '#f8f9fa',
    'padding': '10px 20px',
    'border-bottom': '1px solid #dee2e6',
    'display': 'flex',
    'justify-content': 'space-between'
}

navbar_link_style = {
    'margin-right': '10px',
    'color': '#007bff',
    'text-decoration': 'none',
    'font-weight': 'bold'
}

# Function to generate random data (for demo purposes)
def generate_data(data_points):
    while True:
        current_time = datetime.datetime.now()
        blood_pressure = random.randint(60, 120)
        oxygen_levels = random.randint(90, 100)
        
        # Append current data point
        data_point = {'time': current_time, 'blood_pressure': blood_pressure, 'oxygen_levels': oxygen_levels}
        data_points.append(data_point)
        
        time.sleep(1)  # Wait for 1 second

# Layout of the app
app.layout = html.Div([
    html.Nav([
        html.A('Home', href='/', style=navbar_link_style),
        html.A('Blood', href='/blood', style=navbar_link_style),
        html.A('Oxygen', href='/oxygen', style=navbar_link_style)
    ], style=navbar_style),
    dcc.Graph(id='live-update-graph', config={'scrollZoom': True}),
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)
])

# Initialize data structure for storing real-time data
data_points = []

# Start a separate thread to generate data
data_thread = threading.Thread(target=generate_data, args=(data_points,))
data_thread.daemon = True
data_thread.start()

# Callback to update the graph
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    # Extract data for plotting
    times = [data['time'] for data in data_points]
    blood_pressure = [data['blood_pressure'] for data in data_points]
    oxygen_levels = [data['oxygen_levels'] for data in data_points]
    
    # Create traces for blood pressure and oxygen levels
    traces = [
        go.Scatter(x=times, y=blood_pressure, mode='lines+markers', name='Blood Pressure'),
        go.Scatter(x=times, y=oxygen_levels, mode='lines+markers', name='Oxygen Levels')
    ]

    return {
        'data': traces,
        'layout': {
            'title': 'Real-time Newborn Monitoring',
            'xaxis': {'title': 'Time'},
            'yaxis': {'title': 'Value'},
            'showlegend': True,
            'uirevision': 'constant'  # Set a constant uirevision to preserve zoom and view
        }
    }

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

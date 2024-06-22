import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import random
import plotly.graph_objs as go
import datetime
import threading
import time

# Initialize the Dash app
app = dash.Dash(__name__)

# Initialize data points
x_data = []
y_data = []

# Function to generate random data
def generate_data():
    global x_data, y_data
    while True:
        x_data.append(datetime.datetime.now())
        y_data.append(random.randint(0, 100))
        time.sleep(1)  # Wait 1 second before generating the next data point

# Start a separate thread to generate data
data_thread = threading.Thread(target=generate_data)
data_thread.daemon = True
data_thread.start()

# Define the layout of the Dash app
app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='graph-update',
        interval=1000,  # Update the graph every 1000 ms (1 second)
        n_intervals=0
    )
])

# Callback function to update the graph with new data
@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph(n):
    # Create a scatter plot
    trace = go.Scatter(x=x_data, y=y_data, mode='lines+markers')

    # Define the layout
    layout = go.Layout(
        title='Real-time Data',
        xaxis=dict(title='Time'),
        yaxis=dict(title='Value'),
        showlegend=False,
        uirevision='constant'  # Preserve zoom state with a constant uirevision
    )

    return {'data': [trace], 'layout': layout}

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
